# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .note import *
from .note_iam_policy import *
from .occurrence import *
from .occurrence_iam_policy import *
from .provider_note import *
from .provider_note_iam_policy import *
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
            if typ == "gcp-native:containeranalysis/v1alpha1:Note":
                return Note(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:containeranalysis/v1alpha1:NoteIamPolicy":
                return NoteIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:containeranalysis/v1alpha1:Occurrence":
                return Occurrence(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:containeranalysis/v1alpha1:OccurrenceIamPolicy":
                return OccurrenceIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:containeranalysis/v1alpha1:ProviderNote":
                return ProviderNote(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp-native:containeranalysis/v1alpha1:ProviderNoteIamPolicy":
                return ProviderNoteIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp-native", "containeranalysis/v1alpha1", _module_instance)

_register_module()
