# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['AgentSessionEntityType']


class AgentSessionEntityType(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agents_id: Optional[pulumi.Input[str]] = None,
                 entities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]]] = None,
                 entity_override_mode: Optional[pulumi.Input[str]] = None,
                 entity_types_id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 sessions_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a session entity type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]] entities: Required. The collection of entities to override or supplement the custom entity type.
        :param pulumi.Input[str] entity_override_mode: Required. Indicates whether the additional data should override or supplement the custom entity type definition.
        :param pulumi.Input[str] name: Required. The unique identifier of the session entity type. Format: `projects//locations//agents//sessions//entityTypes/` or `projects//locations//agents//environments//sessions//entityTypes/`. If `Environment ID` is not specified, we assume default 'draft' environment.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if agents_id is None and not opts.urn:
                raise TypeError("Missing required property 'agents_id'")
            __props__['agents_id'] = agents_id
            __props__['entities'] = entities
            __props__['entity_override_mode'] = entity_override_mode
            if entity_types_id is None and not opts.urn:
                raise TypeError("Missing required property 'entity_types_id'")
            __props__['entity_types_id'] = entity_types_id
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            if sessions_id is None and not opts.urn:
                raise TypeError("Missing required property 'sessions_id'")
            __props__['sessions_id'] = sessions_id
        super(AgentSessionEntityType, __self__).__init__(
            'gcp-native:dialogflow/v3beta1:AgentSessionEntityType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AgentSessionEntityType':
        """
        Get an existing AgentSessionEntityType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["entities"] = None
        __props__["entity_override_mode"] = None
        __props__["name"] = None
        return AgentSessionEntityType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def entities(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowCxV3beta1EntityTypeEntityResponse']]:
        """
        Required. The collection of entities to override or supplement the custom entity type.
        """
        return pulumi.get(self, "entities")

    @property
    @pulumi.getter(name="entityOverrideMode")
    def entity_override_mode(self) -> pulumi.Output[str]:
        """
        Required. Indicates whether the additional data should override or supplement the custom entity type definition.
        """
        return pulumi.get(self, "entity_override_mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The unique identifier of the session entity type. Format: `projects//locations//agents//sessions//entityTypes/` or `projects//locations//agents//environments//sessions//entityTypes/`. If `Environment ID` is not specified, we assume default 'draft' environment.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

