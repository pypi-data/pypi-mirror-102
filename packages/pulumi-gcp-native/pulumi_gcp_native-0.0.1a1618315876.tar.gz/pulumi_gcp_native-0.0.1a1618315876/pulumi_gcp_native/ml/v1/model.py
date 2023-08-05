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

__all__ = ['Model']


class Model(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_version: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__VersionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 models_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 online_prediction_console_logging: Optional[pulumi.Input[bool]] = None,
                 online_prediction_logging: Optional[pulumi.Input[bool]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a model which will later contain one or more versions. You must add at least one version before you can request predictions from the model. Add versions by calling projects.models.versions.create.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudMlV1__VersionArgs']] default_version: The default version of the model. This version will be used to handle prediction requests that do not specify a version. You can change the default version by calling projects.models.versions.setDefault.
        :param pulumi.Input[str] description: Optional. The description specified for the model when it was created.
        :param pulumi.Input[str] etag: `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a model from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform model updates in order to avoid race conditions: An `etag` is returned in the response to `GetModel`, and systems are expected to put that etag in the request to `UpdateModel` to ensure that their change will be applied to the model as intended.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. One or more labels that you can add, to organize your models. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        :param pulumi.Input[str] name: Required. The name specified for the model when it was created. The model name must be unique within the project it is created in.
        :param pulumi.Input[bool] online_prediction_console_logging: Optional. If true, online prediction nodes send `stderr` and `stdout` streams to Cloud Logging. These can be more verbose than the standard access logs (see `onlinePredictionLogging`) and can incur higher cost. However, they are helpful for debugging. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high QPS. Estimate your costs before enabling this option. Default is false.
        :param pulumi.Input[bool] online_prediction_logging: Optional. If true, online prediction access logs are sent to Cloud Logging. These logs are like standard server access logs, containing information like timestamp and latency for each request. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high queries per second rate (QPS). Estimate your costs before enabling this option. Default is false.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: Optional. The list of regions where the model is going to be deployed. Only one region per model is supported. Defaults to 'us-central1' if nothing is set. See the available regions for AI Platform services. Note: * No matter where a model is deployed, it can always be accessed by users from anywhere, both for online and batch prediction. * The region for a batch prediction job is set by the region field when submitting the batch prediction job and does not take its value from this field.
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

            __props__['default_version'] = default_version
            __props__['description'] = description
            __props__['etag'] = etag
            __props__['labels'] = labels
            if models_id is None and not opts.urn:
                raise TypeError("Missing required property 'models_id'")
            __props__['models_id'] = models_id
            __props__['name'] = name
            __props__['online_prediction_console_logging'] = online_prediction_console_logging
            __props__['online_prediction_logging'] = online_prediction_logging
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['regions'] = regions
        super(Model, __self__).__init__(
            'gcp-native:ml/v1:Model',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Model':
        """
        Get an existing Model resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["default_version"] = None
        __props__["description"] = None
        __props__["etag"] = None
        __props__["labels"] = None
        __props__["name"] = None
        __props__["online_prediction_console_logging"] = None
        __props__["online_prediction_logging"] = None
        __props__["regions"] = None
        return Model(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> pulumi.Output['outputs.GoogleCloudMlV1__VersionResponse']:
        """
        The default version of the model. This version will be used to handle prediction requests that do not specify a version. You can change the default version by calling projects.models.versions.setDefault.
        """
        return pulumi.get(self, "default_version")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. The description specified for the model when it was created.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a model from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform model updates in order to avoid race conditions: An `etag` is returned in the response to `GetModel`, and systems are expected to put that etag in the request to `UpdateModel` to ensure that their change will be applied to the model as intended.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. One or more labels that you can add, to organize your models. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The name specified for the model when it was created. The model name must be unique within the project it is created in.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onlinePredictionConsoleLogging")
    def online_prediction_console_logging(self) -> pulumi.Output[bool]:
        """
        Optional. If true, online prediction nodes send `stderr` and `stdout` streams to Cloud Logging. These can be more verbose than the standard access logs (see `onlinePredictionLogging`) and can incur higher cost. However, they are helpful for debugging. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high QPS. Estimate your costs before enabling this option. Default is false.
        """
        return pulumi.get(self, "online_prediction_console_logging")

    @property
    @pulumi.getter(name="onlinePredictionLogging")
    def online_prediction_logging(self) -> pulumi.Output[bool]:
        """
        Optional. If true, online prediction access logs are sent to Cloud Logging. These logs are like standard server access logs, containing information like timestamp and latency for each request. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high queries per second rate (QPS). Estimate your costs before enabling this option. Default is false.
        """
        return pulumi.get(self, "online_prediction_logging")

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. The list of regions where the model is going to be deployed. Only one region per model is supported. Defaults to 'us-central1' if nothing is set. See the available regions for AI Platform services. Note: * No matter where a model is deployed, it can always be accessed by users from anywhere, both for online and batch prediction. * The region for a batch prediction job is set by the region field when submitting the batch prediction job and does not take its value from this field.
        """
        return pulumi.get(self, "regions")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

