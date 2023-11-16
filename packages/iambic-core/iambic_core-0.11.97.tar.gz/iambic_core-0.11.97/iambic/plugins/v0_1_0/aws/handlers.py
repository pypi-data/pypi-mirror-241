from __future__ import annotations

import asyncio
import base64
import json
import os
import uuid
from itertools import chain
from typing import TYPE_CHECKING, Coroutine, Optional, Union

import boto3

from iambic.config.dynamic_config import ExtendsConfig, ExtendsConfigKey
from iambic.core.context import ctx
from iambic.core.iambic_enum import Command, IambicManaged
from iambic.core.logger import log
from iambic.core.models import (
    BaseTemplate,
    ExecutionMessage,
    TemplateChangeDetails,
    Variable,
)
from iambic.core.parser import load_templates
from iambic.core.template_generation import (
    get_existing_template_map,
    templatize_resource,
)
from iambic.core.utils import async_batch_processor, gather_templates, yaml
from iambic.plugins.v0_1_0.aws.event_bridge.models import (
    GroupMessageDetails,
    ManagedPolicyMessageDetails,
    PermissionSetMessageDetails,
    RoleMessageDetails,
    SCPMessageDetails,
    UserMessageDetails,
)
from iambic.plugins.v0_1_0.aws.iam.group.models import AWS_IAM_GROUP_TEMPLATE_TYPE
from iambic.plugins.v0_1_0.aws.iam.group.template_generation import (
    collect_aws_groups,
    generate_aws_group_templates,
)
from iambic.plugins.v0_1_0.aws.iam.policy.models import AWS_MANAGED_POLICY_TEMPLATE_TYPE
from iambic.plugins.v0_1_0.aws.iam.policy.template_generation import (
    collect_aws_managed_policies,
    generate_aws_managed_policy_templates,
)
from iambic.plugins.v0_1_0.aws.iam.role.template_generation import (
    collect_aws_roles,
    generate_aws_role_templates,
)
from iambic.plugins.v0_1_0.aws.iam.user.models import AWS_IAM_USER_TEMPLATE_TYPE
from iambic.plugins.v0_1_0.aws.iam.user.template_generation import (
    collect_aws_users,
    generate_aws_user_templates,
)
from iambic.plugins.v0_1_0.aws.identity_center.permission_set.models import (
    AWS_IDENTITY_CENTER_PERMISSION_SET_TEMPLATE_TYPE,
)
from iambic.plugins.v0_1_0.aws.identity_center.permission_set.template_generation import (
    collect_aws_permission_sets,
    generate_aws_permission_set_templates,
)
from iambic.plugins.v0_1_0.aws.identity_center.permission_set.utils import (
    generate_permission_set_map,
)
from iambic.plugins.v0_1_0.aws.models import AWSAccount
from iambic.plugins.v0_1_0.aws.organizations.scp.models import AWS_SCP_POLICY_TEMPLATE
from iambic.plugins.v0_1_0.aws.organizations.scp.template_generation import (
    collect_aws_scp_policies,
    generate_aws_scp_policy_templates,
    get_organizations_account_map,
)
from iambic.plugins.v0_1_0.aws.organizations.scp.utils import (
    service_control_policy_is_enabled,
)
from iambic.plugins.v0_1_0.aws.utils import get_aws_account_map

if TYPE_CHECKING:
    from iambic.plugins.v0_1_0.aws.iambic_plugin import AWSConfig


