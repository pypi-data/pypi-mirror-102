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

__all__ = ['Queue']


class Queue(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine_routing_override: Optional[pulumi.Input[pulumi.InputType['AppEngineRoutingArgs']]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 purge_time: Optional[pulumi.Input[str]] = None,
                 queues_id: Optional[pulumi.Input[str]] = None,
                 rate_limits: Optional[pulumi.Input[pulumi.InputType['RateLimitsArgs']]] = None,
                 retry_config: Optional[pulumi.Input[pulumi.InputType['RetryConfigArgs']]] = None,
                 stackdriver_logging_config: Optional[pulumi.Input[pulumi.InputType['StackdriverLoggingConfigArgs']]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a queue. Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not. WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppEngineRoutingArgs']] app_engine_routing_override: Overrides for task-level app_engine_routing. These settings apply only to App Engine tasks in this queue. Http tasks are not affected. If set, `app_engine_routing_override` is used for all App Engine tasks in the queue, no matter what the setting is for the task-level app_engine_routing.
        :param pulumi.Input[str] name: Caller-specified and required in CreateQueue, after which it becomes output only. The queue name. The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
        :param pulumi.Input[str] purge_time: The last time this queue was purged. All tasks that were created before this time were purged. A queue can be purged using PurgeQueue, the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue). Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged.
        :param pulumi.Input[pulumi.InputType['RateLimitsArgs']] rate_limits: Rate limits for task dispatches. rate_limits and retry_config are related because they both control task attempts. However they control task attempts in different ways: * rate_limits controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry). * retry_config controls what happens to particular a task after its first attempt fails. That is, retry_config controls task retries (the second attempt, third attempt, etc). The queue's actual dispatch rate is the result of: * Number of tasks in the queue * User-specified throttling: rate_limits, retry_config, and the queue's state. * System throttling due to `429` (Too Many Requests) or `503` (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic spikes.
        :param pulumi.Input[pulumi.InputType['RetryConfigArgs']] retry_config: Settings that determine the retry behavior. * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks. * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).
        :param pulumi.Input[pulumi.InputType['StackdriverLoggingConfigArgs']] stackdriver_logging_config: Configuration options for writing logs to [Stackdriver Logging](https://cloud.google.com/logging/docs/). If this field is unset, then no logs are written.
        :param pulumi.Input[str] state: The state of the queue. `state` can only be changed by called PauseQueue, ResumeQueue, or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). UpdateQueue cannot be used to change `state`.
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

            __props__['app_engine_routing_override'] = app_engine_routing_override
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['purge_time'] = purge_time
            if queues_id is None and not opts.urn:
                raise TypeError("Missing required property 'queues_id'")
            __props__['queues_id'] = queues_id
            __props__['rate_limits'] = rate_limits
            __props__['retry_config'] = retry_config
            __props__['stackdriver_logging_config'] = stackdriver_logging_config
            __props__['state'] = state
        super(Queue, __self__).__init__(
            'gcp-native:cloudtasks/v2:Queue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Queue':
        """
        Get an existing Queue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_engine_routing_override"] = None
        __props__["name"] = None
        __props__["purge_time"] = None
        __props__["rate_limits"] = None
        __props__["retry_config"] = None
        __props__["stackdriver_logging_config"] = None
        __props__["state"] = None
        return Queue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appEngineRoutingOverride")
    def app_engine_routing_override(self) -> pulumi.Output['outputs.AppEngineRoutingResponse']:
        """
        Overrides for task-level app_engine_routing. These settings apply only to App Engine tasks in this queue. Http tasks are not affected. If set, `app_engine_routing_override` is used for all App Engine tasks in the queue, no matter what the setting is for the task-level app_engine_routing.
        """
        return pulumi.get(self, "app_engine_routing_override")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Caller-specified and required in CreateQueue, after which it becomes output only. The queue name. The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="purgeTime")
    def purge_time(self) -> pulumi.Output[str]:
        """
        The last time this queue was purged. All tasks that were created before this time were purged. A queue can be purged using PurgeQueue, the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue). Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged.
        """
        return pulumi.get(self, "purge_time")

    @property
    @pulumi.getter(name="rateLimits")
    def rate_limits(self) -> pulumi.Output['outputs.RateLimitsResponse']:
        """
        Rate limits for task dispatches. rate_limits and retry_config are related because they both control task attempts. However they control task attempts in different ways: * rate_limits controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry). * retry_config controls what happens to particular a task after its first attempt fails. That is, retry_config controls task retries (the second attempt, third attempt, etc). The queue's actual dispatch rate is the result of: * Number of tasks in the queue * User-specified throttling: rate_limits, retry_config, and the queue's state. * System throttling due to `429` (Too Many Requests) or `503` (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic spikes.
        """
        return pulumi.get(self, "rate_limits")

    @property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> pulumi.Output['outputs.RetryConfigResponse']:
        """
        Settings that determine the retry behavior. * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks. * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).
        """
        return pulumi.get(self, "retry_config")

    @property
    @pulumi.getter(name="stackdriverLoggingConfig")
    def stackdriver_logging_config(self) -> pulumi.Output['outputs.StackdriverLoggingConfigResponse']:
        """
        Configuration options for writing logs to [Stackdriver Logging](https://cloud.google.com/logging/docs/). If this field is unset, then no logs are written.
        """
        return pulumi.get(self, "stackdriver_logging_config")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the queue. `state` can only be changed by called PauseQueue, ResumeQueue, or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). UpdateQueue cannot be used to change `state`.
        """
        return pulumi.get(self, "state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

