# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['TargetHttpsProxy']


class TargetHttpsProxy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 authorization: Optional[pulumi.Input[str]] = None,
                 authorization_policy: Optional[pulumi.Input[str]] = None,
                 certificate_map: Optional[pulumi.Input[str]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 http_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 proxy_bind: Optional[pulumi.Input[bool]] = None,
                 quic_override: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 self_link_with_id: Optional[pulumi.Input[str]] = None,
                 server_tls_policy: Optional[pulumi.Input[str]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_policy: Optional[pulumi.Input[str]] = None,
                 target_https_proxy: Optional[pulumi.Input[str]] = None,
                 url_map: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a TargetHttpsProxy resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication: [Deprecated] Use serverTlsPolicy instead.
        :param pulumi.Input[str] authorization: [Deprecated] Use authorizationPolicy instead.
        :param pulumi.Input[str] authorization_policy: Optional. A URL referring to a networksecurity.AuthorizationPolicy resource that describes how the proxy should authorize inbound traffic. If left blank, access will not be restricted by an authorization policy.
               Refer to the AuthorizationPolicy resource for additional details.
               authorizationPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED.
               Note: This field currently has no impact.
        :param pulumi.Input[str] certificate_map: URL of a certificate map that identifies a certificate map associated with the given target proxy. This field can only be set for global target proxies. If set, sslCertificates will be ignored.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] fingerprint: Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetHttpsProxy. An up-to-date fingerprint must be provided in order to patch the TargetHttpsProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetHttpsProxy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] http_filters: URLs to networkservices.HttpFilter resources enabled for xDS clients using this configuration. For example, https://networkservices.googleapis.com/beta/projects/project/locations/locationhttpFilters/httpFilter Only filters that handle outbound connection and stream events may be specified. These filters work in conjunction with a default set of HTTP filters that may already be configured by Traffic Director. Traffic Director will determine the final location of these filters within xDS configuration based on the name of the HTTP filter. If Traffic Director positions multiple filters at the same location, those filters will be in the same order as specified in this list.
               httpFilters only applies for loadbalancers with loadBalancingScheme set to INTERNAL_SELF_MANAGED. See ForwardingRule for more details.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output Only] Type of resource. Always compute#targetHttpsProxy for target HTTPS proxies.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[bool] proxy_bind: This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED.
               
               When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them.
               
               The default is false.
        :param pulumi.Input[str] quic_override: Specifies the QUIC override policy for this TargetHttpsProxy resource. This setting determines whether the load balancer attempts to negotiate QUIC with clients. You can specify NONE, ENABLE, or DISABLE.  
               - When quic-override is set to NONE, Google manages whether QUIC is used. 
               - When quic-override is set to ENABLE, the load balancer uses QUIC when possible. 
               - When quic-override is set to DISABLE, the load balancer doesn't use QUIC. 
               - If the quic-override flag is not specified, NONE is implied.
        :param pulumi.Input[str] region: [Output Only] URL of the region where the regional TargetHttpsProxy resides. This field is not applicable to global TargetHttpsProxies.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[str] self_link_with_id: [Output Only] Server-defined URL for this resource with the resource id.
        :param pulumi.Input[str] server_tls_policy: Optional. A URL referring to a networksecurity.ServerTlsPolicy resource that describes how the proxy should authenticate inbound traffic.
               serverTlsPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED.
               If left blank, communications are not encrypted.
               Note: This field currently has no impact.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssl_certificates: URLs to SslCertificate resources that are used to authenticate connections between users and the load balancer. At least one SSL certificate must be specified. Currently, you may specify up to 15 SSL certificates.
        :param pulumi.Input[str] ssl_policy: URL of SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the TargetHttpsProxy resource has no SSL policy configured.
        :param pulumi.Input[str] url_map: A fully-qualified or valid partial URL to the UrlMap resource that defines the mapping from URL to the BackendService. For example, the following are all valid URLs for specifying a URL map:  
               - https://www.googleapis.compute/v1/projects/project/global/urlMaps/url-map 
               - projects/project/global/urlMaps/url-map 
               - global/urlMaps/url-map
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

            __props__['authentication'] = authentication
            __props__['authorization'] = authorization
            __props__['authorization_policy'] = authorization_policy
            __props__['certificate_map'] = certificate_map
            __props__['creation_timestamp'] = creation_timestamp
            __props__['description'] = description
            __props__['fingerprint'] = fingerprint
            __props__['http_filters'] = http_filters
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['name'] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['proxy_bind'] = proxy_bind
            __props__['quic_override'] = quic_override
            __props__['region'] = region
            __props__['self_link'] = self_link
            __props__['self_link_with_id'] = self_link_with_id
            __props__['server_tls_policy'] = server_tls_policy
            __props__['ssl_certificates'] = ssl_certificates
            __props__['ssl_policy'] = ssl_policy
            if target_https_proxy is None and not opts.urn:
                raise TypeError("Missing required property 'target_https_proxy'")
            __props__['target_https_proxy'] = target_https_proxy
            __props__['url_map'] = url_map
        super(TargetHttpsProxy, __self__).__init__(
            'gcp-native:compute/alpha:TargetHttpsProxy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TargetHttpsProxy':
        """
        Get an existing TargetHttpsProxy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authentication"] = None
        __props__["authorization"] = None
        __props__["authorization_policy"] = None
        __props__["certificate_map"] = None
        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["fingerprint"] = None
        __props__["http_filters"] = None
        __props__["kind"] = None
        __props__["name"] = None
        __props__["proxy_bind"] = None
        __props__["quic_override"] = None
        __props__["region"] = None
        __props__["self_link"] = None
        __props__["self_link_with_id"] = None
        __props__["server_tls_policy"] = None
        __props__["ssl_certificates"] = None
        __props__["ssl_policy"] = None
        __props__["url_map"] = None
        return TargetHttpsProxy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[str]:
        """
        [Deprecated] Use serverTlsPolicy instead.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[str]:
        """
        [Deprecated] Use authorizationPolicy instead.
        """
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="authorizationPolicy")
    def authorization_policy(self) -> pulumi.Output[str]:
        """
        Optional. A URL referring to a networksecurity.AuthorizationPolicy resource that describes how the proxy should authorize inbound traffic. If left blank, access will not be restricted by an authorization policy.
        Refer to the AuthorizationPolicy resource for additional details.
        authorizationPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED.
        Note: This field currently has no impact.
        """
        return pulumi.get(self, "authorization_policy")

    @property
    @pulumi.getter(name="certificateMap")
    def certificate_map(self) -> pulumi.Output[str]:
        """
        URL of a certificate map that identifies a certificate map associated with the given target proxy. This field can only be set for global target proxies. If set, sslCertificates will be ignored.
        """
        return pulumi.get(self, "certificate_map")

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
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetHttpsProxy. An up-to-date fingerprint must be provided in order to patch the TargetHttpsProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetHttpsProxy.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="httpFilters")
    def http_filters(self) -> pulumi.Output[Sequence[str]]:
        """
        URLs to networkservices.HttpFilter resources enabled for xDS clients using this configuration. For example, https://networkservices.googleapis.com/beta/projects/project/locations/locationhttpFilters/httpFilter Only filters that handle outbound connection and stream events may be specified. These filters work in conjunction with a default set of HTTP filters that may already be configured by Traffic Director. Traffic Director will determine the final location of these filters within xDS configuration based on the name of the HTTP filter. If Traffic Director positions multiple filters at the same location, those filters will be in the same order as specified in this list.
        httpFilters only applies for loadbalancers with loadBalancingScheme set to INTERNAL_SELF_MANAGED. See ForwardingRule for more details.
        """
        return pulumi.get(self, "http_filters")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] Type of resource. Always compute#targetHttpsProxy for target HTTPS proxies.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="proxyBind")
    def proxy_bind(self) -> pulumi.Output[bool]:
        """
        This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED.

        When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them.

        The default is false.
        """
        return pulumi.get(self, "proxy_bind")

    @property
    @pulumi.getter(name="quicOverride")
    def quic_override(self) -> pulumi.Output[str]:
        """
        Specifies the QUIC override policy for this TargetHttpsProxy resource. This setting determines whether the load balancer attempts to negotiate QUIC with clients. You can specify NONE, ENABLE, or DISABLE.  
        - When quic-override is set to NONE, Google manages whether QUIC is used. 
        - When quic-override is set to ENABLE, the load balancer uses QUIC when possible. 
        - When quic-override is set to DISABLE, the load balancer doesn't use QUIC. 
        - If the quic-override flag is not specified, NONE is implied.
        """
        return pulumi.get(self, "quic_override")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] URL of the region where the regional TargetHttpsProxy resides. This field is not applicable to global TargetHttpsProxies.
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
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> pulumi.Output[str]:
        """
        Optional. A URL referring to a networksecurity.ServerTlsPolicy resource that describes how the proxy should authenticate inbound traffic.
        serverTlsPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED.
        If left blank, communications are not encrypted.
        Note: This field currently has no impact.
        """
        return pulumi.get(self, "server_tls_policy")

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Output[Sequence[str]]:
        """
        URLs to SslCertificate resources that are used to authenticate connections between users and the load balancer. At least one SSL certificate must be specified. Currently, you may specify up to 15 SSL certificates.
        """
        return pulumi.get(self, "ssl_certificates")

    @property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> pulumi.Output[str]:
        """
        URL of SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the TargetHttpsProxy resource has no SSL policy configured.
        """
        return pulumi.get(self, "ssl_policy")

    @property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> pulumi.Output[str]:
        """
        A fully-qualified or valid partial URL to the UrlMap resource that defines the mapping from URL to the BackendService. For example, the following are all valid URLs for specifying a URL map:  
        - https://www.googleapis.compute/v1/projects/project/global/urlMaps/url-map 
        - projects/project/global/urlMaps/url-map 
        - global/urlMaps/url-map
        """
        return pulumi.get(self, "url_map")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

