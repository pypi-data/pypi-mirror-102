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

__all__ = ['AgentIntent']


class AgentIntent(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 default_response_platforms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_interaction: Optional[pulumi.Input[bool]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 followup_intent_info: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentFollowupIntentInfoArgs']]]]] = None,
                 input_context_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 intents_id: Optional[pulumi.Input[str]] = None,
                 is_fallback: Optional[pulumi.Input[bool]] = None,
                 live_agent_handoff: Optional[pulumi.Input[bool]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 messages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentMessageArgs']]]]] = None,
                 ml_disabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_contexts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2ContextArgs']]]]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentParameterArgs']]]]] = None,
                 parent_followup_intent_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 reset_contexts: Optional[pulumi.Input[bool]] = None,
                 root_followup_intent_name: Optional[pulumi.Input[str]] = None,
                 training_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentTrainingPhraseArgs']]]]] = None,
                 webhook_state: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an intent in the specified agent.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Optional. The name of the action associated with the intent. Note: The action name must not contain whitespaces.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] default_response_platforms: Optional. The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED (i.e. default platform).
        :param pulumi.Input[str] display_name: Required. The name of this intent.
        :param pulumi.Input[bool] end_interaction: Optional. Indicates that this intent ends an interaction. Some integrations (e.g., Actions on Google or Dialogflow phone gateway) use this information to close interaction with an end user. Default is false.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] events: Optional. The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of the contexts must be present in the active user session for an event to trigger this intent. Event names are limited to 150 characters.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentFollowupIntentInfoArgs']]]] followup_intent_info: Read-only. Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only in the output.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] input_context_names: Optional. The list of context names required for this intent to be triggered. Format: `projects//agent/sessions/-/contexts/`.
        :param pulumi.Input[bool] is_fallback: Optional. Indicates whether this is a fallback intent.
        :param pulumi.Input[bool] live_agent_handoff: Optional. Indicates that a live agent should be brought in to handle the interaction with the user. In most cases, when you set this flag to true, you would also want to set end_interaction to true as well. Default is false.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentMessageArgs']]]] messages: Optional. The collection of rich messages corresponding to the `Response` field in the Dialogflow console.
        :param pulumi.Input[bool] ml_disabled: Optional. Indicates whether Machine Learning is disabled for the intent. Note: If `ml_disabled` setting is set to true, then this intent is not taken into account during inference in `ML ONLY` match mode. Also, auto-markup in the UI is turned off.
        :param pulumi.Input[str] name: Optional. The unique identifier of this intent. Required for Intents.UpdateIntent and Intents.BatchUpdateIntents methods. Format: `projects//agent/intents/`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2ContextArgs']]]] output_contexts: Optional. The collection of contexts that are activated when the intent is matched. Context messages in this collection should not set the parameters field. Setting the `lifespan_count` to 0 will reset the context when the intent is matched. Format: `projects//agent/sessions/-/contexts/`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentParameterArgs']]]] parameters: Optional. The collection of parameters associated with the intent.
        :param pulumi.Input[str] parent_followup_intent_name: Read-only after creation. The unique identifier of the parent intent in the chain of followup intents. You can set this field when creating an intent, for example with CreateIntent or BatchUpdateIntents, in order to make this intent a followup intent. It identifies the parent followup intent. Format: `projects//agent/intents/`.
        :param pulumi.Input[int] priority: Optional. The priority of this intent. Higher numbers represent higher priorities. - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the `Normal` priority in the console. - If the supplied value is negative, the intent is ignored in runtime detect intent requests.
        :param pulumi.Input[bool] reset_contexts: Optional. Indicates whether to delete all contexts in the current session when this intent is matched.
        :param pulumi.Input[str] root_followup_intent_name: Read-only. The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents chain for this intent. We populate this field only in the output. Format: `projects//agent/intents/`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2IntentTrainingPhraseArgs']]]] training_phrases: Optional. The collection of examples that the agent is trained on.
        :param pulumi.Input[str] webhook_state: Optional. Indicates whether webhooks are enabled for the intent.
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

            __props__['action'] = action
            __props__['default_response_platforms'] = default_response_platforms
            __props__['display_name'] = display_name
            __props__['end_interaction'] = end_interaction
            __props__['events'] = events
            __props__['followup_intent_info'] = followup_intent_info
            __props__['input_context_names'] = input_context_names
            if intents_id is None and not opts.urn:
                raise TypeError("Missing required property 'intents_id'")
            __props__['intents_id'] = intents_id
            __props__['is_fallback'] = is_fallback
            __props__['live_agent_handoff'] = live_agent_handoff
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['messages'] = messages
            __props__['ml_disabled'] = ml_disabled
            __props__['name'] = name
            __props__['output_contexts'] = output_contexts
            __props__['parameters'] = parameters
            __props__['parent_followup_intent_name'] = parent_followup_intent_name
            __props__['priority'] = priority
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['reset_contexts'] = reset_contexts
            __props__['root_followup_intent_name'] = root_followup_intent_name
            __props__['training_phrases'] = training_phrases
            __props__['webhook_state'] = webhook_state
        super(AgentIntent, __self__).__init__(
            'gcp-native:dialogflow/v2:AgentIntent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AgentIntent':
        """
        Get an existing AgentIntent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["action"] = None
        __props__["default_response_platforms"] = None
        __props__["display_name"] = None
        __props__["end_interaction"] = None
        __props__["events"] = None
        __props__["followup_intent_info"] = None
        __props__["input_context_names"] = None
        __props__["is_fallback"] = None
        __props__["live_agent_handoff"] = None
        __props__["messages"] = None
        __props__["ml_disabled"] = None
        __props__["name"] = None
        __props__["output_contexts"] = None
        __props__["parameters"] = None
        __props__["parent_followup_intent_name"] = None
        __props__["priority"] = None
        __props__["reset_contexts"] = None
        __props__["root_followup_intent_name"] = None
        __props__["training_phrases"] = None
        __props__["webhook_state"] = None
        return AgentIntent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        Optional. The name of the action associated with the intent. Note: The action name must not contain whitespaces.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="defaultResponsePlatforms")
    def default_response_platforms(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED (i.e. default platform).
        """
        return pulumi.get(self, "default_response_platforms")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The name of this intent.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endInteraction")
    def end_interaction(self) -> pulumi.Output[bool]:
        """
        Optional. Indicates that this intent ends an interaction. Some integrations (e.g., Actions on Google or Dialogflow phone gateway) use this information to close interaction with an end user. Default is false.
        """
        return pulumi.get(self, "end_interaction")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of the contexts must be present in the active user session for an event to trigger this intent. Event names are limited to 150 characters.
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="followupIntentInfo")
    def followup_intent_info(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowV2IntentFollowupIntentInfoResponse']]:
        """
        Read-only. Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only in the output.
        """
        return pulumi.get(self, "followup_intent_info")

    @property
    @pulumi.getter(name="inputContextNames")
    def input_context_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. The list of context names required for this intent to be triggered. Format: `projects//agent/sessions/-/contexts/`.
        """
        return pulumi.get(self, "input_context_names")

    @property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> pulumi.Output[bool]:
        """
        Optional. Indicates whether this is a fallback intent.
        """
        return pulumi.get(self, "is_fallback")

    @property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> pulumi.Output[bool]:
        """
        Optional. Indicates that a live agent should be brought in to handle the interaction with the user. In most cases, when you set this flag to true, you would also want to set end_interaction to true as well. Default is false.
        """
        return pulumi.get(self, "live_agent_handoff")

    @property
    @pulumi.getter
    def messages(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowV2IntentMessageResponse']]:
        """
        Optional. The collection of rich messages corresponding to the `Response` field in the Dialogflow console.
        """
        return pulumi.get(self, "messages")

    @property
    @pulumi.getter(name="mlDisabled")
    def ml_disabled(self) -> pulumi.Output[bool]:
        """
        Optional. Indicates whether Machine Learning is disabled for the intent. Note: If `ml_disabled` setting is set to true, then this intent is not taken into account during inference in `ML ONLY` match mode. Also, auto-markup in the UI is turned off.
        """
        return pulumi.get(self, "ml_disabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Optional. The unique identifier of this intent. Required for Intents.UpdateIntent and Intents.BatchUpdateIntents methods. Format: `projects//agent/intents/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputContexts")
    def output_contexts(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowV2ContextResponse']]:
        """
        Optional. The collection of contexts that are activated when the intent is matched. Context messages in this collection should not set the parameters field. Setting the `lifespan_count` to 0 will reset the context when the intent is matched. Format: `projects//agent/sessions/-/contexts/`.
        """
        return pulumi.get(self, "output_contexts")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowV2IntentParameterResponse']]:
        """
        Optional. The collection of parameters associated with the intent.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> pulumi.Output[str]:
        """
        Read-only after creation. The unique identifier of the parent intent in the chain of followup intents. You can set this field when creating an intent, for example with CreateIntent or BatchUpdateIntents, in order to make this intent a followup intent. It identifies the parent followup intent. Format: `projects//agent/intents/`.
        """
        return pulumi.get(self, "parent_followup_intent_name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Optional. The priority of this intent. Higher numbers represent higher priorities. - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the `Normal` priority in the console. - If the supplied value is negative, the intent is ignored in runtime detect intent requests.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="resetContexts")
    def reset_contexts(self) -> pulumi.Output[bool]:
        """
        Optional. Indicates whether to delete all contexts in the current session when this intent is matched.
        """
        return pulumi.get(self, "reset_contexts")

    @property
    @pulumi.getter(name="rootFollowupIntentName")
    def root_followup_intent_name(self) -> pulumi.Output[str]:
        """
        Read-only. The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents chain for this intent. We populate this field only in the output. Format: `projects//agent/intents/`.
        """
        return pulumi.get(self, "root_followup_intent_name")

    @property
    @pulumi.getter(name="trainingPhrases")
    def training_phrases(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowV2IntentTrainingPhraseResponse']]:
        """
        Optional. The collection of examples that the agent is trained on.
        """
        return pulumi.get(self, "training_phrases")

    @property
    @pulumi.getter(name="webhookState")
    def webhook_state(self) -> pulumi.Output[str]:
        """
        Optional. Indicates whether webhooks are enabled for the intent.
        """
        return pulumi.get(self, "webhook_state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

