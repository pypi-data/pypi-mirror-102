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

__all__ = ['RegionNetworkEndpointGroup']


class RegionNetworkEndpointGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 app_engine: Optional[pulumi.Input[pulumi.InputType['NetworkEndpointGroupAppEngineArgs']]] = None,
                 cloud_function: Optional[pulumi.Input[pulumi.InputType['NetworkEndpointGroupCloudFunctionArgs']]] = None,
                 cloud_run: Optional[pulumi.Input[pulumi.InputType['NetworkEndpointGroupCloudRunArgs']]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 default_port: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 load_balancer: Optional[pulumi.Input[pulumi.InputType['NetworkEndpointGroupLbNetworkEndpointGroupArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 network_endpoint_group: Optional[pulumi.Input[str]] = None,
                 network_endpoint_type: Optional[pulumi.Input[str]] = None,
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
        Creates a network endpoint group in the specified project using the parameters that are included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Metadata defined as annotations on the network endpoint group.
        :param pulumi.Input[pulumi.InputType['NetworkEndpointGroupAppEngineArgs']] app_engine: Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
        :param pulumi.Input[pulumi.InputType['NetworkEndpointGroupCloudFunctionArgs']] cloud_function: Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
        :param pulumi.Input[pulumi.InputType['NetworkEndpointGroupCloudRunArgs']] cloud_run: Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[int] default_port: The default port used if the port number is not specified in the network endpoint.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output Only] Type of the resource. Always compute#networkEndpointGroup for network endpoint group.
        :param pulumi.Input[pulumi.InputType['NetworkEndpointGroupLbNetworkEndpointGroupArgs']] load_balancer: This field is only valid when the network endpoint group is used for load balancing. [Deprecated] This field is deprecated.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] network: The URL of the network to which all network endpoints in the NEG belong. Uses "default" project network if unspecified.
        :param pulumi.Input[str] network_endpoint_type: Type of network endpoints in this network endpoint group. Can be one of GCE_VM_IP_PORT, NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT, INTERNET_IP_PORT, or SERVERLESS.
        :param pulumi.Input[str] region: [Output Only] The URL of the region where the network endpoint group is located.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[int] size: [Output only] Number of network endpoints in the network endpoint group.
        :param pulumi.Input[str] subnetwork: Optional URL of the subnetwork to which all network endpoints in the NEG belong.
        :param pulumi.Input[str] zone: [Output Only] The URL of the zone where the network endpoint group is located.
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

            __props__['annotations'] = annotations
            __props__['app_engine'] = app_engine
            __props__['cloud_function'] = cloud_function
            __props__['cloud_run'] = cloud_run
            __props__['creation_timestamp'] = creation_timestamp
            __props__['default_port'] = default_port
            __props__['description'] = description
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['load_balancer'] = load_balancer
            __props__['name'] = name
            __props__['network'] = network
            if network_endpoint_group is None and not opts.urn:
                raise TypeError("Missing required property 'network_endpoint_group'")
            __props__['network_endpoint_group'] = network_endpoint_group
            __props__['network_endpoint_type'] = network_endpoint_type
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            __props__['self_link'] = self_link
            __props__['size'] = size
            __props__['subnetwork'] = subnetwork
            __props__['zone'] = zone
        super(RegionNetworkEndpointGroup, __self__).__init__(
            'gcp-native:compute/beta:RegionNetworkEndpointGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegionNetworkEndpointGroup':
        """
        Get an existing RegionNetworkEndpointGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["annotations"] = None
        __props__["app_engine"] = None
        __props__["cloud_function"] = None
        __props__["cloud_run"] = None
        __props__["creation_timestamp"] = None
        __props__["default_port"] = None
        __props__["description"] = None
        __props__["kind"] = None
        __props__["load_balancer"] = None
        __props__["name"] = None
        __props__["network"] = None
        __props__["network_endpoint_type"] = None
        __props__["region"] = None
        __props__["self_link"] = None
        __props__["size"] = None
        __props__["subnetwork"] = None
        __props__["zone"] = None
        return RegionNetworkEndpointGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Metadata defined as annotations on the network endpoint group.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="appEngine")
    def app_engine(self) -> pulumi.Output['outputs.NetworkEndpointGroupAppEngineResponse']:
        """
        Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
        """
        return pulumi.get(self, "app_engine")

    @property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(self) -> pulumi.Output['outputs.NetworkEndpointGroupCloudFunctionResponse']:
        """
        Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
        """
        return pulumi.get(self, "cloud_function")

    @property
    @pulumi.getter(name="cloudRun")
    def cloud_run(self) -> pulumi.Output['outputs.NetworkEndpointGroupCloudRunResponse']:
        """
        Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
        """
        return pulumi.get(self, "cloud_run")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        [Output Only] Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="defaultPort")
    def default_port(self) -> pulumi.Output[int]:
        """
        The default port used if the port number is not specified in the network endpoint.
        """
        return pulumi.get(self, "default_port")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] Type of the resource. Always compute#networkEndpointGroup for network endpoint group.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output['outputs.NetworkEndpointGroupLbNetworkEndpointGroupResponse']:
        """
        This field is only valid when the network endpoint group is used for load balancing. [Deprecated] This field is deprecated.
        """
        return pulumi.get(self, "load_balancer")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        The URL of the network to which all network endpoints in the NEG belong. Uses "default" project network if unspecified.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> pulumi.Output[str]:
        """
        Type of network endpoints in this network endpoint group. Can be one of GCE_VM_IP_PORT, NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT, INTERNET_IP_PORT, or SERVERLESS.
        """
        return pulumi.get(self, "network_endpoint_type")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL of the region where the network endpoint group is located.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        [Output only] Number of network endpoints in the network endpoint group.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Output[str]:
        """
        Optional URL of the subnetwork to which all network endpoints in the NEG belong.
        """
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        [Output Only] The URL of the zone where the network endpoint group is located.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

