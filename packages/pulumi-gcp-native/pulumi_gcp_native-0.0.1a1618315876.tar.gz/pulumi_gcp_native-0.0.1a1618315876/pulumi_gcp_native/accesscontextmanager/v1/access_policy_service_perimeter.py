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

__all__ = ['AccessPolicyServicePerimeter']


class AccessPolicyServicePerimeter(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 perimeter_type: Optional[pulumi.Input[str]] = None,
                 service_perimeters_id: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['ServicePerimeterConfigArgs']]] = None,
                 status: Optional[pulumi.Input[pulumi.InputType['ServicePerimeterConfigArgs']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 use_explicit_dry_run_spec: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Service Perimeter. The longrunning operation from this RPC will have a successful status once the Service Perimeter has propagated to long-lasting storage. Service Perimeters containing errors will result in an error response for the first error encountered.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the `ServicePerimeter` and its use. Does not affect behavior.
        :param pulumi.Input[str] name: Required. Resource name for the ServicePerimeter. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{policy_id}/servicePerimeters/{short_name}`
        :param pulumi.Input[str] perimeter_type: Perimeter type indicator. A single project is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty.
        :param pulumi.Input[pulumi.InputType['ServicePerimeterConfigArgs']] spec: Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "use_explicit_dry_run_spec" flag is set.
        :param pulumi.Input[pulumi.InputType['ServicePerimeterConfigArgs']] status: Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries.
        :param pulumi.Input[str] title: Human readable title. Must be unique within the Policy.
        :param pulumi.Input[bool] use_explicit_dry_run_spec: Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values.
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

            if access_policies_id is None and not opts.urn:
                raise TypeError("Missing required property 'access_policies_id'")
            __props__['access_policies_id'] = access_policies_id
            __props__['description'] = description
            __props__['name'] = name
            __props__['perimeter_type'] = perimeter_type
            if service_perimeters_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_perimeters_id'")
            __props__['service_perimeters_id'] = service_perimeters_id
            __props__['spec'] = spec
            __props__['status'] = status
            __props__['title'] = title
            __props__['use_explicit_dry_run_spec'] = use_explicit_dry_run_spec
        super(AccessPolicyServicePerimeter, __self__).__init__(
            'gcp-native:accesscontextmanager/v1:AccessPolicyServicePerimeter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessPolicyServicePerimeter':
        """
        Get an existing AccessPolicyServicePerimeter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = None
        __props__["name"] = None
        __props__["perimeter_type"] = None
        __props__["spec"] = None
        __props__["status"] = None
        __props__["title"] = None
        __props__["use_explicit_dry_run_spec"] = None
        return AccessPolicyServicePerimeter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the `ServicePerimeter` and its use. Does not affect behavior.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. Resource name for the ServicePerimeter. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{policy_id}/servicePerimeters/{short_name}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perimeterType")
    def perimeter_type(self) -> pulumi.Output[str]:
        """
        Perimeter type indicator. A single project is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty.
        """
        return pulumi.get(self, "perimeter_type")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.ServicePerimeterConfigResponse']:
        """
        Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "use_explicit_dry_run_spec" flag is set.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.ServicePerimeterConfigResponse']:
        """
        Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        Human readable title. Must be unique within the Policy.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="useExplicitDryRunSpec")
    def use_explicit_dry_run_spec(self) -> pulumi.Output[bool]:
        """
        Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values.
        """
        return pulumi.get(self, "use_explicit_dry_run_spec")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

