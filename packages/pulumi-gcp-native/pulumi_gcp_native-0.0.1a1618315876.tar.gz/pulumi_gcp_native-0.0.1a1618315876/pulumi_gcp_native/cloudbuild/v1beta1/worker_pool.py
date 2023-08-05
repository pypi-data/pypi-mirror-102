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

__all__ = ['WorkerPool']


class WorkerPool(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 network_config: Optional[pulumi.Input[pulumi.InputType['NetworkConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 worker_config: Optional[pulumi.Input[pulumi.InputType['WorkerConfigArgs']]] = None,
                 worker_pools_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a `WorkerPool` to run the builds, and returns the new worker pool. NOTE: As of now, this method returns an `Operation` that is always complete.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['NetworkConfigArgs']] network_config: Network configuration for the `WorkerPool`.
        :param pulumi.Input[pulumi.InputType['WorkerConfigArgs']] worker_config: Worker configuration for the `WorkerPool`.
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

            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['network_config'] = network_config
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['worker_config'] = worker_config
            if worker_pools_id is None and not opts.urn:
                raise TypeError("Missing required property 'worker_pools_id'")
            __props__['worker_pools_id'] = worker_pools_id
            __props__['create_time'] = None
            __props__['delete_time'] = None
            __props__['name'] = None
            __props__['state'] = None
            __props__['update_time'] = None
        super(WorkerPool, __self__).__init__(
            'gcp-native:cloudbuild/v1beta1:WorkerPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkerPool':
        """
        Get an existing WorkerPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = None
        __props__["delete_time"] = None
        __props__["name"] = None
        __props__["network_config"] = None
        __props__["state"] = None
        __props__["update_time"] = None
        __props__["worker_config"] = None
        return WorkerPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time at which the request to create the `WorkerPool` was received.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        Time at which the request to delete the `WorkerPool` was received.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the `WorkerPool`, with format `projects/{project}/locations/{location}/workerPools/{worker_pool}`. The value of `{worker_pool}` is provided by `worker_pool_id` in `CreateWorkerPool` request and the value of `{location}` is determined by the endpoint accessed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output['outputs.NetworkConfigResponse']:
        """
        Network configuration for the `WorkerPool`.
        """
        return pulumi.get(self, "network_config")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        `WorkerPool` state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time at which the request to update the `WorkerPool` was received.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> pulumi.Output['outputs.WorkerConfigResponse']:
        """
        Worker configuration for the `WorkerPool`.
        """
        return pulumi.get(self, "worker_config")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

