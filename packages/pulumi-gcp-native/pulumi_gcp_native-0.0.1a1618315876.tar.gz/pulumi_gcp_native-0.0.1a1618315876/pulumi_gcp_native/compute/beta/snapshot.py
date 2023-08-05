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

__all__ = ['Snapshot']


class Snapshot(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_created: Optional[pulumi.Input[bool]] = None,
                 chain_name: Optional[pulumi.Input[str]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_size_gb: Optional[pulumi.Input[str]] = None,
                 download_bytes: Optional[pulumi.Input[str]] = None,
                 guest_flush: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 label_fingerprint: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 license_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 licenses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location_hint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 satisfies_pzs: Optional[pulumi.Input[bool]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 snapshot: Optional[pulumi.Input[str]] = None,
                 snapshot_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
                 source_disk: Optional[pulumi.Input[str]] = None,
                 source_disk_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
                 source_disk_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 storage_bytes: Optional[pulumi.Input[str]] = None,
                 storage_bytes_status: Optional[pulumi.Input[str]] = None,
                 storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a snapshot in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_created: [Output Only] Set to true if snapshots are automatically created by applying resource policy on the target disk.
        :param pulumi.Input[str] chain_name: Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] disk_size_gb: [Output Only] Size of the source disk, specified in GB.
        :param pulumi.Input[str] download_bytes: [Output Only] Number of bytes downloaded to restore a snapshot to a disk.
        :param pulumi.Input[bool] guest_flush: [Input Only] Whether to attempt an application consistent snapshot by informing the OS to prepare for the snapshot process. Currently only supported on Windows instances using the Volume Shadow Copy Service (VSS).
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output Only] Type of the resource. Always compute#snapshot for Snapshot resources.
        :param pulumi.Input[str] label_fingerprint: A fingerprint for the labels being applied to this snapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet.
               
               To see the latest fingerprint, make a get() request to retrieve a snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] license_codes: [Output Only] Integer license codes indicating which licenses are attached to this snapshot.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] licenses: [Output Only] A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses attached (such as a Windows image).
        :param pulumi.Input[str] location_hint: An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[bool] satisfies_pzs: [Output Only] Reserved for future use.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']] snapshot_encryption_key: Encrypts the snapshot using a customer-supplied encryption key.
               
               After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request.
               
               Customer-supplied encryption keys do not protect access to metadata of the snapshot.
               
               If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
        :param pulumi.Input[str] source_disk: The source disk used to create this snapshot.
        :param pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']] source_disk_encryption_key: The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
        :param pulumi.Input[str] source_disk_id: [Output Only] The ID value of the disk used to create this snapshot. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given disk name.
        :param pulumi.Input[str] status: [Output Only] The status of the snapshot. This can be CREATING, DELETING, FAILED, READY, or UPLOADING.
        :param pulumi.Input[str] storage_bytes: [Output Only] A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot creation/deletion.
        :param pulumi.Input[str] storage_bytes_status: [Output Only] An indicator whether storageBytes is in a stable state or it is being adjusted as a result of shared storage reallocation. This status can either be UPDATING, meaning the size of the snapshot is being updated, or UP_TO_DATE, meaning the size of the snapshot is up-to-date.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_locations: Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
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

            __props__['auto_created'] = auto_created
            __props__['chain_name'] = chain_name
            __props__['creation_timestamp'] = creation_timestamp
            __props__['description'] = description
            __props__['disk_size_gb'] = disk_size_gb
            __props__['download_bytes'] = download_bytes
            __props__['guest_flush'] = guest_flush
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['label_fingerprint'] = label_fingerprint
            __props__['labels'] = labels
            __props__['license_codes'] = license_codes
            __props__['licenses'] = licenses
            __props__['location_hint'] = location_hint
            __props__['name'] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['satisfies_pzs'] = satisfies_pzs
            __props__['self_link'] = self_link
            if snapshot is None and not opts.urn:
                raise TypeError("Missing required property 'snapshot'")
            __props__['snapshot'] = snapshot
            __props__['snapshot_encryption_key'] = snapshot_encryption_key
            __props__['source_disk'] = source_disk
            __props__['source_disk_encryption_key'] = source_disk_encryption_key
            __props__['source_disk_id'] = source_disk_id
            __props__['status'] = status
            __props__['storage_bytes'] = storage_bytes
            __props__['storage_bytes_status'] = storage_bytes_status
            __props__['storage_locations'] = storage_locations
        super(Snapshot, __self__).__init__(
            'gcp-native:compute/beta:Snapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Snapshot':
        """
        Get an existing Snapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auto_created"] = None
        __props__["chain_name"] = None
        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["disk_size_gb"] = None
        __props__["download_bytes"] = None
        __props__["guest_flush"] = None
        __props__["kind"] = None
        __props__["label_fingerprint"] = None
        __props__["labels"] = None
        __props__["license_codes"] = None
        __props__["licenses"] = None
        __props__["location_hint"] = None
        __props__["name"] = None
        __props__["satisfies_pzs"] = None
        __props__["self_link"] = None
        __props__["snapshot_encryption_key"] = None
        __props__["source_disk"] = None
        __props__["source_disk_encryption_key"] = None
        __props__["source_disk_id"] = None
        __props__["status"] = None
        __props__["storage_bytes"] = None
        __props__["storage_bytes_status"] = None
        __props__["storage_locations"] = None
        return Snapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoCreated")
    def auto_created(self) -> pulumi.Output[bool]:
        """
        [Output Only] Set to true if snapshots are automatically created by applying resource policy on the target disk.
        """
        return pulumi.get(self, "auto_created")

    @property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> pulumi.Output[str]:
        """
        Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
        """
        return pulumi.get(self, "chain_name")

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
    @pulumi.getter(name="downloadBytes")
    def download_bytes(self) -> pulumi.Output[str]:
        """
        [Output Only] Number of bytes downloaded to restore a snapshot to a disk.
        """
        return pulumi.get(self, "download_bytes")

    @property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> pulumi.Output[bool]:
        """
        [Input Only] Whether to attempt an application consistent snapshot by informing the OS to prepare for the snapshot process. Currently only supported on Windows instances using the Volume Shadow Copy Service (VSS).
        """
        return pulumi.get(self, "guest_flush")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] Type of the resource. Always compute#snapshot for Snapshot resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[str]:
        """
        A fingerprint for the labels being applied to this snapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet.

        To see the latest fingerprint, make a get() request to retrieve a snapshot.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="licenseCodes")
    def license_codes(self) -> pulumi.Output[Sequence[str]]:
        """
        [Output Only] Integer license codes indicating which licenses are attached to this snapshot.
        """
        return pulumi.get(self, "license_codes")

    @property
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence[str]]:
        """
        [Output Only] A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses attached (such as a Windows image).
        """
        return pulumi.get(self, "licenses")

    @property
    @pulumi.getter(name="locationHint")
    def location_hint(self) -> pulumi.Output[str]:
        """
        An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
        """
        return pulumi.get(self, "location_hint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

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
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(self) -> pulumi.Output['outputs.CustomerEncryptionKeyResponse']:
        """
        Encrypts the snapshot using a customer-supplied encryption key.

        After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request.

        Customer-supplied encryption keys do not protect access to metadata of the snapshot.

        If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
        """
        return pulumi.get(self, "snapshot_encryption_key")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[str]:
        """
        The source disk used to create this snapshot.
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> pulumi.Output['outputs.CustomerEncryptionKeyResponse']:
        """
        The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_disk_encryption_key")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> pulumi.Output[str]:
        """
        [Output Only] The ID value of the disk used to create this snapshot. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given disk name.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        [Output Only] The status of the snapshot. This can be CREATING, DELETING, FAILED, READY, or UPLOADING.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> pulumi.Output[str]:
        """
        [Output Only] A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot creation/deletion.
        """
        return pulumi.get(self, "storage_bytes")

    @property
    @pulumi.getter(name="storageBytesStatus")
    def storage_bytes_status(self) -> pulumi.Output[str]:
        """
        [Output Only] An indicator whether storageBytes is in a stable state or it is being adjusted as a result of shared storage reallocation. This status can either be UPDATING, meaning the size of the snapshot is being updated, or UP_TO_DATE, meaning the size of the snapshot is up-to-date.
        """
        return pulumi.get(self, "storage_bytes_status")

    @property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> pulumi.Output[Sequence[str]]:
        """
        Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        """
        return pulumi.get(self, "storage_locations")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

