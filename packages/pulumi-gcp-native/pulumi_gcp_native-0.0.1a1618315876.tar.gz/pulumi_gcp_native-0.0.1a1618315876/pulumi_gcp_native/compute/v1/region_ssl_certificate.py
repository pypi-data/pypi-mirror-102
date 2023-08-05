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

__all__ = ['RegionSslCertificate']


class RegionSslCertificate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input[pulumi.InputType['SslCertificateManagedSslCertificateArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 self_managed: Optional[pulumi.Input[pulumi.InputType['SslCertificateSelfManagedSslCertificateArgs']]] = None,
                 ssl_certificate: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a SslCertificate resource in the specified project and region using the data included in the request

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: A value read into memory from a certificate file. The certificate file must be in PEM format. The certificate chain must be no greater than 5 certs long. The chain must include at least one intermediate cert.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] expire_time: [Output Only] Expire time of the certificate. RFC3339
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output Only] Type of the resource. Always compute#sslCertificate for SSL certificates.
        :param pulumi.Input[pulumi.InputType['SslCertificateManagedSslCertificateArgs']] managed: Configuration and status of a managed SSL certificate.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] private_key: A value read into memory from a write-only private key file. The private key file must be in PEM format. For security, only insert requests include this field.
        :param pulumi.Input[str] region: [Output Only] URL of the region where the regional SSL Certificate resides. This field is not applicable to global SSL Certificate.
        :param pulumi.Input[str] self_link: [Output only] Server-defined URL for the resource.
        :param pulumi.Input[pulumi.InputType['SslCertificateSelfManagedSslCertificateArgs']] self_managed: Configuration and status of a self-managed SSL certificate.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alternative_names: [Output Only] Domains associated with the certificate via Subject Alternative Name.
        :param pulumi.Input[str] type: (Optional) Specifies the type of SSL certificate, either "SELF_MANAGED" or "MANAGED". If not specified, the certificate is self-managed and the fields certificate and private_key are used.
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

            __props__['certificate'] = certificate
            __props__['creation_timestamp'] = creation_timestamp
            __props__['description'] = description
            __props__['expire_time'] = expire_time
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['managed'] = managed
            __props__['name'] = name
            __props__['private_key'] = private_key
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            __props__['self_link'] = self_link
            __props__['self_managed'] = self_managed
            if ssl_certificate is None and not opts.urn:
                raise TypeError("Missing required property 'ssl_certificate'")
            __props__['ssl_certificate'] = ssl_certificate
            __props__['subject_alternative_names'] = subject_alternative_names
            __props__['type'] = type
        super(RegionSslCertificate, __self__).__init__(
            'gcp-native:compute/v1:RegionSslCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegionSslCertificate':
        """
        Get an existing RegionSslCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["certificate"] = None
        __props__["creation_timestamp"] = None
        __props__["description"] = None
        __props__["expire_time"] = None
        __props__["kind"] = None
        __props__["managed"] = None
        __props__["name"] = None
        __props__["private_key"] = None
        __props__["region"] = None
        __props__["self_link"] = None
        __props__["self_managed"] = None
        __props__["subject_alternative_names"] = None
        __props__["type"] = None
        return RegionSslCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[str]:
        """
        A value read into memory from a certificate file. The certificate file must be in PEM format. The certificate chain must be no greater than 5 certs long. The chain must include at least one intermediate cert.
        """
        return pulumi.get(self, "certificate")

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
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        [Output Only] Expire time of the certificate. RFC3339
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] Type of the resource. Always compute#sslCertificate for SSL certificates.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def managed(self) -> pulumi.Output['outputs.SslCertificateManagedSslCertificateResponse']:
        """
        Configuration and status of a managed SSL certificate.
        """
        return pulumi.get(self, "managed")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        A value read into memory from a write-only private key file. The private key file must be in PEM format. For security, only insert requests include this field.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] URL of the region where the regional SSL Certificate resides. This field is not applicable to global SSL Certificate.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfManaged")
    def self_managed(self) -> pulumi.Output['outputs.SslCertificateSelfManagedSslCertificateResponse']:
        """
        Configuration and status of a self-managed SSL certificate.
        """
        return pulumi.get(self, "self_managed")

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> pulumi.Output[Sequence[str]]:
        """
        [Output Only] Domains associated with the certificate via Subject Alternative Name.
        """
        return pulumi.get(self, "subject_alternative_names")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        (Optional) Specifies the type of SSL certificate, either "SELF_MANAGED" or "MANAGED". If not specified, the certificate is self-managed and the fields certificate and private_key are used.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

