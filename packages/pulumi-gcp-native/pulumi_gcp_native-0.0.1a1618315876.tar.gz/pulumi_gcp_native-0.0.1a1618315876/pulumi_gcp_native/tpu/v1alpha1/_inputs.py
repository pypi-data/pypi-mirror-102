# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'SchedulingConfigArgs',
]

@pulumi.input_type
class SchedulingConfigArgs:
    def __init__(__self__, *,
                 preemptible: Optional[pulumi.Input[bool]] = None,
                 reserved: Optional[pulumi.Input[bool]] = None):
        """
        Sets the scheduling options for this node.
        :param pulumi.Input[bool] preemptible: Defines whether the node is preemptible.
        :param pulumi.Input[bool] reserved: Whether the node is created under a reservation.
        """
        if preemptible is not None:
            pulumi.set(__self__, "preemptible", preemptible)
        if reserved is not None:
            pulumi.set(__self__, "reserved", reserved)

    @property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines whether the node is preemptible.
        """
        return pulumi.get(self, "preemptible")

    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "preemptible", value)

    @property
    @pulumi.getter
    def reserved(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the node is created under a reservation.
        """
        return pulumi.get(self, "reserved")

    @reserved.setter
    def reserved(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reserved", value)


