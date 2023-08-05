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

__all__ = ['DatasetConsentStoreConsentArtifact']


class DatasetConsentStoreConsentArtifact(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 consent_artifacts_id: Optional[pulumi.Input[str]] = None,
                 consent_content_screenshots: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageArgs']]]]] = None,
                 consent_content_version: Optional[pulumi.Input[str]] = None,
                 consent_stores_id: Optional[pulumi.Input[str]] = None,
                 datasets_id: Optional[pulumi.Input[str]] = None,
                 guardian_signature: Optional[pulumi.Input[pulumi.InputType['SignatureArgs']]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_signature: Optional[pulumi.Input[pulumi.InputType['SignatureArgs']]] = None,
                 witness_signature: Optional[pulumi.Input[pulumi.InputType['SignatureArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new Consent artifact in the parent consent store.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageArgs']]]] consent_content_screenshots: Optional. Screenshots, PDFs, or other binary information documenting the user's consent.
        :param pulumi.Input[str] consent_content_version: Optional. An string indicating the version of the consent information shown to the user.
        :param pulumi.Input[pulumi.InputType['SignatureArgs']] guardian_signature: Optional. A signature from a guardian.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version.
        :param pulumi.Input[str] name: Resource name of the Consent artifact, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}`. Cannot be changed after creation.
        :param pulumi.Input[str] user_id: Required. User's UUID provided by the client.
        :param pulumi.Input[pulumi.InputType['SignatureArgs']] user_signature: Optional. User's signature.
        :param pulumi.Input[pulumi.InputType['SignatureArgs']] witness_signature: Optional. A signature from a witness.
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

            if consent_artifacts_id is None and not opts.urn:
                raise TypeError("Missing required property 'consent_artifacts_id'")
            __props__['consent_artifacts_id'] = consent_artifacts_id
            __props__['consent_content_screenshots'] = consent_content_screenshots
            __props__['consent_content_version'] = consent_content_version
            if consent_stores_id is None and not opts.urn:
                raise TypeError("Missing required property 'consent_stores_id'")
            __props__['consent_stores_id'] = consent_stores_id
            if datasets_id is None and not opts.urn:
                raise TypeError("Missing required property 'datasets_id'")
            __props__['datasets_id'] = datasets_id
            __props__['guardian_signature'] = guardian_signature
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['metadata'] = metadata
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['user_id'] = user_id
            __props__['user_signature'] = user_signature
            __props__['witness_signature'] = witness_signature
        super(DatasetConsentStoreConsentArtifact, __self__).__init__(
            'gcp-native:healthcare/v1beta1:DatasetConsentStoreConsentArtifact',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatasetConsentStoreConsentArtifact':
        """
        Get an existing DatasetConsentStoreConsentArtifact resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["consent_content_screenshots"] = None
        __props__["consent_content_version"] = None
        __props__["guardian_signature"] = None
        __props__["metadata"] = None
        __props__["name"] = None
        __props__["user_id"] = None
        __props__["user_signature"] = None
        __props__["witness_signature"] = None
        return DatasetConsentStoreConsentArtifact(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="consentContentScreenshots")
    def consent_content_screenshots(self) -> pulumi.Output[Sequence['outputs.ImageResponse']]:
        """
        Optional. Screenshots, PDFs, or other binary information documenting the user's consent.
        """
        return pulumi.get(self, "consent_content_screenshots")

    @property
    @pulumi.getter(name="consentContentVersion")
    def consent_content_version(self) -> pulumi.Output[str]:
        """
        Optional. An string indicating the version of the consent information shown to the user.
        """
        return pulumi.get(self, "consent_content_version")

    @property
    @pulumi.getter(name="guardianSignature")
    def guardian_signature(self) -> pulumi.Output['outputs.SignatureResponse']:
        """
        Optional. A signature from a guardian.
        """
        return pulumi.get(self, "guardian_signature")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the Consent artifact, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}`. Cannot be changed after creation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        Required. User's UUID provided by the client.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userSignature")
    def user_signature(self) -> pulumi.Output['outputs.SignatureResponse']:
        """
        Optional. User's signature.
        """
        return pulumi.get(self, "user_signature")

    @property
    @pulumi.getter(name="witnessSignature")
    def witness_signature(self) -> pulumi.Output['outputs.SignatureResponse']:
        """
        Optional. A signature from a witness.
        """
        return pulumi.get(self, "witness_signature")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

