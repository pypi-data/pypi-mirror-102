# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['DatasetAnnotationStore']


class DatasetAnnotationStore(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation_stores_id: Optional[pulumi.Input[str]] = None,
                 datasets_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new Annotation store within the parent dataset.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User-supplied key-value pairs used to organize Annotation stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        :param pulumi.Input[str] name: Resource name of the Annotation store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}`.
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

            if annotation_stores_id is None and not opts.urn:
                raise TypeError("Missing required property 'annotation_stores_id'")
            __props__['annotation_stores_id'] = annotation_stores_id
            if datasets_id is None and not opts.urn:
                raise TypeError("Missing required property 'datasets_id'")
            __props__['datasets_id'] = datasets_id
            __props__['labels'] = labels
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
        super(DatasetAnnotationStore, __self__).__init__(
            'gcp-native:healthcare/v1beta1:DatasetAnnotationStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatasetAnnotationStore':
        """
        Get an existing DatasetAnnotationStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["labels"] = None
        __props__["name"] = None
        return DatasetAnnotationStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. User-supplied key-value pairs used to organize Annotation stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the Annotation store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}`.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

