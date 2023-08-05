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

__all__ = ['Dataset']


class Dataset(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blocking_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 data_item_count: Optional[pulumi.Input[str]] = None,
                 datasets_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 input_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDatalabelingV1beta1InputConfigArgs']]]]] = None,
                 last_migrate_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates dataset. If success return a Dataset resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] blocking_resources: The names of any related resources that are blocking changes to the dataset.
        :param pulumi.Input[str] create_time: Time the dataset is created.
        :param pulumi.Input[str] data_item_count: The number of data items in the dataset.
        :param pulumi.Input[str] description: Optional. User-provided description of the annotation specification set. The description can be up to 10000 characters long.
        :param pulumi.Input[str] display_name: Required. The display name of the dataset. Maximum of 64 characters.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDatalabelingV1beta1InputConfigArgs']]]] input_configs: This is populated with the original input configs where ImportData is called. It is available only after the clients import data to this dataset.
        :param pulumi.Input[str] last_migrate_time: Last time that the Dataset is migrated to AI Platform V2. If any of the AnnotatedDataset is migrated, the last_migration_time in Dataset is also updated.
        :param pulumi.Input[str] name: Dataset resource name, format is: projects/{project_id}/datasets/{dataset_id}
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

            __props__['blocking_resources'] = blocking_resources
            __props__['create_time'] = create_time
            __props__['data_item_count'] = data_item_count
            if datasets_id is None and not opts.urn:
                raise TypeError("Missing required property 'datasets_id'")
            __props__['datasets_id'] = datasets_id
            __props__['description'] = description
            __props__['display_name'] = display_name
            __props__['input_configs'] = input_configs
            __props__['last_migrate_time'] = last_migrate_time
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
        super(Dataset, __self__).__init__(
            'gcp-native:datalabeling/v1beta1:Dataset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Dataset':
        """
        Get an existing Dataset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["blocking_resources"] = None
        __props__["create_time"] = None
        __props__["data_item_count"] = None
        __props__["description"] = None
        __props__["display_name"] = None
        __props__["input_configs"] = None
        __props__["last_migrate_time"] = None
        __props__["name"] = None
        return Dataset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blockingResources")
    def blocking_resources(self) -> pulumi.Output[Sequence[str]]:
        """
        The names of any related resources that are blocking changes to the dataset.
        """
        return pulumi.get(self, "blocking_resources")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time the dataset is created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataItemCount")
    def data_item_count(self) -> pulumi.Output[str]:
        """
        The number of data items in the dataset.
        """
        return pulumi.get(self, "data_item_count")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. User-provided description of the annotation specification set. The description can be up to 10000 characters long.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The display name of the dataset. Maximum of 64 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="inputConfigs")
    def input_configs(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDatalabelingV1beta1InputConfigResponse']]:
        """
        This is populated with the original input configs where ImportData is called. It is available only after the clients import data to this dataset.
        """
        return pulumi.get(self, "input_configs")

    @property
    @pulumi.getter(name="lastMigrateTime")
    def last_migrate_time(self) -> pulumi.Output[str]:
        """
        Last time that the Dataset is migrated to AI Platform V2. If any of the AnnotatedDataset is migrated, the last_migration_time in Dataset is also updated.
        """
        return pulumi.get(self, "last_migrate_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Dataset resource name, format is: projects/{project_id}/datasets/{dataset_id}
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

