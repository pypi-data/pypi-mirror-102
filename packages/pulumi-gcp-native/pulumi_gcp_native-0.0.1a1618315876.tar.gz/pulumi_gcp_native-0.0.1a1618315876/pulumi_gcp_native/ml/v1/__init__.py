# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .job import *
from .job_iam_policy import *
from .model import *
from .model_iam_policy import *
from .model_version import *
from .study import *
from .study_trial import *
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
            if typ == "gcp-native:ml/v1:Job":
                return Job(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:ml/v1:JobIamPolicy":
                return JobIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:ml/v1:Model":
                return Model(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:ml/v1:ModelIamPolicy":
                return ModelIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:ml/v1:ModelVersion":
                return ModelVersion(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:ml/v1:Study":
                return Study(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:ml/v1:StudyTrial":
                return StudyTrial(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp-native", "ml/v1", _module_instance)

_register_module()
