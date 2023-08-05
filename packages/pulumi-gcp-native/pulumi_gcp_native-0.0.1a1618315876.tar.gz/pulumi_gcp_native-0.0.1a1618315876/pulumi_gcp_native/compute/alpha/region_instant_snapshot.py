# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['RegionInstantSnapshot']


class RegionInstantSnapshot(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_size_gb: Optional[pulumi.Input[str]] = None,
                 guest_flush: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 instant_snapshot: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 label_fingerprint: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 satisfies_pzs: Optional[pulumi.Input[bool]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 self_link_with_id: Optional[pulumi.Input[str]] = None,
                 source_disk: Optional[pulumi.Input[str]] = None,
                 source_disk_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an instant snapshot in the specified region.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] disk_size_gb: [Output Only] Size of the source disk, specified in GB.
        :param pulumi.Input[bool] guest_flush: Whether to attempt an application consistent instant snapshot by informing the OS to prepare for the snapshot process. Currently only supported on Windows instances using the Volume Shadow Copy Service (VSS).
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output Only] Type of the resource. Always compute#instantSnapshot for InstantSnapshot resources.
        :param pulumi.Input[str] label_fingerprint: A fingerprint for the labels being applied to this InstantSnapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet.
               
               To see the latest fingerprint, make a get() request to retrieve a InstantSnapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this InstantSnapshot. These can be later modified by the setLabels method. Label values may be empty.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] region: [Output Only] URL of the region where the instant snapshot resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        :param pulumi.Input[bool] satisfies_pzs: [Output Only] Reserved for future use.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[str] self_link_with_id: [Output Only] Server-defined URL for this resource's resource id.
        :param pulumi.Input[str] source_disk: URL of the source disk used to create this instant snapshot. Note that the source disk must be in the same zone/region as the instant snapshot to be created. This can be a full or valid partial URL. For example, the following are valid values:  
               - https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk  
               - https://www.googleapis.com/compute/v1/projects/project/regions/region/disks/disk  
               - projects/project/zones/zone/disks/disk  
               - projects/project/regions/region/disks/disk  
               - zones/zone/disks/disk  
               - regions/region/disks/disk
        :param pulumi.Input[str] source_disk_id: [Output Only] The ID value of the disk used to create this InstantSnapshot. This value may be used to determine whether the InstantSnapshot was taken from the current or a previous instance of a given disk name.
        :param pulumi.Input[str] status: [Output Only] The status of the instantSnapshot. This can be CREATING, DELETING, FAILED, or READY.
        :param pulumi.Input[str] zone: [Output Only] URL of the zone where the instant snapshot resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
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

            __props__['creation_timestamp'] = creation_timestamp
            __props__['description'] = description
            __props__['disk_size_gb'] = disk_size_gb
            __props__['guest_flush'] = guest_flush
            __props__['id'] = id
            if instant_snapshot is None and not opts.urn:
                raise TypeError("Missing required property 'instant_snapshot'")
            __props__['instant_snapshot'] = instant_snapshot
            __props__['kind'] = kind
            __props__['label_fingerprint'] = label_fingerprint
            __props__['labels'] = labels
            __props__['name'] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            __props__['satisfies_pzs'] = satisfies_pzs
            __props__['self_link'] = self_link
            __props__['self_link_with_id'] = self_link_with_id
            __props__['source_disk'] = source_disk
            __props__['source_disk_id'] = source_disk_id
            __props__['status'] = status
            __props__['zone'] = zone
        super(RegionInstantSnapshot, __self__).__init__(
            'gcp-native:compute/alpha:RegionInstantSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegionInstantSnapshot':
        """
        Get an existing RegionInstantSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["disk_size_gb"] = None
        __props__["guest_flush"] = None
        __props__["kind"] = None
        __props__["label_fingerprint"] = None
        __props__["labels"] = None
        __props__["name"] = None
        __props__["region"] = None
        __props__["satisfies_pzs"] = None
        __props__["self_link"] = None
        __props__["self_link_with_id"] = None
        __props__["source_disk"] = None
        __props__["source_disk_id"] = None
        __props__["status"] = None
        __props__["zone"] = None
        return RegionInstantSnapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        [Output Only] Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> pulumi.Output[str]:
        """
        [Output Only] Size of the source disk, specified in GB.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> pulumi.Output[bool]:
        """
        Whether to attempt an application consistent instant snapshot by informing the OS to prepare for the snapshot process. Currently only supported on Windows instances using the Volume Shadow Copy Service (VSS).
        """
        return pulumi.get(self, "guest_flush")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] Type of the resource. Always compute#instantSnapshot for InstantSnapshot resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[str]:
        """
        A fingerprint for the labels being applied to this InstantSnapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet.

        To see the latest fingerprint, make a get() request to retrieve a InstantSnapshot.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels to apply to this InstantSnapshot. These can be later modified by the setLabels method. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] URL of the region where the instant snapshot resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[bool]:
        """
        [Output Only] Reserved for future use.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for this resource's resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[str]:
        """
        URL of the source disk used to create this instant snapshot. Note that the source disk must be in the same zone/region as the instant snapshot to be created. This can be a full or valid partial URL. For example, the following are valid values:  
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk  
        - https://www.googleapis.com/compute/v1/projects/project/regions/region/disks/disk  
        - projects/project/zones/zone/disks/disk  
        - projects/project/regions/region/disks/disk  
        - zones/zone/disks/disk  
        - regions/region/disks/disk
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> pulumi.Output[str]:
        """
        [Output Only] The ID value of the disk used to create this InstantSnapshot. This value may be used to determine whether the InstantSnapshot was taken from the current or a previous instance of a given disk name.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        [Output Only] The status of the instantSnapshot. This can be CREATING, DELETING, FAILED, or READY.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        [Output Only] URL of the zone where the instant snapshot resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

