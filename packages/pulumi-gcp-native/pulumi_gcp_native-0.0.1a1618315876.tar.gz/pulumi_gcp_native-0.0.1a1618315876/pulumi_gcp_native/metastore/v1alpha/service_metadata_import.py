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

__all__ = ['ServiceMetadataImport']


class ServiceMetadataImport(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_dump: Optional[pulumi.Input[pulumi.InputType['DatabaseDumpArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 metadata_imports_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 services_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new MetadataImport in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DatabaseDumpArgs']] database_dump: Immutable. A database dump from a pre-existing metastore's database.
        :param pulumi.Input[str] description: The description of the metadata import.
        :param pulumi.Input[str] name: Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}.
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

            __props__['database_dump'] = database_dump
            __props__['description'] = description
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            if metadata_imports_id is None and not opts.urn:
                raise TypeError("Missing required property 'metadata_imports_id'")
            __props__['metadata_imports_id'] = metadata_imports_id
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            if services_id is None and not opts.urn:
                raise TypeError("Missing required property 'services_id'")
            __props__['services_id'] = services_id
            __props__['create_time'] = None
            __props__['state'] = None
            __props__['update_time'] = None
        super(ServiceMetadataImport, __self__).__init__(
            'gcp-native:metastore/v1alpha:ServiceMetadataImport',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceMetadataImport':
        """
        Get an existing ServiceMetadataImport resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = None
        __props__["database_dump"] = None
        __props__["description"] = None
        __props__["name"] = None
        __props__["state"] = None
        __props__["update_time"] = None
        return ServiceMetadataImport(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the metadata import was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="databaseDump")
    def database_dump(self) -> pulumi.Output['outputs.DatabaseDumpResponse']:
        """
        Immutable. A database dump from a pre-existing metastore's database.
        """
        return pulumi.get(self, "database_dump")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the metadata import.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the metadata import.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the metadata import was last updated.
        """
        return pulumi.get(self, "update_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

