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

__all__ = ['Glossary']


class Glossary(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 glossaries_id: Optional[pulumi.Input[str]] = None,
                 input_config: Optional[pulumi.Input[pulumi.InputType['GlossaryInputConfigArgs']]] = None,
                 language_codes_set: Optional[pulumi.Input[pulumi.InputType['LanguageCodesSetArgs']]] = None,
                 language_pair: Optional[pulumi.Input[pulumi.InputType['LanguageCodePairArgs']]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a glossary and returns the long-running operation. Returns NOT_FOUND, if the project doesn't exist.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GlossaryInputConfigArgs']] input_config: Required. Provides examples to build the glossary from. Total glossary must not exceed 10M Unicode codepoints.
        :param pulumi.Input[pulumi.InputType['LanguageCodesSetArgs']] language_codes_set: Used with equivalent term set glossaries.
        :param pulumi.Input[pulumi.InputType['LanguageCodePairArgs']] language_pair: Used with unidirectional glossaries.
        :param pulumi.Input[str] name: Required. The resource name of the glossary. Glossary names have the form `projects/{project-number-or-id}/locations/{location-id}/glossaries/{glossary-id}`.
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

            if glossaries_id is None and not opts.urn:
                raise TypeError("Missing required property 'glossaries_id'")
            __props__['glossaries_id'] = glossaries_id
            __props__['input_config'] = input_config
            __props__['language_codes_set'] = language_codes_set
            __props__['language_pair'] = language_pair
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['end_time'] = None
            __props__['entry_count'] = None
            __props__['submit_time'] = None
        super(Glossary, __self__).__init__(
            'gcp-native:translate/v3beta1:Glossary',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Glossary':
        """
        Get an existing Glossary resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["end_time"] = None
        __props__["entry_count"] = None
        __props__["input_config"] = None
        __props__["language_codes_set"] = None
        __props__["language_pair"] = None
        __props__["name"] = None
        __props__["submit_time"] = None
        return Glossary(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        When the glossary creation was finished.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="entryCount")
    def entry_count(self) -> pulumi.Output[int]:
        """
        The number of entries defined in the glossary.
        """
        return pulumi.get(self, "entry_count")

    @property
    @pulumi.getter(name="inputConfig")
    def input_config(self) -> pulumi.Output['outputs.GlossaryInputConfigResponse']:
        """
        Required. Provides examples to build the glossary from. Total glossary must not exceed 10M Unicode codepoints.
        """
        return pulumi.get(self, "input_config")

    @property
    @pulumi.getter(name="languageCodesSet")
    def language_codes_set(self) -> pulumi.Output['outputs.LanguageCodesSetResponse']:
        """
        Used with equivalent term set glossaries.
        """
        return pulumi.get(self, "language_codes_set")

    @property
    @pulumi.getter(name="languagePair")
    def language_pair(self) -> pulumi.Output['outputs.LanguageCodePairResponse']:
        """
        Used with unidirectional glossaries.
        """
        return pulumi.get(self, "language_pair")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The resource name of the glossary. Glossary names have the form `projects/{project-number-or-id}/locations/{location-id}/glossaries/{glossary-id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="submitTime")
    def submit_time(self) -> pulumi.Output[str]:
        """
        When CreateGlossary was called.
        """
        return pulumi.get(self, "submit_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

