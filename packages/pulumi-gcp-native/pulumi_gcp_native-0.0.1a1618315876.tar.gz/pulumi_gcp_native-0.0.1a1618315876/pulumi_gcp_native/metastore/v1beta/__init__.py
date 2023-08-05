# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .service import *
from .service_backup import *
from .service_iam_policy import *
from .service_metadata_import import *
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
            if typ == "gcp-native:metastore/v1beta:Service":
                return Service(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:metastore/v1beta:ServiceBackup":
                return ServiceBackup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:metastore/v1beta:ServiceIamPolicy":
                return ServiceIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:metastore/v1beta:ServiceMetadataImport":
                return ServiceMetadataImport(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp-native", "metastore/v1beta", _module_instance)

_register_module()
