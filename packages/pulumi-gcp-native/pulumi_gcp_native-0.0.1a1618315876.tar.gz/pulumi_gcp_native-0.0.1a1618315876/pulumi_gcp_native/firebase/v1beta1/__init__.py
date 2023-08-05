# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .android_app import *
from .ios_app import *
from .web_app import *

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "gcp-native:firebase/v1beta1:AndroidApp":
                return AndroidApp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:firebase/v1beta1:IosApp":
                return IosApp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:firebase/v1beta1:WebApp":
                return WebApp(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp-native", "firebase/v1beta1", _module_instance)

_register_module()
