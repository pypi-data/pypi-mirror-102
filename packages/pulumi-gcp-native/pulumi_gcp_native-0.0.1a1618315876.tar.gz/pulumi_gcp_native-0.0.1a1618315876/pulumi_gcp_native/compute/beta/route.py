# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['Route']


class Route(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dest_range: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 next_hop_gateway: Optional[pulumi.Input[str]] = None,
                 next_hop_ilb: Optional[pulumi.Input[str]] = None,
                 next_hop_instance: Optional[pulumi.Input[str]] = None,
                 next_hop_interconnect_attachment: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 next_hop_network: Optional[pulumi.Input[str]] = None,
                 next_hop_peering: Optional[pulumi.Input[str]] = None,
                 next_hop_vpn_tunnel: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 route: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 warnings: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a Route resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this field when you create the resource.
        :param pulumi.Input[str] dest_range: The destination range of outgoing packets that this route applies to. Both IPv4 and IPv6 are supported.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output Only] Type of this resource. Always compute#routes for Route resources.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.
        :param pulumi.Input[str] network: Fully-qualified URL of the network that this route applies to.
        :param pulumi.Input[str] next_hop_gateway: The URL to a gateway that should handle matching packets. You can only specify the internet gateway using a full or partial valid URL:  projects/project/global/gateways/default-internet-gateway
        :param pulumi.Input[str] next_hop_ilb: The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets or the IP address of the forwarding Rule. For example, the following are all valid URLs:  
               - 10.128.0.56 
               - https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule 
               - regions/region/forwardingRules/forwardingRule
        :param pulumi.Input[str] next_hop_instance: The URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example:
               https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/
        :param pulumi.Input[str] next_hop_interconnect_attachment: [Output Only] The URL to an InterconnectAttachment which is the next hop for the route. This field will only be populated for the dynamic routes generated by Cloud Router with a linked interconnectAttachment.
        :param pulumi.Input[str] next_hop_ip: The network IP address of an instance that should handle matching packets. Only IPv4 is supported.
        :param pulumi.Input[str] next_hop_network: The URL of the local network if it should handle matching packets.
        :param pulumi.Input[str] next_hop_peering: [Output Only] The network peering name that should handle matching packets, which should conform to RFC1035.
        :param pulumi.Input[str] next_hop_vpn_tunnel: The URL to a VpnTunnel that should handle matching packets.
        :param pulumi.Input[int] priority: The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In cases where multiple routes have equal prefix length, the one with the lowest-numbered priority value wins. The default value is `1000`. The priority value must be from `0` to `65535`, inclusive.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined fully-qualified URL for this resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of instance tags to which this route applies.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] warnings: [Output Only] If potential misconfigurations are detected for this route, this field will be populated with warning messages.
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
            __props__['dest_range'] = dest_range
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['name'] = name
            __props__['network'] = network
            __props__['next_hop_gateway'] = next_hop_gateway
            __props__['next_hop_ilb'] = next_hop_ilb
            __props__['next_hop_instance'] = next_hop_instance
            __props__['next_hop_interconnect_attachment'] = next_hop_interconnect_attachment
            __props__['next_hop_ip'] = next_hop_ip
            __props__['next_hop_network'] = next_hop_network
            __props__['next_hop_peering'] = next_hop_peering
            __props__['next_hop_vpn_tunnel'] = next_hop_vpn_tunnel
            __props__['priority'] = priority
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            if route is None and not opts.urn:
                raise TypeError("Missing required property 'route'")
            __props__['route'] = route
            __props__['self_link'] = self_link
            __props__['tags'] = tags
            __props__['warnings'] = warnings
        super(Route, __self__).__init__(
            'gcp-native:compute/beta:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["dest_range"] = None
        __props__["kind"] = None
        __props__["name"] = None
        __props__["network"] = None
        __props__["next_hop_gateway"] = None
        __props__["next_hop_ilb"] = None
        __props__["next_hop_instance"] = None
        __props__["next_hop_interconnect_attachment"] = None
        __props__["next_hop_ip"] = None
        __props__["next_hop_network"] = None
        __props__["next_hop_peering"] = None
        __props__["next_hop_vpn_tunnel"] = None
        __props__["priority"] = None
        __props__["self_link"] = None
        __props__["tags"] = None
        __props__["warnings"] = None
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        [Output Only] Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this field when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> pulumi.Output[str]:
        """
        The destination range of outgoing packets that this route applies to. Both IPv4 and IPv6 are supported.
        """
        return pulumi.get(self, "dest_range")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] Type of this resource. Always compute#routes for Route resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        Fully-qualified URL of the network that this route applies to.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="nextHopGateway")
    def next_hop_gateway(self) -> pulumi.Output[str]:
        """
        The URL to a gateway that should handle matching packets. You can only specify the internet gateway using a full or partial valid URL:  projects/project/global/gateways/default-internet-gateway
        """
        return pulumi.get(self, "next_hop_gateway")

    @property
    @pulumi.getter(name="nextHopIlb")
    def next_hop_ilb(self) -> pulumi.Output[str]:
        """
        The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets or the IP address of the forwarding Rule. For example, the following are all valid URLs:  
        - 10.128.0.56 
        - https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule 
        - regions/region/forwardingRules/forwardingRule
        """
        return pulumi.get(self, "next_hop_ilb")

    @property
    @pulumi.getter(name="nextHopInstance")
    def next_hop_instance(self) -> pulumi.Output[str]:
        """
        The URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example:
        https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/
        """
        return pulumi.get(self, "next_hop_instance")

    @property
    @pulumi.getter(name="nextHopInterconnectAttachment")
    def next_hop_interconnect_attachment(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL to an InterconnectAttachment which is the next hop for the route. This field will only be populated for the dynamic routes generated by Cloud Router with a linked interconnectAttachment.
        """
        return pulumi.get(self, "next_hop_interconnect_attachment")

    @property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> pulumi.Output[str]:
        """
        The network IP address of an instance that should handle matching packets. Only IPv4 is supported.
        """
        return pulumi.get(self, "next_hop_ip")

    @property
    @pulumi.getter(name="nextHopNetwork")
    def next_hop_network(self) -> pulumi.Output[str]:
        """
        The URL of the local network if it should handle matching packets.
        """
        return pulumi.get(self, "next_hop_network")

    @property
    @pulumi.getter(name="nextHopPeering")
    def next_hop_peering(self) -> pulumi.Output[str]:
        """
        [Output Only] The network peering name that should handle matching packets, which should conform to RFC1035.
        """
        return pulumi.get(self, "next_hop_peering")

    @property
    @pulumi.getter(name="nextHopVpnTunnel")
    def next_hop_vpn_tunnel(self) -> pulumi.Output[str]:
        """
        The URL to a VpnTunnel that should handle matching packets.
        """
        return pulumi.get(self, "next_hop_vpn_tunnel")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In cases where multiple routes have equal prefix length, the one with the lowest-numbered priority value wins. The default value is `1000`. The priority value must be from `0` to `65535`, inclusive.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined fully-qualified URL for this resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of instance tags to which this route applies.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def warnings(self) -> pulumi.Output[Sequence[Mapping[str, str]]]:
        """
        [Output Only] If potential misconfigurations are detected for this route, this field will be populated with warning messages.
        """
        return pulumi.get(self, "warnings")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

