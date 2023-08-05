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

__all__ = ['InstanceGroup']


class InstanceGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 instance_group: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 named_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NamedPortArgs']]]]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 subnetwork: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an instance group in the specified project using the parameters that are included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_timestamp: [Output Only] The creation timestamp for this instance group in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] fingerprint: [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.
        :param pulumi.Input[str] id: [Output Only] A unique identifier for this instance group, generated by the server.
        :param pulumi.Input[str] kind: [Output Only] The resource type, which is always compute#instanceGroup for instance groups.
        :param pulumi.Input[str] name: The name of the instance group. The name must be 1-63 characters long, and comply with RFC1035.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NamedPortArgs']]]] named_ports: Assigns a name to a port number. For example: {name: "http", port: 80}
               
               This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example: [{name: "http", port: 80},{name: "http", port: 8080}] 
               
               Named ports apply to all instances in this instance group.
        :param pulumi.Input[str] network: [Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).
        :param pulumi.Input[str] region: [Output Only] The URL of the region where the instance group is located (for regional resources).
        :param pulumi.Input[str] self_link: [Output Only] The URL for this instance group. The server generates this URL.
        :param pulumi.Input[int] size: [Output Only] The total number of instances in the instance group.
        :param pulumi.Input[str] subnetwork: [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).
        :param pulumi.Input[str] zone: [Output Only] The URL of the zone where the instance group is located (for zonal resources).
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

            __props__['creation_timestamp'] = creation_timestamp
            __props__['description'] = description
            __props__['fingerprint'] = fingerprint
            __props__['id'] = id
            if instance_group is None and not opts.urn:
                raise TypeError("Missing required property 'instance_group'")
            __props__['instance_group'] = instance_group
            __props__['kind'] = kind
            __props__['name'] = name
            __props__['named_ports'] = named_ports
            __props__['network'] = network
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['region'] = region
            __props__['self_link'] = self_link
            __props__['size'] = size
            __props__['subnetwork'] = subnetwork
            if zone is None and not opts.urn:
                raise TypeError("Missing required property 'zone'")
            __props__['zone'] = zone
        super(InstanceGroup, __self__).__init__(
            'gcp-native:compute/v1:InstanceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstanceGroup':
        """
        Get an existing InstanceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["fingerprint"] = None
        __props__["kind"] = None
        __props__["name"] = None
        __props__["named_ports"] = None
        __props__["network"] = None
        __props__["region"] = None
        __props__["self_link"] = None
        __props__["size"] = None
        __props__["subnetwork"] = None
        __props__["zone"] = None
        return InstanceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        [Output Only] The creation timestamp for this instance group in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] The resource type, which is always compute#instanceGroup for instance groups.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the instance group. The name must be 1-63 characters long, and comply with RFC1035.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namedPorts")
    def named_ports(self) -> pulumi.Output[Sequence['outputs.NamedPortResponse']]:
        """
        Assigns a name to a port number. For example: {name: "http", port: 80}

        This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example: [{name: "http", port: 80},{name: "http", port: 8080}] 

        Named ports apply to all instances in this instance group.
        """
        return pulumi.get(self, "named_ports")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL of the region where the instance group is located (for regional resources).
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL for this instance group. The server generates this URL.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        [Output Only] The total number of instances in the instance group.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).
        """
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL of the zone where the instance group is located (for zonal resources).
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