async def load(config: AWSConfig) -> AWSConfig:
    config_account_idx_map = {
        account.account_id: idx for idx, account in enumerate(config.accounts)
    }
    if config.organizations:
        if any(account.hub_role_arn for account in config.accounts):
            log.warning(
                "You have a `hub_role_arn` defined on an `aws.account` specified in your IAMbic configuration that will be ignored. "
                "IAMbic will prefer the `hub_role_arn` specified under your AWS Organization. To remove this message, "
                "please remove the `hub_role_arn` specified in an `AWS Account`."
            )
        orgs_accounts = await asyncio.gather(
            *[org.get_accounts() for org in config.organizations]
        )
        for org_accounts, org in zip(orgs_accounts, config.organizations):
            for account in org_accounts:
                if (
                    account_elem := config_account_idx_map.get(account.account_id)
                ) is not None:
                    config.accounts[
                        account_elem
                    ].hub_session_info = account.hub_session_info
                    config.accounts[
                        account_elem
                    ].identity_center_details = account.identity_center_details

                    # if the account is an organization account, set the organization details
                    if org.org_account_id == account.account_id:
                        await config.accounts[
                            account_elem
                        ].set_account_organization_details(
                            organization=org,
                            config=config,
                        )
                else:
                    log.warning(
                        "Account not found in config. Account will be ignored.",
                        account_id=account.account_id,
                        account_name=account.account_name,
                    )
    elif config.accounts:
        hub_account = [account for account in config.accounts if account.hub_role_arn]
        if len(hub_account) > 1:
            raise AttributeError("Only one AWS Account can specify the hub_role_arn")
        elif not hub_account:
            raise AttributeError("One of the AWS Accounts must define the hub_role_arn")
        else:
            hub_account = hub_account[0]
            await hub_account.set_hub_session_info()
            hub_session_info = hub_account.hub_session_info
            if not hub_session_info:
                raise Exception("Unable to assume into the hub_role_arn")
            for account in config.accounts:
                if account.account_id != hub_account.account_id:
                    account.hub_session_info = hub_session_info

    # Set up the dynamic account attributes
    for idx, account in enumerate(config.accounts):
        config.accounts[
            idx
        ].enable_iam_user_credentials = config.enable_iam_user_credentials
        config.accounts[idx].variables.extend(
            [
                Variable(key="account_id", value=account.account_id),
                Variable(key="account_name", value=account.account_name),
            ]
        )

    # Preload the iam client to improve performance
    await asyncio.gather(
        *[account.get_boto3_client("iam") for account in config.accounts],
        return_exceptions=True,
    )

    return config


async def apply_identity_center_templates(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    templates: list[BaseTemplate],
    remote_worker=None,
) -> list[TemplateChangeDetails]:
    """
    The async_apply_callable for IdentityCenter (SSO) resources.

    :param exe_message: Execution context
    :param config: The config object.
    :param templates: The list of templates to apply.
    :param remote_worker: The remote worker to use for applying templates.
    """
    await config.set_identity_center_details(exe_message.provider_id)
    return await async_batch_processor(
        [template.apply(config) for template in templates],
        5,
        0.5,
    )


async def apply_iam_templates(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    templates: list[BaseTemplate],
    remote_worker=None,
) -> list[TemplateChangeDetails]:
    """
    The async_apply_callable for IAM resource.

    :param exe_message: Execution context
    :param config: The config object.
    :param templates: The list of templates to apply.
    :param remote_worker: The remote worker to use for applying templates.
    """
    if config.spoke_role_is_read_only:
        log.critical("Unable to apply resources when spoke_role_is_read_only is True")
        return []

    await generate_permission_set_map(config.accounts, templates)

    template_changes: list[TemplateChangeDetails] = []
    excluded_from_batch = [AWS_MANAGED_POLICY_TEMPLATE_TYPE]

    if managed_policy_tasks := [
        template.apply(config)
        for template in templates
        if template.template_type == AWS_MANAGED_POLICY_TEMPLATE_TYPE
    ]:
        # There are other template changes that could rely on the managed policy so create these first
        template_changes.extend(await async_batch_processor(managed_policy_tasks, 40))
        if len(template_changes) > len(managed_policy_tasks):
            # Give a few seconds to allow the managed policies to be created in AWS
            await asyncio.sleep(10)

    if any(
        template.template_type == AWS_IAM_GROUP_TEMPLATE_TYPE for template in templates
    ) and any(
        template.template_type == AWS_IAM_USER_TEMPLATE_TYPE for template in templates
    ):
        # There are user templates that may rely on the group so groups must be created first
        excluded_from_batch.append(AWS_IAM_GROUP_TEMPLATE_TYPE)
        group_tasks = [
            template.apply(config)
            for template in templates
            if template.template_type == AWS_IAM_GROUP_TEMPLATE_TYPE
        ]
        template_changes.extend(await async_batch_processor(group_tasks, 30))
        # Give a few seconds to allow the group to be created in AWS
        await asyncio.sleep(10)

    template_changes.extend(
        await async_batch_processor(
            [
                template.apply(config)
                for template in templates
                if template.template_type not in excluded_from_batch
            ],
            30,
        )
    )
    return template_changes


