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

__all__ = ['ConnectionProfile']


class ConnectionProfile(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloudsql: Optional[pulumi.Input[pulumi.InputType['CloudSqlConnectionProfileArgs']]] = None,
                 connection_profiles_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 mysql: Optional[pulumi.Input[pulumi.InputType['MySqlConnectionProfileArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 postgresql: Optional[pulumi.Input[pulumi.InputType['PostgreSqlConnectionProfileArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 provider: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new connection profile in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CloudSqlConnectionProfileArgs']] cloudsql: A CloudSQL database connection profile.
        :param pulumi.Input[str] display_name: The connection profile display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.
        :param pulumi.Input[pulumi.InputType['MySqlConnectionProfileArgs']] mysql: A MySQL database connection profile.
        :param pulumi.Input[str] name: The name of this connection profile resource in the form of projects/{project}/locations/{location}/instances/{instance}.
        :param pulumi.Input[pulumi.InputType['PostgreSqlConnectionProfileArgs']] postgresql: A PostgreSQL database connection profile.
        :param pulumi.Input[str] provider: The database provider.
        :param pulumi.Input[str] state: The current connection profile state (e.g. DRAFT, READY, or FAILED).
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

            __props__['cloudsql'] = cloudsql
            if connection_profiles_id is None and not opts.urn:
                raise TypeError("Missing required property 'connection_profiles_id'")
            __props__['connection_profiles_id'] = connection_profiles_id
            __props__['display_name'] = display_name
            __props__['labels'] = labels
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['mysql'] = mysql
            __props__['name'] = name
            __props__['postgresql'] = postgresql
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['provider'] = provider
            __props__['state'] = state
            __props__['create_time'] = None
            __props__['error'] = None
            __props__['update_time'] = None
        super(ConnectionProfile, __self__).__init__(
            'gcp-native:datamigration/v1:ConnectionProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectionProfile':
        """
        Get an existing ConnectionProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cloudsql"] = None
        __props__["create_time"] = None
        __props__["display_name"] = None
        __props__["error"] = None
        __props__["labels"] = None
        __props__["mysql"] = None
        __props__["name"] = None
        __props__["postgresql"] = None
        __props__["provider"] = None
        __props__["state"] = None
        __props__["update_time"] = None
        return ConnectionProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cloudsql(self) -> pulumi.Output['outputs.CloudSqlConnectionProfileResponse']:
        """
        A CloudSQL database connection profile.
        """
        return pulumi.get(self, "cloudsql")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp when the resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The connection profile display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output['outputs.StatusResponse']:
        """
        The error details in case of state FAILED.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def mysql(self) -> pulumi.Output['outputs.MySqlConnectionProfileResponse']:
        """
        A MySQL database connection profile.
        """
        return pulumi.get(self, "mysql")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of this connection profile resource in the form of projects/{project}/locations/{location}/instances/{instance}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def postgresql(self) -> pulumi.Output['outputs.PostgreSqlConnectionProfileResponse']:
        """
        A PostgreSQL database connection profile.
        """
        return pulumi.get(self, "postgresql")

    @property
    @pulumi.getter
    def provider(self) -> pulumi.Output[str]:
        """
        The database provider.
        """
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current connection profile state (e.g. DRAFT, READY, or FAILED).
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The timestamp when the resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

