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

__all__ = ['Spoke']


class Spoke(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hub: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 linked_interconnect_attachments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 linked_router_appliance_instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouterApplianceInstanceArgs']]]]] = None,
                 linked_vpn_tunnels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 spokes_id: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new Spoke in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The time when the Spoke was created.
        :param pulumi.Input[str] description: Short description of the spoke resource
        :param pulumi.Input[str] hub: The resource URL of the hub resource that the spoke is attached to
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-defined labels.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] linked_interconnect_attachments: The URIs of linked interconnect attachment resources
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouterApplianceInstanceArgs']]]] linked_router_appliance_instances: The URIs of linked Router appliance resources
        :param pulumi.Input[Sequence[pulumi.Input[str]]] linked_vpn_tunnels: The URIs of linked VPN tunnel resources
        :param pulumi.Input[str] name: Immutable. The name of a Spoke resource.
        :param pulumi.Input[str] update_time: The time when the Spoke was updated.
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

            __props__['create_time'] = create_time
            __props__['description'] = description
            __props__['hub'] = hub
            __props__['labels'] = labels
            __props__['linked_interconnect_attachments'] = linked_interconnect_attachments
            __props__['linked_router_appliance_instances'] = linked_router_appliance_instances
            __props__['linked_vpn_tunnels'] = linked_vpn_tunnels
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            if spokes_id is None and not opts.urn:
                raise TypeError("Missing required property 'spokes_id'")
            __props__['spokes_id'] = spokes_id
            __props__['update_time'] = update_time
            __props__['state'] = None
            __props__['unique_id'] = None
        super(Spoke, __self__).__init__(
            'gcp-native:networkconnectivity/v1alpha1:Spoke',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Spoke':
        """
        Get an existing Spoke resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = None
        __props__["description"] = None
        __props__["hub"] = None
        __props__["labels"] = None
        __props__["linked_interconnect_attachments"] = None
        __props__["linked_router_appliance_instances"] = None
        __props__["linked_vpn_tunnels"] = None
        __props__["name"] = None
        __props__["state"] = None
        __props__["unique_id"] = None
        __props__["update_time"] = None
        return Spoke(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the Spoke was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Short description of the spoke resource
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hub(self) -> pulumi.Output[str]:
        """
        The resource URL of the hub resource that the spoke is attached to
        """
        return pulumi.get(self, "hub")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        User-defined labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="linkedInterconnectAttachments")
    def linked_interconnect_attachments(self) -> pulumi.Output[Sequence[str]]:
        """
        The URIs of linked interconnect attachment resources
        """
        return pulumi.get(self, "linked_interconnect_attachments")

    @property
    @pulumi.getter(name="linkedRouterApplianceInstances")
    def linked_router_appliance_instances(self) -> pulumi.Output[Sequence['outputs.RouterApplianceInstanceResponse']]:
        """
        The URIs of linked Router appliance resources
        """
        return pulumi.get(self, "linked_router_appliance_instances")

    @property
    @pulumi.getter(name="linkedVpnTunnels")
    def linked_vpn_tunnels(self) -> pulumi.Output[Sequence[str]]:
        """
        The URIs of linked VPN tunnel resources
        """
        return pulumi.get(self, "linked_vpn_tunnels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The name of a Spoke resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of this Hub.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        Google-generated UUID for this resource. This is unique across all Spoke resources. If a Spoke resource is deleted and another with the same name is created, it gets a different unique_id.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the Spoke was updated.
        """
        return pulumi.get(self, "update_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

