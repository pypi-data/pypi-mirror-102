# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .alert_policy import *
from .group import *
from .metric_descriptor import *
from .notification_channel import *
from .service import *
from .service_service_level_objective import *
from .uptime_check_config import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "gcp-native:monitoring/v3:AlertPolicy":
                return AlertPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:monitoring/v3:Group":
                return Group(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:monitoring/v3:MetricDescriptor":
                return MetricDescriptor(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:monitoring/v3:NotificationChannel":
                return NotificationChannel(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:monitoring/v3:Service":
                return Service(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:monitoring/v3:ServiceServiceLevelObjective":
                return ServiceServiceLevelObjective(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:monitoring/v3:UptimeCheckConfig":
                return UptimeCheckConfig(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp-native", "monitoring/v3", _module_instance)

_register_module()
