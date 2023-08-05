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

__all__ = ['AgentEnvironmentExperiment']


class AgentEnvironmentExperiment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agents_id: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1ExperimentDefinitionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 environments_id: Optional[pulumi.Input[str]] = None,
                 experiment_length: Optional[pulumi.Input[str]] = None,
                 experiments_id: Optional[pulumi.Input[str]] = None,
                 last_update_time: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 result: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1ExperimentResultArgs']]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 variants_history: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1VariantsHistoryArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an Experiment in the specified Environment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Creation time of this experiment.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1ExperimentDefinitionArgs']] definition: The definition of the experiment.
        :param pulumi.Input[str] description: The human-readable description of the experiment.
        :param pulumi.Input[str] display_name: Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters.
        :param pulumi.Input[str] end_time: End time of this experiment.
        :param pulumi.Input[str] experiment_length: Maximum number of days to run the experiment. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days.
        :param pulumi.Input[str] last_update_time: Last update time of this experiment.
        :param pulumi.Input[str] name: The name of the experiment. Format: projects//locations//agents//environments//experiments/..
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1ExperimentResultArgs']] result: Inference result of the experiment.
        :param pulumi.Input[str] start_time: Start time of this experiment.
        :param pulumi.Input[str] state: The current state of the experiment. Transition triggered by Expriments.StartExperiment: PENDING->RUNNING. Transition triggered by Expriments.CancelExperiment: PENDING->CANCELLED or RUNNING->CANCELLED.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1VariantsHistoryArgs']]]] variants_history: The history of updates to the experiment variants.
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

            if agents_id is None and not opts.urn:
                raise TypeError("Missing required property 'agents_id'")
            __props__['agents_id'] = agents_id
            __props__['create_time'] = create_time
            __props__['definition'] = definition
            __props__['description'] = description
            __props__['display_name'] = display_name
            __props__['end_time'] = end_time
            if environments_id is None and not opts.urn:
                raise TypeError("Missing required property 'environments_id'")
            __props__['environments_id'] = environments_id
            __props__['experiment_length'] = experiment_length
            if experiments_id is None and not opts.urn:
                raise TypeError("Missing required property 'experiments_id'")
            __props__['experiments_id'] = experiments_id
            __props__['last_update_time'] = last_update_time
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['result'] = result
            __props__['start_time'] = start_time
            __props__['state'] = state
            __props__['variants_history'] = variants_history
        super(AgentEnvironmentExperiment, __self__).__init__(
            'gcp-native:dialogflow/v3beta1:AgentEnvironmentExperiment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AgentEnvironmentExperiment':
        """
        Get an existing AgentEnvironmentExperiment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = None
        __props__["definition"] = None
        __props__["description"] = None
        __props__["display_name"] = None
        __props__["end_time"] = None
        __props__["experiment_length"] = None
        __props__["last_update_time"] = None
        __props__["name"] = None
        __props__["result"] = None
        __props__["start_time"] = None
        __props__["state"] = None
        __props__["variants_history"] = None
        return AgentEnvironmentExperiment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of this experiment.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3beta1ExperimentDefinitionResponse']:
        """
        The definition of the experiment.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The human-readable description of the experiment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        End time of this experiment.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="experimentLength")
    def experiment_length(self) -> pulumi.Output[str]:
        """
        Maximum number of days to run the experiment. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days.
        """
        return pulumi.get(self, "experiment_length")

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> pulumi.Output[str]:
        """
        Last update time of this experiment.
        """
        return pulumi.get(self, "last_update_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the experiment. Format: projects//locations//agents//environments//experiments/..
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3beta1ExperimentResultResponse']:
        """
        Inference result of the experiment.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        Start time of this experiment.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the experiment. Transition triggered by Expriments.StartExperiment: PENDING->RUNNING. Transition triggered by Expriments.CancelExperiment: PENDING->CANCELLED or RUNNING->CANCELLED.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="variantsHistory")
    def variants_history(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowCxV3beta1VariantsHistoryResponse']]:
        """
        The history of updates to the experiment variants.
        """
        return pulumi.get(self, "variants_history")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