async def apply(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    templates: list[BaseTemplate],
    remote_worker=None,
) -> list[TemplateChangeDetails]:
    """
    The async_apply_callable for the AWS IambicPlugin class.

    :param exe_message: Execution context
    :param config: The config object.
    :param templates: The list of templates to apply.
    :param remote_worker: The remote worker to use for applying templates.
    """
    # TODO: Leverage exe_message as part of a distributed execution
    # TODO: Leverage remote_worker as part of a distributed execution

    identity_center_templates = []
    iam_templates = []
    tasks = []

    for template in templates:
        if template.template_type == AWS_IDENTITY_CENTER_PERMISSION_SET_TEMPLATE_TYPE:
            identity_center_templates.append(template)
        else:
            iam_templates.append(template)

    if identity_center_templates:
        tasks.append(
            apply_identity_center_templates(
                exe_message, config, identity_center_templates, remote_worker
            )
        )

    if iam_templates:
        tasks.append(
            apply_iam_templates(exe_message, config, iam_templates, remote_worker)
        )

    template_changes = list(chain.from_iterable(await asyncio.gather(*tasks)))

    return [
        template_change
        for template_change in template_changes
        if template_change.proposed_changes or template_change.exceptions_seen
    ]


async def import_service_resources(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    base_output_dir: str,
    service_name: str,
    async_collector_callables: list,
    async_generator_callables: list,
    messages: list = None,
    remote_worker=None,
    existing_template_map: dict = None,
):
    base_runner = bool(not exe_message.metadata)
    if not exe_message.metadata:
        exe_message = exe_message.copy()
        exe_message.metadata = dict(service=service_name)

    for async_collector_callable in async_collector_callables:
        tasks = []

        for account in config.accounts:
            task_message = exe_message.copy()

            if (
                task_message.provider_id
                and task_message.provider_id != account.account_id
            ):
                continue
            elif account.iambic_managed == IambicManaged.DISABLED:
                continue
            elif not task_message.provider_id:
                task_message.provider_id = account.account_id

            tasks.append(
                async_collector_callable(
                    task_message, config, existing_template_map, messages
                )
            )

        if tasks:
            if base_runner and ctx.use_remote and remote_worker and not messages:
                # TODO: Update to use the remote_worker
                await asyncio.gather(*tasks)
                # TODO: Add a process to gather status messages from the remote worker
            else:
                if remote_worker:
                    log.warning(
                        "The remote worker definition must be defined in the config to run remote execution."
                    )
                await asyncio.gather(*tasks)

    if base_runner:
        await asyncio.gather(
            *[
                async_generator_callable(
                    exe_message,
                    config,
                    base_output_dir,
                    existing_template_map,
                    messages,
                )
                for async_generator_callable in async_generator_callables
            ]
        )


async def import_identity_center_resources(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    base_output_dir: str,
    messages: list = None,
    remote_worker=None,
    existing_template_map: dict = None,
):
    identity_center_config = config.copy()
    identity_center_config.accounts = [
        account
        for account in config.accounts
        if account.identity_center_details
        and account.iambic_managed != IambicManaged.DISABLED
    ]
    identity_center_accounts = [
        account.account_id for account in identity_center_config.accounts
    ]
    if not identity_center_accounts:
        return
    elif (
        exe_message.provider_id
        and exe_message.provider_id not in identity_center_accounts
    ):
        return

    await config.set_identity_center_details(exe_message.provider_id)
    await import_service_resources(
        exe_message,
        identity_center_config,
        base_output_dir,
        "identity_center",
        [collect_aws_permission_sets],
        [generate_aws_permission_set_templates],
        messages,
        remote_worker,
        existing_template_map,
    )


