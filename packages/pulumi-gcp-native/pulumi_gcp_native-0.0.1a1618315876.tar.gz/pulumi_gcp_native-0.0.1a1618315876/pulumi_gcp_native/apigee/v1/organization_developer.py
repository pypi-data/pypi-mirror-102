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

__all__ = ['OrganizationDeveloper']


class OrganizationDeveloper(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_type: Optional[pulumi.Input[str]] = None,
                 app_family: Optional[pulumi.Input[str]] = None,
                 apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]]] = None,
                 companies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 developer_id: Optional[pulumi.Input[str]] = None,
                 developers_id: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a developer. Once created, the developer can register an app and obtain an API key. At creation time, a developer is set as `active`. To change the developer status, use the SetDeveloperStatus API.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_type: Access type.
        :param pulumi.Input[str] app_family: Developer app family.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] apps: List of apps associated with the developer.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]] attributes: Optional. Developer attributes (name/value pairs). The custom attribute limit is 18.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] companies: List of companies associated with the developer.
        :param pulumi.Input[str] developer_id: ID of the developer. **Note**: IDs are generated internally by Apigee and are not guaranteed to stay the same over time.
        :param pulumi.Input[str] email: Required. Email address of the developer. This value is used to uniquely identify the developer in Apigee hybrid. Note that the email address has to be in lowercase only.
        :param pulumi.Input[str] first_name: Required. First name of the developer.
        :param pulumi.Input[str] last_name: Required. Last name of the developer.
        :param pulumi.Input[str] user_name: Required. User name of the developer. Not used by Apigee hybrid.
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

            __props__['access_type'] = access_type
            __props__['app_family'] = app_family
            __props__['apps'] = apps
            __props__['attributes'] = attributes
            __props__['companies'] = companies
            __props__['developer_id'] = developer_id
            if developers_id is None and not opts.urn:
                raise TypeError("Missing required property 'developers_id'")
            __props__['developers_id'] = developers_id
            __props__['email'] = email
            __props__['first_name'] = first_name
            __props__['last_name'] = last_name
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__['organizations_id'] = organizations_id
            __props__['user_name'] = user_name
            __props__['created_at'] = None
            __props__['last_modified_at'] = None
            __props__['organization_name'] = None
            __props__['status'] = None
        super(OrganizationDeveloper, __self__).__init__(
            'gcp-native:apigee/v1:OrganizationDeveloper',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationDeveloper':
        """
        Get an existing OrganizationDeveloper resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_type"] = None
        __props__["app_family"] = None
        __props__["apps"] = None
        __props__["attributes"] = None
        __props__["companies"] = None
        __props__["created_at"] = None
        __props__["developer_id"] = None
        __props__["email"] = None
        __props__["first_name"] = None
        __props__["last_modified_at"] = None
        __props__["last_name"] = None
        __props__["organization_name"] = None
        __props__["status"] = None
        __props__["user_name"] = None
        return OrganizationDeveloper(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessType")
    def access_type(self) -> pulumi.Output[str]:
        """
        Access type.
        """
        return pulumi.get(self, "access_type")

    @property
    @pulumi.getter(name="appFamily")
    def app_family(self) -> pulumi.Output[str]:
        """
        Developer app family.
        """
        return pulumi.get(self, "app_family")

    @property
    @pulumi.getter
    def apps(self) -> pulumi.Output[Sequence[str]]:
        """
        List of apps associated with the developer.
        """
        return pulumi.get(self, "apps")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Sequence['outputs.GoogleCloudApigeeV1AttributeResponse']]:
        """
        Optional. Developer attributes (name/value pairs). The custom attribute limit is 18.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def companies(self) -> pulumi.Output[Sequence[str]]:
        """
        List of companies associated with the developer.
        """
        return pulumi.get(self, "companies")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time at which the developer was created in milliseconds since epoch.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="developerId")
    def developer_id(self) -> pulumi.Output[str]:
        """
        ID of the developer. **Note**: IDs are generated internally by Apigee and are not guaranteed to stay the same over time.
        """
        return pulumi.get(self, "developer_id")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Required. Email address of the developer. This value is used to uniquely identify the developer in Apigee hybrid. Note that the email address has to be in lowercase only.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[str]:
        """
        Required. First name of the developer.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[str]:
        """
        Time at which the developer was last modified in milliseconds since epoch.
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[str]:
        """
        Required. Last name of the developer.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> pulumi.Output[str]:
        """
        Name of the Apigee organization in which the developer resides.
        """
        return pulumi.get(self, "organization_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the developer. Valid values are `active` and `inactive`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Required. User name of the developer. Not used by Apigee hybrid.
        """
        return pulumi.get(self, "user_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

