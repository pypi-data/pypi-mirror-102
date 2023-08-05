# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['ObjectIamPolicy']


class ObjectIamPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Updates an IAM policy for the specified object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] bindings: An association between a role, which comes with a set of permissions, and members who may assume that role.
        :param pulumi.Input[str] etag: HTTP 1.1  Entity tag for the policy.
        :param pulumi.Input[str] kind: The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        :param pulumi.Input[str] resource_id: The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        :param pulumi.Input[int] version: The IAM policy format version.
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

            __props__['bindings'] = bindings
            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            __props__['etag'] = etag
            __props__['kind'] = kind
            if object is None and not opts.urn:
                raise TypeError("Missing required property 'object'")
            __props__['object'] = object
            __props__['resource_id'] = resource_id
            __props__['version'] = version
        super(ObjectIamPolicy, __self__).__init__(
            'gcp-native:storage/v1:ObjectIamPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ObjectIamPolicy':
        """
        Get an existing ObjectIamPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bindings"] = None
        __props__["etag"] = None
        __props__["kind"] = None
        __props__["resource_id"] = None
        __props__["version"] = None
        return ObjectIamPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bindings(self) -> pulumi.Output[Sequence[Mapping[str, str]]]:
        """
        An association between a role, which comes with a set of permissions, and members who may assume that role.
        """
        return pulumi.get(self, "bindings")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        HTTP 1.1  Entity tag for the policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The IAM policy format version.
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