async def import_aws_resources(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    base_output_dir: str,
    messages: list = None,
    remote_worker=None,
):
    tasks: list[Coroutine] = []

    if not exe_message.metadata or exe_message.metadata["service"] == "identity_center":
        identity_center_template_map = None
        if not remote_worker or exe_message.metadata:
            identity_center_template_map = await get_existing_template_map(
                repo_dir=base_output_dir,
                template_type="AWS::IdentityCenter.*",
                template_map=config.template_map,
                nested=True,
            )

        tasks.append(
            import_identity_center_resources(
                exe_message,
                config,
                base_output_dir,
                messages,
                remote_worker,
                identity_center_template_map,
            )
        )

    tasks += await import_organization_resources(
        exe_message, config, base_output_dir, messages, remote_worker
    )  # type: ignore

    if not exe_message.metadata or exe_message.metadata["service"] == "iam":
        iam_template_map = None

        if not remote_worker or exe_message.metadata:
            iam_template_map = await get_existing_template_map(
                repo_dir=base_output_dir,
                template_type="AWS::IAM.*",
                template_map=config.template_map,
                nested=True,
            )

        tasks.append(
            import_service_resources(
                exe_message,
                config,
                base_output_dir,
                "iam",
                [
                    collect_aws_roles,
                    collect_aws_users,
                    collect_aws_groups,
                    collect_aws_managed_policies,
                ],
                [
                    generate_aws_role_templates,
                    generate_aws_user_templates,
                    generate_aws_group_templates,
                    generate_aws_managed_policy_templates,
                ],
                messages,
                remote_worker,
                iam_template_map,
            )
        )

    await asyncio.gather(*tasks)


async def import_organization_resources(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    base_output_dir: str,
    messages: list = None,
    remote_worker=None,
) -> list[Coroutine]:
    tasks = []
    if not config.organizations:
        return tasks
    exe_messages = await config.get_command_by_organization_account(exe_message)
    scp_template_map = await get_existing_template_map(
        repo_dir=base_output_dir,
        template_type=AWS_SCP_POLICY_TEMPLATE,
        template_map=config.template_map,
        nested=True,
    )

    for exe_msg in exe_messages:
        aws_account_map: dict[str, AWSAccount] = await get_organizations_account_map(
            exe_msg, config
        )
        aws_account = aws_account_map[exe_msg.provider_id]  # type: ignore
        org_client = await aws_account.get_boto3_client("organizations")

        if not (await service_control_policy_is_enabled(org_client)):
            pass

        # this is also configured at aws config load method
        await aws_account.set_account_organization_details(
            await config.get_organization_from_account(exe_msg.provider_id), config
        )
        tasks.append(
            import_service_resources(
                exe_msg,
                config,
                base_output_dir,
                "scp",
                [collect_aws_scp_policies],
                [generate_aws_scp_policy_templates],
                messages,
                remote_worker,
                scp_template_map,
            )
        )

    return tasks


