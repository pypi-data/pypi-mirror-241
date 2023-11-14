# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220518

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('access_governance_cp.access_governance_cp_root_group.command_name', 'access-governance-cp'), cls=CommandGroupWithAlias, help=cli_util.override('access_governance_cp.access_governance_cp_root_group.help', """Use the Oracle Access Governance API to create, view, and manage GovernanceInstances."""), short_help=cli_util.override('access_governance_cp.access_governance_cp_root_group.short_help', """Access Governance APIs"""))
@cli_util.help_option_group
def access_governance_cp_root_group():
    pass


@click.command(cli_util.override('access_governance_cp.governance_instance_collection_group.command_name', 'governance-instance-collection'), cls=CommandGroupWithAlias, help="""Results of a GovernanceInstance search.""")
@cli_util.help_option_group
def governance_instance_collection_group():
    pass


@click.command(cli_util.override('access_governance_cp.governance_instance_configuration_group.command_name', 'governance-instance-configuration'), cls=CommandGroupWithAlias, help="""The tenancy-wide configuration for GovernanceInstances.""")
@cli_util.help_option_group
def governance_instance_configuration_group():
    pass


@click.command(cli_util.override('access_governance_cp.governance_instance_group.command_name', 'governance-instance'), cls=CommandGroupWithAlias, help="""The details of a GovenanceInstance.""")
@cli_util.help_option_group
def governance_instance_group():
    pass


access_governance_cp_root_group.add_command(governance_instance_collection_group)
access_governance_cp_root_group.add_command(governance_instance_configuration_group)
access_governance_cp_root_group.add_command(governance_instance_group)


