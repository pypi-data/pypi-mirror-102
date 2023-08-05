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

__all__ = ['ServiceRollout']


class ServiceRollout(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 delete_service_strategy: Optional[pulumi.Input[pulumi.InputType['DeleteServiceStrategyArgs']]] = None,
                 rollout_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 traffic_percent_strategy: Optional[pulumi.Input[pulumi.InputType['TrafficPercentStrategyArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging. Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts. Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually. Operation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Creation time of the rollout. Readonly.
        :param pulumi.Input[str] created_by: This field is deprecated and will be deleted. Please remove usage of this field.
        :param pulumi.Input[pulumi.InputType['DeleteServiceStrategyArgs']] delete_service_strategy: The strategy associated with a rollout to delete a `ManagedService`. Readonly.
        :param pulumi.Input[str] rollout_id: Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
        :param pulumi.Input[str] service_name: The name of the service associated with this Rollout.
        :param pulumi.Input[str] status: The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.
        :param pulumi.Input[pulumi.InputType['TrafficPercentStrategyArgs']] traffic_percent_strategy: Google Service Control selects service configurations based on traffic percentage.
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

            __props__['create_time'] = create_time
            __props__['created_by'] = created_by
            __props__['delete_service_strategy'] = delete_service_strategy
            if rollout_id is None and not opts.urn:
                raise TypeError("Missing required property 'rollout_id'")
            __props__['rollout_id'] = rollout_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__['service_name'] = service_name
            __props__['status'] = status
            __props__['traffic_percent_strategy'] = traffic_percent_strategy
        super(ServiceRollout, __self__).__init__(
            'gcp-native:servicemanagement/v1:ServiceRollout',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceRollout':
        """
        Get an existing ServiceRollout resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = None
        __props__["created_by"] = None
        __props__["delete_service_strategy"] = None
        __props__["rollout_id"] = None
        __props__["service_name"] = None
        __props__["status"] = None
        __props__["traffic_percent_strategy"] = None
        return ServiceRollout(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of the rollout. Readonly.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        This field is deprecated and will be deleted. Please remove usage of this field.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="deleteServiceStrategy")
    def delete_service_strategy(self) -> pulumi.Output['outputs.DeleteServiceStrategyResponse']:
        """
        The strategy associated with a rollout to delete a `ManagedService`. Readonly.
        """
        return pulumi.get(self, "delete_service_strategy")

    @property
    @pulumi.getter(name="rolloutId")
    def rollout_id(self) -> pulumi.Output[str]:
        """
        Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
        """
        return pulumi.get(self, "rollout_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The name of the service associated with this Rollout.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="trafficPercentStrategy")
    def traffic_percent_strategy(self) -> pulumi.Output['outputs.TrafficPercentStrategyResponse']:
        """
        Google Service Control selects service configurations based on traffic percentage.
        """
        return pulumi.get(self, "traffic_percent_strategy")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