async def detect_changes(  # noqa: C901
    config: AWSConfig,
    repo_dir: str,
    message_details_file: Optional[str] = None,
) -> Union[str, None]:
    if not config.sqs_cloudtrail_changes_queues:
        log.debug("No cloudtrail changes queue arn found. Returning")
        return

    aws_account_map = await get_aws_account_map(config)
    role_messages = []
    user_messages = []
    group_messages = []
    managed_policy_messages = []
    permission_set_messages = []
    scp_messages = []
    commit_message = "Out of band changes detected.\nSummary:\n"

    for queue_arn in config.sqs_cloudtrail_changes_queues:
        queue_name = queue_arn.split(":")[-1]
        region_name = queue_arn.split(":")[3]
        session = await config.get_boto_session_from_arn(queue_arn, region_name)
        identity = session.client("sts").get_caller_identity()
        identity_arn_with_session_name = (
            identity["Arn"].replace(":sts:", ":iam:").replace("assumed-role", "role")
        )
        # TODO: This only works for same account identities. We need to do similar to NoqMeter,
        # check all roles we have access to on all accounts, or store this in configuration.
        # Then exclude these from the list of roles to check.

        identity_arn = "/".join(identity_arn_with_session_name.split("/")[0:2])
        sqs = session.client("sqs", region_name=region_name)
        queue_url_res = sqs.get_queue_url(QueueName=queue_name)
        queue_url = queue_url_res.get("QueueUrl")
        messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10).get(
            "Messages", []
        )

        detect_log_details = []

        while messages:
            processed_messages = []
            for message in messages:
                try:
                    processed_messages.append(
                        {
                            "Id": message["MessageId"],
                            "ReceiptHandle": message["ReceiptHandle"],
                        }
                    )
                    message_body = json.loads(message["Body"])
                    try:
                        if "Message" in message_body:
                            decoded_message = json.loads(message_body["Message"])[
                                "detail"
                            ]
                        else:
                            decoded_message = message_body["detail"]
                    except Exception as err:
                        log.debug(
                            "Unable to process message", error=str(err), message=message
                        )
                        processed_messages.append(
                            {
                                "Id": message["MessageId"],
                                "ReceiptHandle": message["ReceiptHandle"],
                            }
                        )
                        continue
                    actor = (
                        decoded_message.get("userIdentity", {})
                        .get("sessionContext", {})
                        .get("sessionIssuer", {})
                        .get("arn", "")
                    )
                    session_name = (
                        decoded_message.get("userIdentity", {})
                        .get("principalId")
                        .split(":")[-1]
                    )
                    if actor != identity_arn:
                        account_id = decoded_message.get("recipientAccountId")
                        aws_account = aws_account_map[account_id]
                        request_params = decoded_message["requestParameters"]
                        response_elements = decoded_message["responseElements"]
                        event = decoded_message["eventName"]
                        resource_id = None
                        resource_type = None
                        if role_name := request_params.get("roleName"):
                            resource_id = role_name
                            resource_type = "Role"
                            role_messages.append(
                                RoleMessageDetails(
                                    account_id=account_id,
                                    role_name=templatize_resource(
                                        aws_account, role_name
                                    ),
                                    delete=bool(event == "DeleteRole"),
                                )
                            )
                        elif user_name := request_params.get("userName"):
                            resource_id = user_name
                            resource_type = "User"
                            user_messages.append(
                                UserMessageDetails(
                                    account_id=account_id,
                                    user_name=templatize_resource(
                                        aws_account, user_name
                                    ),
                                    delete=bool(event == "DeleteUser"),
                                )
                            )
                        elif group_name := request_params.get("groupName"):
                            resource_id = group_name
                            resource_type = "Group"
                            group_messages.append(
                                GroupMessageDetails(
                                    account_id=account_id,
                                    group_name=templatize_resource(
                                        aws_account, group_name
                                    ),
                                    delete=bool(event == "DeleteGroup"),
                                )
                            )
                        elif policy_arn := request_params.get("policyArn"):
                            split_policy = policy_arn.split("/")
                            policy_name = split_policy[-1]
                            policy_path = (
                                "/"
                                if len(split_policy) == 2
                                else f"/{'/'.join(split_policy[1:-1])}/"
                            )
                            resource_id = policy_name
                            resource_type = "ManagedPolicy"
                            managed_policy_messages.append(
                                ManagedPolicyMessageDetails(
                                    account_id=account_id,
                                    policy_name=templatize_resource(
                                        aws_account, policy_name
                                    ),
                                    policy_path=templatize_resource(
                                        aws_account, policy_path
                                    ),
                                    delete=bool(
                                        decoded_message["eventName"] == "DeletePolicy"
                                    ),
                                )
                            )
                        elif permission_set_arn := request_params.get(
                            "permissionSetArn"
                        ):
                            resource_id = permission_set_arn
                            resource_type = "PermissionSet"
                            permission_set_messages.append(
                                PermissionSetMessageDetails(
                                    account_id=account_id,
                                    instance_arn=templatize_resource(
                                        aws_account, request_params.get("instanceArn")
                                    ),
                                    permission_set_arn=templatize_resource(
                                        aws_account, permission_set_arn
                                    ),
                                )
                            )
                        elif scp_policy_id := SCPMessageDetails.get_policy_id(
                            request_params,
                            response_elements,
                        ):
                            resource_id = scp_policy_id
                            resource_type = "SCPPolicy"
                            scp_messages.append(
                                SCPMessageDetails(
                                    account_id=account_id,
                                    policy_id=scp_policy_id,
                                    delete=bool(event == "DeletePolicy"),
                                    event=event,
                                )
                            )
                        elif SCPMessageDetails.tag_event(
                            event,
                            decoded_message["eventSource"],
                        ):
                            resource_id = request_params.get("resourceId")
                            resource_type = "SCPPolicy"
                            scp_messages.append(
                                SCPMessageDetails(
                                    account_id=account_id,
                                    policy_id=resource_id,
                                    delete=False,
                                    event=event,
                                )
                            )

                        if resource_id:
                            detect_log_details.append(
                                {
                                    "resource_id": resource_id,
                                    **message_body,
                                }
                            )
                            commit_message = (
                                f"{commit_message}User {session_name} performed action {event} "
                                f"on {resource_type}({resource_id}) on account {account_id}.\n"
                            )
                except Exception as err:
                    log.debug(
                        "Unable to process message", error=str(err), message=message
                    )
                    continue

            sqs.delete_message_batch(QueueUrl=queue_url, Entries=processed_messages)
            messages = sqs.receive_message(
                QueueUrl=queue_url, MaxNumberOfMessages=10
            ).get("Messages", [])

    exe_message = ExecutionMessage(
        execution_id=str(uuid.uuid4()), command=Command.IMPORT, provider_type="aws"
    )
    collect_tasks = []
    iam_template_map = None
    identity_center_template_map = None
    scp_template_map = None

    if (
        role_messages
        or user_messages
        or group_messages
        or managed_policy_messages
        or scp_messages
    ):
        iam_template_map = await get_existing_template_map(
            repo_dir=repo_dir,
            template_type="AWS::IAM.*",
            template_map=config.template_map,
            nested=True,
        )

    if permission_set_messages:
        identity_center_template_map = await get_existing_template_map(
            repo_dir=repo_dir,
            template_type="AWS::IdentityCenter.*",
            template_map=config.template_map,
            nested=True,
        )

    if scp_messages:
        scp_template_map = await get_existing_template_map(
            repo_dir=repo_dir,
            template_type=AWS_SCP_POLICY_TEMPLATE,
            template_map=config.template_map,
            nested=True,
        )

    if role_messages:
        collect_tasks.append(
            collect_aws_roles(exe_message, config, iam_template_map, role_messages)
        )
    if user_messages:
        collect_tasks.append(
            collect_aws_users(exe_message, config, iam_template_map, user_messages)
        )
    if group_messages:
        collect_tasks.append(
            collect_aws_groups(exe_message, config, iam_template_map, group_messages)
        )
    if managed_policy_messages:
        collect_tasks.append(
            collect_aws_managed_policies(
                exe_message, config, iam_template_map, managed_policy_messages
            )
        )
    if permission_set_messages:
        collect_tasks.append(
            collect_aws_permission_sets(
                exe_message,
                config,
                identity_center_template_map,
                permission_set_messages,
            )
        )
    if scp_messages:
        exe_messages = await config.get_command_by_organization_account(exe_message)

        # for each execution message (by organization), collect the SCP policies.
        for message in exe_messages:
            if current_messages := [
                m for m in scp_messages if m.account_id == message.provider_id
            ]:
                collect_tasks.append(
                    collect_aws_scp_policies(
                        message,
                        config,
                        scp_template_map,
                        current_messages,
                    )
                )

    if collect_tasks:
        await asyncio.gather(*collect_tasks)

        tasks = []
        if role_messages:
            tasks.append(
                generate_aws_role_templates(
                    exe_message, config, repo_dir, iam_template_map, role_messages
                )
            )
        if user_messages:
            tasks.append(
                generate_aws_user_templates(
                    exe_message, config, repo_dir, iam_template_map, user_messages
                )
            )
        if group_messages:
            tasks.append(
                generate_aws_group_templates(
                    exe_message, config, repo_dir, iam_template_map, group_messages
                )
            )
        if managed_policy_messages:
            tasks.append(
                generate_aws_managed_policy_templates(
                    exe_message,
                    config,
                    repo_dir,
                    iam_template_map,
                    managed_policy_messages,
                )
            )
        if permission_set_messages:
            tasks.append(
                generate_aws_permission_set_templates(
                    exe_message,
                    config,
                    repo_dir,
                    identity_center_template_map,
                    permission_set_messages,
                )
            )
        if scp_messages:
            exe_messages = await config.get_command_by_organization_account(exe_message)

            # for each execution message (by organization), collect the SCP policies.
            for message in exe_messages:
                if current_messages := [
                    m for m in scp_messages if m.account_id == message.provider_id
                ]:
                    tasks.append(
                        generate_aws_scp_policy_templates(
                            message,
                            config,
                            repo_dir,
                            scp_template_map,
                            current_messages,
                        )
                    )
        await asyncio.gather(*tasks)

        if message_details_file and detect_log_details:
            os.makedirs(os.path.dirname(message_details_file), exist_ok=True)
            with open(message_details_file, "w") as f:
                f.write(json.dumps(detect_log_details, indent=2))
            log.info("Message details written to file", file=message_details_file)

        return commit_message


