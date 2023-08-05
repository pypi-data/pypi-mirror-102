# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'CapacityArgs',
    'DeliveryConfigArgs',
    'PartitionConfigArgs',
    'RetentionConfigArgs',
]

@pulumi.input_type
class CapacityArgs:
    def __init__(__self__, *,
                 publish_mib_per_sec: Optional[pulumi.Input[int]] = None,
                 subscribe_mib_per_sec: Optional[pulumi.Input[int]] = None):
        """
        The throughput capacity configuration for each partition.
        :param pulumi.Input[int] publish_mib_per_sec: Publish throughput capacity per partition in MiB/s. Must be >= 4 and <= 16.
        :param pulumi.Input[int] subscribe_mib_per_sec: Subscribe throughput capacity per partition in MiB/s. Must be >= 4 and <= 32.
        """
        if publish_mib_per_sec is not None:
            pulumi.set(__self__, "publish_mib_per_sec", publish_mib_per_sec)
        if subscribe_mib_per_sec is not None:
            pulumi.set(__self__, "subscribe_mib_per_sec", subscribe_mib_per_sec)

    @property
    @pulumi.getter(name="publishMibPerSec")
    def publish_mib_per_sec(self) -> Optional[pulumi.Input[int]]:
        """
        Publish throughput capacity per partition in MiB/s. Must be >= 4 and <= 16.
        """
        return pulumi.get(self, "publish_mib_per_sec")

    @publish_mib_per_sec.setter
    def publish_mib_per_sec(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "publish_mib_per_sec", value)

    @property
    @pulumi.getter(name="subscribeMibPerSec")
    def subscribe_mib_per_sec(self) -> Optional[pulumi.Input[int]]:
        """
        Subscribe throughput capacity per partition in MiB/s. Must be >= 4 and <= 32.
        """
        return pulumi.get(self, "subscribe_mib_per_sec")

    @subscribe_mib_per_sec.setter
    def subscribe_mib_per_sec(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "subscribe_mib_per_sec", value)


@pulumi.input_type
class DeliveryConfigArgs:
    def __init__(__self__, *,
                 delivery_requirement: Optional[pulumi.Input[str]] = None):
        """
        The settings for a subscription's message delivery.
        :param pulumi.Input[str] delivery_requirement: The DeliveryRequirement for this subscription.
        """
        if delivery_requirement is not None:
            pulumi.set(__self__, "delivery_requirement", delivery_requirement)

    @property
    @pulumi.getter(name="deliveryRequirement")
    def delivery_requirement(self) -> Optional[pulumi.Input[str]]:
        """
        The DeliveryRequirement for this subscription.
        """
        return pulumi.get(self, "delivery_requirement")

    @delivery_requirement.setter
    def delivery_requirement(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_requirement", value)


@pulumi.input_type
class PartitionConfigArgs:
    def __init__(__self__, *,
                 capacity: Optional[pulumi.Input['CapacityArgs']] = None,
                 count: Optional[pulumi.Input[str]] = None,
                 scale: Optional[pulumi.Input[int]] = None):
        """
        The settings for a topic's partitions.
        :param pulumi.Input['CapacityArgs'] capacity: The capacity configuration.
        :param pulumi.Input[str] count: The number of partitions in the topic. Must be at least 1. Once a topic has been created the number of partitions can be increased but not decreased. Message ordering is not guaranteed across a topic resize. For more information see https://cloud.google.com/pubsub/lite/docs/topics#scaling_capacity
        :param pulumi.Input[int] scale: DEPRECATED: Use capacity instead which can express a superset of configurations. Every partition in the topic is allocated throughput equivalent to `scale` times the standard partition throughput (4 MiB/s). This is also reflected in the cost of this topic; a topic with `scale` of 2 and count of 10 is charged for 20 partitions. This value must be in the range [1,4].
        """
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if count is not None:
            pulumi.set(__self__, "count", count)
        if scale is not None:
            pulumi.set(__self__, "scale", scale)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input['CapacityArgs']]:
        """
        The capacity configuration.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input['CapacityArgs']]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[str]]:
        """
        The number of partitions in the topic. Must be at least 1. Once a topic has been created the number of partitions can be increased but not decreased. Message ordering is not guaranteed across a topic resize. For more information see https://cloud.google.com/pubsub/lite/docs/topics#scaling_capacity
        """
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[int]]:
        """
        DEPRECATED: Use capacity instead which can express a superset of configurations. Every partition in the topic is allocated throughput equivalent to `scale` times the standard partition throughput (4 MiB/s). This is also reflected in the cost of this topic; a topic with `scale` of 2 and count of 10 is charged for 20 partitions. This value must be in the range [1,4].
        """
        return pulumi.get(self, "scale")

    @scale.setter
    def scale(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scale", value)


@pulumi.input_type
class RetentionConfigArgs:
    def __init__(__self__, *,
                 per_partition_bytes: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[str]] = None):
        """
        The settings for a topic's message retention.
        :param pulumi.Input[str] per_partition_bytes: The provisioned storage, in bytes, per partition. If the number of bytes stored in any of the topic's partitions grows beyond this value, older messages will be dropped to make room for newer ones, regardless of the value of `period`.
        :param pulumi.Input[str] period: How long a published message is retained. If unset, messages will be retained as long as the bytes retained for each partition is below `per_partition_bytes`.
        """
        if per_partition_bytes is not None:
            pulumi.set(__self__, "per_partition_bytes", per_partition_bytes)
        if period is not None:
            pulumi.set(__self__, "period", period)

    @property
    @pulumi.getter(name="perPartitionBytes")
    def per_partition_bytes(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioned storage, in bytes, per partition. If the number of bytes stored in any of the topic's partitions grows beyond this value, older messages will be dropped to make room for newer ones, regardless of the value of `period`.
        """
        return pulumi.get(self, "per_partition_bytes")

    @per_partition_bytes.setter
    def per_partition_bytes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "per_partition_bytes", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[str]]:
        """
        How long a published message is retained. If unset, messages will be retained as long as the bytes retained for each partition is below `per_partition_bytes`.
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "period", value)


