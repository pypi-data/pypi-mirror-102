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

__all__ = ['HealthCheck']


class HealthCheck(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 check_interval_sec: Optional[pulumi.Input[int]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grpc_health_check: Optional[pulumi.Input[pulumi.InputType['GRPCHealthCheckArgs']]] = None,
                 health_check: Optional[pulumi.Input[str]] = None,
                 healthy_threshold: Optional[pulumi.Input[int]] = None,
                 http2_health_check: Optional[pulumi.Input[pulumi.InputType['HTTP2HealthCheckArgs']]] = None,
                 http_health_check: Optional[pulumi.Input[pulumi.InputType['HTTPHealthCheckArgs']]] = None,
                 https_health_check: Optional[pulumi.Input[pulumi.InputType['HTTPSHealthCheckArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['HealthCheckLogConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 ssl_health_check: Optional[pulumi.Input[pulumi.InputType['SSLHealthCheckArgs']]] = None,
                 tcp_health_check: Optional[pulumi.Input[pulumi.InputType['TCPHealthCheckArgs']]] = None,
                 timeout_sec: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 unhealthy_threshold: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a HealthCheck resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] check_interval_sec: How often (in seconds) to send a health check. The default value is 5 seconds.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in 3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[int] healthy_threshold: A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: Type of the resource.
        :param pulumi.Input[pulumi.InputType['HealthCheckLogConfigArgs']] log_config: Configure logging on this health check.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.
        :param pulumi.Input[str] region: [Output Only] Region where the health check resides. Not applicable to global health checks.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[int] timeout_sec: How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        :param pulumi.Input[str] type: Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS or HTTP2. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.
        :param pulumi.Input[int] unhealthy_threshold: A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
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

            __props__['check_interval_sec'] = check_interval_sec
            __props__['creation_timestamp'] = creation_timestamp
            __props__['description'] = description
            __props__['grpc_health_check'] = grpc_health_check
            if health_check is None and not opts.urn:
                raise TypeError("Missing required property 'health_check'")
            __props__['health_check'] = health_check
            __props__['healthy_threshold'] = healthy_threshold
            __props__['http2_health_check'] = http2_health_check
            __props__['http_health_check'] = http_health_check
            __props__['https_health_check'] = https_health_check
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['log_config'] = log_config
            __props__['name'] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['region'] = region
            __props__['self_link'] = self_link
            __props__['ssl_health_check'] = ssl_health_check
            __props__['tcp_health_check'] = tcp_health_check
            __props__['timeout_sec'] = timeout_sec
            __props__['type'] = type
            __props__['unhealthy_threshold'] = unhealthy_threshold
        super(HealthCheck, __self__).__init__(
            'gcp-native:compute/beta:HealthCheck',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HealthCheck':
        """
        Get an existing HealthCheck resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["check_interval_sec"] = None
        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["grpc_health_check"] = None
        __props__["healthy_threshold"] = None
        __props__["http2_health_check"] = None
        __props__["http_health_check"] = None
        __props__["https_health_check"] = None
        __props__["kind"] = None
        __props__["log_config"] = None
        __props__["name"] = None
        __props__["region"] = None
        __props__["self_link"] = None
        __props__["ssl_health_check"] = None
        __props__["tcp_health_check"] = None
        __props__["timeout_sec"] = None
        __props__["type"] = None
        __props__["unhealthy_threshold"] = None
        return HealthCheck(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> pulumi.Output[int]:
        """
        How often (in seconds) to send a health check. The default value is 5 seconds.
        """
        return pulumi.get(self, "check_interval_sec")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        [Output Only] Creation timestamp in 3339 text format.
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
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(self) -> pulumi.Output['outputs.GRPCHealthCheckResponse']:
        return pulumi.get(self, "grpc_health_check")

    @property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Output[int]:
        """
        A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        """
        return pulumi.get(self, "healthy_threshold")

    @property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(self) -> pulumi.Output['outputs.HTTP2HealthCheckResponse']:
        return pulumi.get(self, "http2_health_check")

    @property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(self) -> pulumi.Output['outputs.HTTPHealthCheckResponse']:
        return pulumi.get(self, "http_health_check")

    @property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(self) -> pulumi.Output['outputs.HTTPSHealthCheckResponse']:
        return pulumi.get(self, "https_health_check")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output['outputs.HealthCheckLogConfigResponse']:
        """
        Configure logging on this health check.
        """
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] Region where the health check resides. Not applicable to global health checks.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(self) -> pulumi.Output['outputs.SSLHealthCheckResponse']:
        return pulumi.get(self, "ssl_health_check")

    @property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(self) -> pulumi.Output['outputs.TCPHealthCheckResponse']:
        return pulumi.get(self, "tcp_health_check")

    @property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[int]:
        """
        How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        """
        return pulumi.get(self, "timeout_sec")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS or HTTP2. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Output[int]:
        """
        A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
        """
        return pulumi.get(self, "unhealthy_threshold")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

