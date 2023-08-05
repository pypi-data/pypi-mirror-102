# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['OrganizationEnvironmentReference']


class OrganizationEnvironmentReference(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environments_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 references_id: Optional[pulumi.Input[str]] = None,
                 refers: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a Reference in the specified environment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. A human-readable description of this reference.
        :param pulumi.Input[str] name: Required. The resource id of this reference. Values must match the regular expression [\w\s\-.]+.
        :param pulumi.Input[str] refers: Required. The id of the resource to which this reference refers. Must be the id of a resource that exists in the parent environment and is of the given resource_type.
        :param pulumi.Input[str] resource_type: The type of resource referred to by this reference. Valid values are 'KeyStore' or 'TrustStore'.
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

            __props__['description'] = description
            if environments_id is None and not opts.urn:
                raise TypeError("Missing required property 'environments_id'")
            __props__['environments_id'] = environments_id
            __props__['name'] = name
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__['organizations_id'] = organizations_id
            if references_id is None and not opts.urn:
                raise TypeError("Missing required property 'references_id'")
            __props__['references_id'] = references_id
            __props__['refers'] = refers
            __props__['resource_type'] = resource_type
        super(OrganizationEnvironmentReference, __self__).__init__(
            'gcp-native:apigee/v1:OrganizationEnvironmentReference',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationEnvironmentReference':
        """
        Get an existing OrganizationEnvironmentReference resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = None
        __props__["name"] = None
        __props__["refers"] = None
        __props__["resource_type"] = None
        return OrganizationEnvironmentReference(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A human-readable description of this reference.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The resource id of this reference. Values must match the regular expression [\w\s\-.]+.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def refers(self) -> pulumi.Output[str]:
        """
        Required. The id of the resource to which this reference refers. Must be the id of a resource that exists in the parent environment and is of the given resource_type.
        """
        return pulumi.get(self, "refers")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        The type of resource referred to by this reference. Valid values are 'KeyStore' or 'TrustStore'.
        """
        return pulumi.get(self, "resource_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

