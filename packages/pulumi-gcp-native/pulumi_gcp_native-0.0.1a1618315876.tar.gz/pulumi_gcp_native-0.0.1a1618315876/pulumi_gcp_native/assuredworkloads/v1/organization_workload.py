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

__all__ = ['OrganizationWorkload']


class OrganizationWorkload(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account: Optional[pulumi.Input[str]] = None,
                 compliance_regime: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kms_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 provisioned_resources_parent: Optional[pulumi.Input[str]] = None,
                 workloads_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates Assured Workload.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_account: Required. Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.
        :param pulumi.Input[str] compliance_regime: Required. Immutable. Compliance Regime associated with this workload.
        :param pulumi.Input[str] display_name: Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload
        :param pulumi.Input[str] etag: Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.
        :param pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']] kms_settings: Input only. Settings used to create a CMEK crypto key. When set a project with a KMS CMEK key is provisioned. This field is mandatory for a subset of Compliance Regimes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels applied to the workload.
        :param pulumi.Input[str] name: Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload} Read-only.
        :param pulumi.Input[str] provisioned_resources_parent: Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id} organizations/{organization_id}
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

            __props__['billing_account'] = billing_account
            __props__['compliance_regime'] = compliance_regime
            __props__['display_name'] = display_name
            __props__['etag'] = etag
            __props__['kms_settings'] = kms_settings
            __props__['labels'] = labels
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['name'] = name
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__['organizations_id'] = organizations_id
            __props__['provisioned_resources_parent'] = provisioned_resources_parent
            if workloads_id is None and not opts.urn:
                raise TypeError("Missing required property 'workloads_id'")
            __props__['workloads_id'] = workloads_id
            __props__['create_time'] = None
            __props__['resources'] = None
        super(OrganizationWorkload, __self__).__init__(
            'gcp-native:assuredworkloads/v1:OrganizationWorkload',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationWorkload':
        """
        Get an existing OrganizationWorkload resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["billing_account"] = None
        __props__["compliance_regime"] = None
        __props__["create_time"] = None
        __props__["display_name"] = None
        __props__["etag"] = None
        __props__["kms_settings"] = None
        __props__["labels"] = None
        __props__["name"] = None
        __props__["provisioned_resources_parent"] = None
        __props__["resources"] = None
        return OrganizationWorkload(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Output[str]:
        """
        Required. Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.
        """
        return pulumi.get(self, "billing_account")

    @property
    @pulumi.getter(name="complianceRegime")
    def compliance_regime(self) -> pulumi.Output[str]:
        """
        Required. Immutable. Compliance Regime associated with this workload.
        """
        return pulumi.get(self, "compliance_regime")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Immutable. The Workload creation timestamp.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> pulumi.Output['outputs.GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsResponse']:
        """
        Input only. Settings used to create a CMEK crypto key. When set a project with a KMS CMEK key is provisioned. This field is mandatory for a subset of Compliance Regimes.
        """
        return pulumi.get(self, "kms_settings")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Labels applied to the workload.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload} Read-only.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisionedResourcesParent")
    def provisioned_resources_parent(self) -> pulumi.Output[str]:
        """
        Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id} organizations/{organization_id}
        """
        return pulumi.get(self, "provisioned_resources_parent")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence['outputs.GoogleCloudAssuredworkloadsV1WorkloadResourceInfoResponse']]:
        """
        The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.
        """
        return pulumi.get(self, "resources")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