async def decode_aws_secret(config: AWSConfig, extend: ExtendsConfig) -> dict:
    if extend.key.value != ExtendsConfigKey.AWS_SECRETS_MANAGER.value:
        return {}

    assume_role_arn = extend.assume_role_arn
    secret_arn = extend.value
    region_name = secret_arn.split(":")[3]
    secret_account_id = secret_arn.split(":")[4]
    aws_account_map = {account.account_id: account for account in config.accounts}
    session = None

    if aws_account := aws_account_map.get(secret_account_id):
        if assume_role_arn == aws_account.spoke_role_arn:
            session = await aws_account.get_boto3_session(region_name=region_name)

    if not session and (config.accounts or config.organizations):
        if config.organizations:
            boto3_session = await config.organizations[0].get_boto3_session()
        else:
            hub_account = [
                account for account in config.accounts if account.hub_role_arn
            ][0]
            boto3_session = await hub_account.get_boto3_session()

        secret_account = AWSAccount(
            account_id=secret_account_id,
            account_name="Secret_Account",
            spoke_role_arn=assume_role_arn,
            hub_session_info=dict(boto3_session=boto3_session),
            boto3_session_map={},
        )
        session = await secret_account.get_boto3_session(region_name=region_name)
    elif not session:
        session = boto3.Session(region_name=region_name)

    try:
        client = session.client(service_name="secretsmanager")
        get_secret_value_response = client.get_secret_value(SecretId=secret_arn)
    except Exception:
        log.exception(
            "Unable to retrieve the AWS secret using the provided assume_role_arn",
            assume_role_arn=assume_role_arn,
            secret_arn=extend.value,
        )
        raise

    if "SecretString" in get_secret_value_response:
        return_val = get_secret_value_response["SecretString"]
    else:
        return_val = base64.b64decode(get_secret_value_response["SecretBinary"])

    return yaml.load(return_val)


