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

__all__ = ['StoredInfoType']


class StoredInfoType(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['GooglePrivacyDlpV2StoredInfoTypeConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 stored_info_type_id: Optional[pulumi.Input[str]] = None,
                 stored_info_types_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GooglePrivacyDlpV2StoredInfoTypeConfigArgs']] config: Required. Configuration of the storedInfoType to create.
        :param pulumi.Input[str] stored_info_type_id: The storedInfoType ID can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.
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

            __props__['config'] = config
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['stored_info_type_id'] = stored_info_type_id
            if stored_info_types_id is None and not opts.urn:
                raise TypeError("Missing required property 'stored_info_types_id'")
            __props__['stored_info_types_id'] = stored_info_types_id
            __props__['current_version'] = None
            __props__['name'] = None
            __props__['pending_versions'] = None
        super(StoredInfoType, __self__).__init__(
            'gcp-native:dlp/v2:StoredInfoType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StoredInfoType':
        """
        Get an existing StoredInfoType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["current_version"] = None
        __props__["name"] = None
        __props__["pending_versions"] = None
        return StoredInfoType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> pulumi.Output['outputs.GooglePrivacyDlpV2StoredInfoTypeVersionResponse']:
        """
        Current version of the stored info type.
        """
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pendingVersions")
    def pending_versions(self) -> pulumi.Output[Sequence['outputs.GooglePrivacyDlpV2StoredInfoTypeVersionResponse']]:
        """
        Pending versions of the stored info type. Empty if no versions are pending.
        """
        return pulumi.get(self, "pending_versions")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

