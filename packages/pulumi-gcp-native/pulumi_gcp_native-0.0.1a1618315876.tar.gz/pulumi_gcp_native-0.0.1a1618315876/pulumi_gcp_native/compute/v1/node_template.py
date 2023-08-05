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

__all__ = ['NodeTemplate']


class NodeTemplate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AcceleratorConfigArgs']]]]] = None,
                 cpu_overcommit_type: Optional[pulumi.Input[str]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalDiskArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_template: Optional[pulumi.Input[str]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 node_type_flexibility: Optional[pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 server_binding: Optional[pulumi.Input[pulumi.InputType['ServerBindingArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 status_message: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a NodeTemplate resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cpu_overcommit_type: CPU overcommit.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output Only] The type of the resource. Always compute#nodeTemplate for node templates.
        :param pulumi.Input[str] name: The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_affinity_labels: Labels to use for node affinity, which will be used in instance scheduling.
        :param pulumi.Input[str] node_type: The node type to use for nodes group that are created from this template.
        :param pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']] node_type_flexibility: The flexible properties of the desired node type. Node groups that use this node template will create nodes of a type that matches these properties.
               
               This field is mutually exclusive with the node_type property; you can only define one or the other, but not both.
        :param pulumi.Input[str] region: [Output Only] The name of the region where the node template resides, such as us-central1.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[pulumi.InputType['ServerBindingArgs']] server_binding: Sets the binding properties for the physical server. Valid values include:  
               - [Default] RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server 
               - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible  
               
               See Sole-tenant node options for more information.
        :param pulumi.Input[str] status: [Output Only] The status of the node template. One of the following values: CREATING, READY, and DELETING.
        :param pulumi.Input[str] status_message: [Output Only] An optional, human-readable explanation of the status.
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

            __props__['accelerators'] = accelerators
            __props__['cpu_overcommit_type'] = cpu_overcommit_type
            __props__['creation_timestamp'] = creation_timestamp
            __props__['description'] = description
            __props__['disks'] = disks
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['name'] = name
            __props__['node_affinity_labels'] = node_affinity_labels
            if node_template is None and not opts.urn:
                raise TypeError("Missing required property 'node_template'")
            __props__['node_template'] = node_template
            __props__['node_type'] = node_type
            __props__['node_type_flexibility'] = node_type_flexibility
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            __props__['self_link'] = self_link
            __props__['server_binding'] = server_binding
            __props__['status'] = status
            __props__['status_message'] = status_message
        super(NodeTemplate, __self__).__init__(
            'gcp-native:compute/v1:NodeTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NodeTemplate':
        """
        Get an existing NodeTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["accelerators"] = None
        __props__["cpu_overcommit_type"] = None
        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["disks"] = None
        __props__["kind"] = None
        __props__["name"] = None
        __props__["node_affinity_labels"] = None
        __props__["node_type"] = None
        __props__["node_type_flexibility"] = None
        __props__["region"] = None
        __props__["self_link"] = None
        __props__["server_binding"] = None
        __props__["status"] = None
        __props__["status_message"] = None
        return NodeTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accelerators(self) -> pulumi.Output[Sequence['outputs.AcceleratorConfigResponse']]:
        return pulumi.get(self, "accelerators")

    @property
    @pulumi.getter(name="cpuOvercommitType")
    def cpu_overcommit_type(self) -> pulumi.Output[str]:
        """
        CPU overcommit.
        """
        return pulumi.get(self, "cpu_overcommit_type")

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
    def disks(self) -> pulumi.Output[Sequence['outputs.LocalDiskResponse']]:
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] The type of the resource. Always compute#nodeTemplate for node templates.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeAffinityLabels")
    def node_affinity_labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels to use for node affinity, which will be used in instance scheduling.
        """
        return pulumi.get(self, "node_affinity_labels")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[str]:
        """
        The node type to use for nodes group that are created from this template.
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter(name="nodeTypeFlexibility")
    def node_type_flexibility(self) -> pulumi.Output['outputs.NodeTemplateNodeTypeFlexibilityResponse']:
        """
        The flexible properties of the desired node type. Node groups that use this node template will create nodes of a type that matches these properties.

        This field is mutually exclusive with the node_type property; you can only define one or the other, but not both.
        """
        return pulumi.get(self, "node_type_flexibility")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] The name of the region where the node template resides, such as us-central1.
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
    @pulumi.getter(name="serverBinding")
    def server_binding(self) -> pulumi.Output['outputs.ServerBindingResponse']:
        """
        Sets the binding properties for the physical server. Valid values include:  
        - [Default] RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server 
        - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible  

        See Sole-tenant node options for more information.
        """
        return pulumi.get(self, "server_binding")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        [Output Only] The status of the node template. One of the following values: CREATING, READY, and DELETING.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        [Output Only] An optional, human-readable explanation of the status.
        """
        return pulumi.get(self, "status_message")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