async def discover_new_aws_accounts(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    config_account_idx_map: dict[str, int],
    orgs_accounts: list[list[AWSAccount]],
    repo_dir: str,
    remote_worker=None,
) -> bool:
    run_import = False
    accounts_to_apply = []
    for org_accounts in orgs_accounts:
        for account in org_accounts:
            if config_account_idx_map.get(account.account_id) is None:
                account.variables.extend(
                    [
                        Variable(key="account_id", value=account.account_id),
                        Variable(key="account_name", value=account.account_name),
                    ]
                )
                config.accounts.append(account)
                log.warning(
                    "New AWS account discovered. Adding account to config.",
                    account_id=account.account_id,
                    account_name=account.account_name,
                )
                if account.iambic_managed not in [
                    IambicManaged.DISABLED,
                    IambicManaged.IMPORT_ONLY,
                ]:
                    accounts_to_apply.append(account)

                if account.iambic_managed != IambicManaged.DISABLED:
                    run_import = True

    if accounts_to_apply:
        log.warning(
            "Applying templates to provision identities to the discovered account(s).",
        )
        templates = await gather_templates(repo_dir, "AWS.*")
        sub_message = exe_message.copy()
        sub_message.command = Command.APPLY
        sub_config = config.copy()
        sub_config.accounts = accounts_to_apply
        await apply(
            exe_message,
            sub_config,
            load_templates(templates, config.template_map),
            remote_worker,
        )

    return run_import


