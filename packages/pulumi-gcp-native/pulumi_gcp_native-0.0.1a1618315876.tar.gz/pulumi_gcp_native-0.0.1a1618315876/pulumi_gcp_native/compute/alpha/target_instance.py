# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['TargetInstance']


class TargetInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_policy: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 self_link_with_id: Optional[pulumi.Input[str]] = None,
                 target_instance: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a TargetInstance resource in the specified project and zone using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] instance: A URL to the virtual machine instance that handles traffic for this target instance. When creating a target instance, you can provide the fully-qualified URL or a valid partial URL to the desired virtual machine. For example, the following are all valid URLs: 
               - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance 
               - projects/project/zones/zone/instances/instance 
               - zones/zone/instances/instance
        :param pulumi.Input[str] kind: [Output Only] The type of the resource. Always compute#targetInstance for target instances.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] nat_policy: NAT option controlling how IPs are NAT'ed to the instance. Currently only NO_NAT (default value) is supported.
        :param pulumi.Input[str] network: The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to the network that the default network interface belongs to.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[str] self_link_with_id: [Output Only] Server-defined URL for this resource with the resource id.
        :param pulumi.Input[str] zone: [Output Only] URL of the zone where the target instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
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
            __props__['id'] = id
            __props__['instance'] = instance
            __props__['kind'] = kind
            __props__['name'] = name
            __props__['nat_policy'] = nat_policy
            __props__['network'] = network
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['self_link'] = self_link
            __props__['self_link_with_id'] = self_link_with_id
            if target_instance is None and not opts.urn:
                raise TypeError("Missing required property 'target_instance'")
            __props__['target_instance'] = target_instance
            if zone is None and not opts.urn:
                raise TypeError("Missing required property 'zone'")
            __props__['zone'] = zone
        super(TargetInstance, __self__).__init__(
            'gcp-native:compute/alpha:TargetInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TargetInstance':
        """
        Get an existing TargetInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["instance"] = None
        __props__["kind"] = None
        __props__["name"] = None
        __props__["nat_policy"] = None
        __props__["network"] = None
        __props__["self_link"] = None
        __props__["self_link_with_id"] = None
        __props__["zone"] = None
        return TargetInstance(resource_name, opts=opts, __props__=__props__)

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
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[str]:
        """
        A URL to the virtual machine instance that handles traffic for this target instance. When creating a target instance, you can provide the fully-qualified URL or a valid partial URL to the desired virtual machine. For example, the following are all valid URLs: 
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance 
        - projects/project/zones/zone/instances/instance 
        - zones/zone/instances/instance
        """
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] The type of the resource. Always compute#targetInstance for target instances.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natPolicy")
    def nat_policy(self) -> pulumi.Output[str]:
        """
        NAT option controlling how IPs are NAT'ed to the instance. Currently only NO_NAT (default value) is supported.
        """
        return pulumi.get(self, "nat_policy")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to the network that the default network interface belongs to.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        [Output Only] URL of the zone where the target instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

