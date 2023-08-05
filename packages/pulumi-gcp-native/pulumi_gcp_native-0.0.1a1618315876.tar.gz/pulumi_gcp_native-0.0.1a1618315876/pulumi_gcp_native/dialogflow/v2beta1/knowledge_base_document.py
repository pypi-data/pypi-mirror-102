# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = ['KnowledgeBaseDocument']


class KnowledgeBaseDocument(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_uri: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 documents_id: Optional[pulumi.Input[str]] = None,
                 enable_auto_reload: Optional[pulumi.Input[bool]] = None,
                 knowledge_bases_id: Optional[pulumi.Input[str]] = None,
                 knowledge_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 raw_content: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new document. Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The raw content of the document. This field is only permitted for EXTRACTIVE_QA and FAQ knowledge types. Note: This field is in the process of being deprecated, please use raw_content instead.
        :param pulumi.Input[str] content_uri: The URI where the file content is located. For documents stored in Google Cloud Storage, these URIs must have the form `gs:///`. NOTE: External URLs must correspond to public webpages, i.e., they must be indexed by Google Search. In particular, URLs for showing documents in Google Cloud Storage (i.e. the URL in your browser) are not supported. Instead use the `gs://` format URI described above.
        :param pulumi.Input[str] display_name: Required. The display name of the document. The name must be 1024 bytes or less; otherwise, the creation request fails.
        :param pulumi.Input[bool] enable_auto_reload: Optional. If true, we try to automatically reload the document every day (at a time picked by the system). If false or unspecified, we don't try to automatically reload the document. Currently you can only enable automatic reload for documents sourced from a public url, see `source` field for the source types. Reload status can be tracked in `latest_reload_status`. If a reload fails, we will keep the document unchanged. If a reload fails with internal errors, the system will try to reload the document on the next day. If a reload fails with non-retriable errors (e.g. PERMISION_DENIED), the system will not try to reload the document anymore. You need to manually reload the document successfully by calling `ReloadDocument` and clear the errors.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] knowledge_types: Required. The knowledge type of document content.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Optional. Metadata for the document. The metadata supports arbitrary key-value pairs. Suggested use cases include storing a document's title, an external URL distinct from the document's content_uri, etc. The max size of a `key` or a `value` of the metadata is 1024 bytes.
        :param pulumi.Input[str] mime_type: Required. The MIME type of this document.
        :param pulumi.Input[str] name: Optional. The document resource name. The name must be empty when creating a document. Format: `projects//locations//knowledgeBases//documents/`.
        :param pulumi.Input[str] raw_content: The raw content of the document. This field is only permitted for EXTRACTIVE_QA and FAQ knowledge types.
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

            __props__['content'] = content
            __props__['content_uri'] = content_uri
            __props__['display_name'] = display_name
            if documents_id is None and not opts.urn:
                raise TypeError("Missing required property 'documents_id'")
            __props__['documents_id'] = documents_id
            __props__['enable_auto_reload'] = enable_auto_reload
            if knowledge_bases_id is None and not opts.urn:
                raise TypeError("Missing required property 'knowledge_bases_id'")
            __props__['knowledge_bases_id'] = knowledge_bases_id
            __props__['knowledge_types'] = knowledge_types
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['metadata'] = metadata
            __props__['mime_type'] = mime_type
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['raw_content'] = raw_content
            __props__['latest_reload_status'] = None
        super(KnowledgeBaseDocument, __self__).__init__(
            'gcp-native:dialogflow/v2beta1:KnowledgeBaseDocument',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KnowledgeBaseDocument':
        """
        Get an existing KnowledgeBaseDocument resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["content"] = None
        __props__["content_uri"] = None
        __props__["display_name"] = None
        __props__["enable_auto_reload"] = None
        __props__["knowledge_types"] = None
        __props__["latest_reload_status"] = None
        __props__["metadata"] = None
        __props__["mime_type"] = None
        __props__["name"] = None
        __props__["raw_content"] = None
        return KnowledgeBaseDocument(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        The raw content of the document. This field is only permitted for EXTRACTIVE_QA and FAQ knowledge types. Note: This field is in the process of being deprecated, please use raw_content instead.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentUri")
    def content_uri(self) -> pulumi.Output[str]:
        """
        The URI where the file content is located. For documents stored in Google Cloud Storage, these URIs must have the form `gs:///`. NOTE: External URLs must correspond to public webpages, i.e., they must be indexed by Google Search. In particular, URLs for showing documents in Google Cloud Storage (i.e. the URL in your browser) are not supported. Instead use the `gs://` format URI described above.
        """
        return pulumi.get(self, "content_uri")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The display name of the document. The name must be 1024 bytes or less; otherwise, the creation request fails.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableAutoReload")
    def enable_auto_reload(self) -> pulumi.Output[bool]:
        """
        Optional. If true, we try to automatically reload the document every day (at a time picked by the system). If false or unspecified, we don't try to automatically reload the document. Currently you can only enable automatic reload for documents sourced from a public url, see `source` field for the source types. Reload status can be tracked in `latest_reload_status`. If a reload fails, we will keep the document unchanged. If a reload fails with internal errors, the system will try to reload the document on the next day. If a reload fails with non-retriable errors (e.g. PERMISION_DENIED), the system will not try to reload the document anymore. You need to manually reload the document successfully by calling `ReloadDocument` and clear the errors.
        """
        return pulumi.get(self, "enable_auto_reload")

    @property
    @pulumi.getter(name="knowledgeTypes")
    def knowledge_types(self) -> pulumi.Output[Sequence[str]]:
        """
        Required. The knowledge type of document content.
        """
        return pulumi.get(self, "knowledge_types")

    @property
    @pulumi.getter(name="latestReloadStatus")
    def latest_reload_status(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2beta1DocumentReloadStatusResponse']:
        """
        The time and status of the latest reload. This reload may have been triggered automatically or manually and may not have succeeded.
        """
        return pulumi.get(self, "latest_reload_status")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Metadata for the document. The metadata supports arbitrary key-value pairs. Suggested use cases include storing a document's title, an external URL distinct from the document's content_uri, etc. The max size of a `key` or a `value` of the metadata is 1024 bytes.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> pulumi.Output[str]:
        """
        Required. The MIME type of this document.
        """
        return pulumi.get(self, "mime_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Optional. The document resource name. The name must be empty when creating a document. Format: `projects//locations//knowledgeBases//documents/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rawContent")
    def raw_content(self) -> pulumi.Output[str]:
        """
        The raw content of the document. This field is only permitted for EXTRACTIVE_QA and FAQ knowledge types.
        """
        return pulumi.get(self, "raw_content")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