@governance_instance_group.command(name=cli_util.override('access_governance_cp.change_governance_instance_compartment.command_name', 'change-compartment'), help=u"""Moves a GovernanceInstance resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeGovernanceInstanceCompartment)""")
@cli_util.option('--governance-instance-id', required=True, help=u"""The OCID of the GovernanceInstance""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the GovernanceInstance resides.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_governance_instance_compartment(ctx, from_json, governance_instance_id, compartment_id, if_match):

    if isinstance(governance_instance_id, six.string_types) and len(governance_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    result = client.change_governance_instance_compartment(
        governance_instance_id=governance_instance_id,
        change_governance_instance_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@governance_instance_group.command(name=cli_util.override('access_governance_cp.create_governance_instance.command_name', 'create'), help=u"""Creates a new GovernanceInstance. \n[Command Reference](createGovernanceInstance)""")
@cli_util.option('--display-name', required=True, help=u"""The name for the GovernanceInstance.""")
@cli_util.option('--license-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["NEW_LICENSE", "BRING_YOUR_OWN_LICENSE", "AG_ORACLE_WORKLOADS", "AG_OCI"]), help=u"""The licenseType being used.""")
@cli_util.option('--tenancy-namespace', required=True, help=u"""The namespace for tenancy object storage.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the GovernanceInstance resides.""")
@cli_util.option('--idcs-access-token', required=True, help=u"""IDCS access token identifying a stripe and service administrator user.""")
@cli_util.option('--description', help=u"""The description of the GovernanceInstance.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'access_governance_cp', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'access_governance_cp', 'class': 'dict(str, string)'}, 'system-tags': {'module': 'access_governance_cp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'access_governance_cp', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'access_governance_cp', 'class': 'dict(str, string)'}, 'system-tags': {'module': 'access_governance_cp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'access_governance_cp', 'class': 'GovernanceInstance'})
@cli_util.wrap_exceptions
def create_governance_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, license_type, tenancy_namespace, compartment_id, idcs_access_token, description, defined_tags, freeform_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['licenseType'] = license_type
    _details['tenancyNamespace'] = tenancy_namespace
    _details['compartmentId'] = compartment_id
    _details['idcsAccessToken'] = idcs_access_token

    if description is not None:
        _details['description'] = description

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    result = client.create_governance_instance(
        create_governance_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_governance_instance') and callable(getattr(client, 'get_governance_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_governance_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@governance_instance_group.command(name=cli_util.override('access_governance_cp.delete_governance_instance.command_name', 'delete'), help=u"""Deletes an existing GovernanceInstance. \n[Command Reference](deleteGovernanceInstance)""")
@cli_util.option('--governance-instance-id', required=True, help=u"""The OCID of the GovernanceInstance""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_governance_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_instance_id, if_match):

    if isinstance(governance_instance_id, six.string_types) and len(governance_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    result = client.delete_governance_instance(
        governance_instance_id=governance_instance_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_governance_instance') and callable(getattr(client, 'get_governance_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_governance_instance(governance_instance_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@governance_instance_group.command(name=cli_util.override('access_governance_cp.get_governance_instance.command_name', 'get'), help=u"""Gets a GovernanceInstance by OCID. \n[Command Reference](getGovernanceInstance)""")
@cli_util.option('--governance-instance-id', required=True, help=u"""The OCID of the GovernanceInstance""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'access_governance_cp', 'class': 'GovernanceInstance'})
@cli_util.wrap_exceptions
def get_governance_instance(ctx, from_json, governance_instance_id):

    if isinstance(governance_instance_id, six.string_types) and len(governance_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    result = client.get_governance_instance(
        governance_instance_id=governance_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@governance_instance_configuration_group.command(name=cli_util.override('access_governance_cp.get_governance_instance_configuration.command_name', 'get'), help=u"""Gets the tenancy-wide configuration for GovernanceInstances \n[Command Reference](getGovernanceInstanceConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which resources are listed.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'access_governance_cp', 'class': 'GovernanceInstanceConfiguration'})
@cli_util.wrap_exceptions
def get_governance_instance_configuration(ctx, from_json, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    result = client.get_governance_instance_configuration(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@governance_instance_collection_group.command(name=cli_util.override('access_governance_cp.list_governance_instances.command_name', 'list-governance-instances'), help=u"""Returns a list of Governance Instances. \n[Command Reference](listGovernanceInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which resources are listed.""")
@cli_util.option('--lifecycle-state', help=u"""The lifecycle state to filter on.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""The OCID of the GovernanceInstance""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "timeUpdated", "lifecycleState"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'access_governance_cp', 'class': 'GovernanceInstanceCollection'})
@cli_util.wrap_exceptions
def list_governance_instances(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_governance_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_governance_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_governance_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@governance_instance_group.command(name=cli_util.override('access_governance_cp.update_governance_instance.command_name', 'update'), help=u"""Updates the GovernanceInstance. \n[Command Reference](updateGovernanceInstance)""")
@cli_util.option('--governance-instance-id', required=True, help=u"""The OCID of the GovernanceInstance""")
@cli_util.option('--display-name', help=u"""The name for the GovernanceInstance.""")
@cli_util.option('--description', help=u"""The description of the GovernanceInstance.""")
@cli_util.option('--license-type', type=custom_types.CliCaseInsensitiveChoice(["NEW_LICENSE", "BRING_YOUR_OWN_LICENSE", "AG_ORACLE_WORKLOADS", "AG_OCI"]), help=u"""The licenseType being used.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'access_governance_cp', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'access_governance_cp', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'access_governance_cp', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'access_governance_cp', 'class': 'dict(str, string)'}}, output_type={'module': 'access_governance_cp', 'class': 'GovernanceInstance'})
@cli_util.wrap_exceptions
def update_governance_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_instance_id, display_name, description, license_type, defined_tags, freeform_tags, if_match):

    if isinstance(governance_instance_id, six.string_types) and len(governance_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-instance-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if license_type is not None:
        _details['licenseType'] = license_type

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    result = client.update_governance_instance(
        governance_instance_id=governance_instance_id,
        update_governance_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_governance_instance') and callable(getattr(client, 'get_governance_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_governance_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@governance_instance_group.command(name=cli_util.override('access_governance_cp.update_governance_instance_configuration.command_name', 'update-governance-instance-configuration'), help=u"""Updates the tenancy-wide configuration for GovernanceInstances \n[Command Reference](updateGovernanceInstanceConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which resources are listed.""")
@cli_util.option('--sender-info', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'sender-info': {'module': 'access_governance_cp', 'class': 'UpdateSenderConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sender-info': {'module': 'access_governance_cp', 'class': 'UpdateSenderConfig'}}, output_type={'module': 'access_governance_cp', 'class': 'GovernanceInstanceConfiguration'})
@cli_util.wrap_exceptions
def update_governance_instance_configuration(ctx, from_json, force, compartment_id, sender_info, if_match):
    if not force:
        if sender_info:
            if not click.confirm("WARNING: Updates to sender-info will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if sender_info is not None:
        _details['senderInfo'] = cli_util.parse_json_parameter("sender_info", sender_info)

    client = cli_util.build_client('access_governance_cp', 'access_governance_cp', ctx)
    result = client.update_governance_instance_configuration(
        compartment_id=compartment_id,
        update_governance_instance_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