async def discover_aws_account_attribute_changes(
    config: AWSConfig,
    config_account_idx_map: dict[str, int],
    orgs_accounts: list[list[AWSAccount]],
) -> bool:
    run_import = False
    for org_accounts in orgs_accounts:
        for account in org_accounts:
            if (
                account_elem := config_account_idx_map.get(account.account_id)
            ) is not None:
                config_account = config.accounts[account_elem]
                config_account_var_map = {
                    var["key"]: {"elem": idx, "value": var["value"]}
                    for idx, var in enumerate(config_account.variables)
                }

                if config_account.account_name != account.account_name:
                    log.warning(
                        "Updated AWS account name discovered. Updating account in config.",
                        account_id=account.account_id,
                        account_name=account.account_name,
                    )
                    config.accounts[account_elem].account_name = account.account_name
                    if account.iambic_managed != IambicManaged.DISABLED:
                        run_import = True

                for org_account_var in account.variables:
                    if config_account_var := config_account_var_map.get(
                        org_account_var.key
                    ):
                        if config_account_var["value"] != org_account_var.value:
                            log.warning(
                                "Mismatched variable on AWS account. Updating in config.",
                                account_id=account.account_id,
                                account_name=account.account_name,
                                variable_key=org_account_var.key,
                                discovered_value=org_account_var.value,
                                config_value=config_account_var["value"],
                            )
                            config.accounts[account_elem].variables[
                                config_account_var["elem"]
                            ].value = org_account_var.value
                            if account.iambic_managed != IambicManaged.DISABLED:
                                run_import = True

    return run_import


async def aws_account_update_and_discovery(
    exe_message: ExecutionMessage,
    config: AWSConfig,
    repo_dir: str,
    remote_worker=None,
):
    """
    Update and discover AWS accounts.

    This function updates the list of AWS accounts in the `config` object by retrieving the list of accounts
    from the AWS Organizations and checking for any new or updated accounts. If any new or updated accounts
    are found, the function imports the AWS resources and regenerates the AWS templates.

    Args:
    - config (AWSConfig): The AWS configuration object.
    - repo_dir (str): The directory path for the repository.

    Returns:
    - None
    """
    # TODO: Leverage exe_message as part of a distributed execution
    # TODO: Leverage remote_worker as part of a distributed execution

    if not config.organizations:
        return

    ctx.eval_only = False
    config_account_idx_map = {
        account.account_id: idx for idx, account in enumerate(config.accounts)
    }

    orgs_accounts = await asyncio.gather(
        *[org.get_accounts() for org in config.organizations]
    )
    import_new_account = await discover_new_aws_accounts(
        exe_message,
        config,
        config_account_idx_map,
        orgs_accounts,
        repo_dir,
        remote_worker,
    )
    import_updated_account = await discover_aws_account_attribute_changes(
        config, config_account_idx_map, orgs_accounts
    )
    if import_new_account or import_updated_account:
        log.warning(
            "Running import to regenerate AWS templates.",
        )
        sub_message = exe_message.copy()
        sub_message.command = Command.IMPORT
        await import_aws_resources(sub_message, config, repo_dir, remote_worker)
