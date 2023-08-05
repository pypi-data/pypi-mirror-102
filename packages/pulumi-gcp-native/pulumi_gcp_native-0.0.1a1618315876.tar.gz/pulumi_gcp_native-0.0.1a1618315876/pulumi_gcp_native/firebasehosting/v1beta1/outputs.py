# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = [
    'ActingUserResponse',
    'CertDnsChallengeResponse',
    'CertHttpChallengeResponse',
    'CloudRunRewriteResponse',
    'DomainProvisioningResponse',
    'DomainRedirectResponse',
    'HeaderResponse',
    'I18nConfigResponse',
    'PreviewConfigResponse',
    'RedirectResponse',
    'ReleaseResponse',
    'RewriteResponse',
    'ServingConfigResponse',
    'VersionResponse',
]

@pulumi.output_type
class ActingUserResponse(dict):
    """
    Contains metadata about the user who performed an action, such as creating a release or finalizing a version.
    """
    def __init__(__self__, *,
                 email: str,
                 image_url: str):
        """
        Contains metadata about the user who performed an action, such as creating a release or finalizing a version.
        :param str email: The email address of the user when the user performed the action.
        :param str image_url: A profile image URL for the user. May not be present if the user has changed their email address or deleted their account.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "image_url", image_url)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address of the user when the user performed the action.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> str:
        """
        A profile image URL for the user. May not be present if the user has changed their email address or deleted their account.
        """
        return pulumi.get(self, "image_url")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CertDnsChallengeResponse(dict):
    """
    Represents a DNS certificate challenge.
    """
    def __init__(__self__, *,
                 domain_name: str,
                 token: str):
        """
        Represents a DNS certificate challenge.
        :param str domain_name: The domain name upon which the DNS challenge must be satisfied.
        :param str token: The value that must be present as a TXT record on the domain name to satisfy the challenge.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        """
        The domain name upon which the DNS challenge must be satisfied.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        The value that must be present as a TXT record on the domain name to satisfy the challenge.
        """
        return pulumi.get(self, "token")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CertHttpChallengeResponse(dict):
    """
    Represents an HTTP certificate challenge.
    """
    def __init__(__self__, *,
                 path: str,
                 token: str):
        """
        Represents an HTTP certificate challenge.
        :param str path: The URL path on which to serve the specified token to satisfy the certificate challenge.
        :param str token: The token to serve at the specified URL path to satisfy the certificate challenge.
        """
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        The URL path on which to serve the specified token to satisfy the certificate challenge.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        The token to serve at the specified URL path to satisfy the certificate challenge.
        """
        return pulumi.get(self, "token")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CloudRunRewriteResponse(dict):
    """
    A configured rewrite that directs requests to a Cloud Run service. If the Cloud Run service does not exist when setting or updating your Firebase Hosting configuration, then the request fails. Any errors from the Cloud Run service are passed to the end user (for example, if you delete a service, any requests directed to that service receive a `404` error).
    """
    def __init__(__self__, *,
                 region: str,
                 service_id: str):
        """
        A configured rewrite that directs requests to a Cloud Run service. If the Cloud Run service does not exist when setting or updating your Firebase Hosting configuration, then the request fails. Any errors from the Cloud Run service are passed to the end user (for example, if you delete a service, any requests directed to that service receive a `404` error).
        :param str region: Optional. User-provided region where the Cloud Run service is hosted. Defaults to `us-central1` if not supplied.
        :param str service_id: Required. User-defined ID of the Cloud Run service.
        """
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "service_id", service_id)

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        Optional. User-provided region where the Cloud Run service is hosted. Defaults to `us-central1` if not supplied.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        """
        Required. User-defined ID of the Cloud Run service.
        """
        return pulumi.get(self, "service_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainProvisioningResponse(dict):
    """
    The current certificate provisioning status information for a domain.
    """
    def __init__(__self__, *,
                 cert_challenge_discovered_txt: Sequence[str],
                 cert_challenge_dns: 'outputs.CertDnsChallengeResponse',
                 cert_challenge_http: 'outputs.CertHttpChallengeResponse',
                 cert_status: str,
                 discovered_ips: Sequence[str],
                 dns_fetch_time: str,
                 dns_status: str,
                 expected_ips: Sequence[str]):
        """
        The current certificate provisioning status information for a domain.
        :param Sequence[str] cert_challenge_discovered_txt: The TXT records (for the certificate challenge) that were found at the last DNS fetch.
        :param 'CertDnsChallengeResponseArgs' cert_challenge_dns: The DNS challenge for generating a certificate.
        :param 'CertHttpChallengeResponseArgs' cert_challenge_http: The HTTP challenge for generating a certificate.
        :param str cert_status: The certificate provisioning status; updated when Firebase Hosting provisions an SSL certificate for the domain.
        :param Sequence[str] discovered_ips: The IPs found at the last DNS fetch.
        :param str dns_fetch_time: The time at which the last DNS fetch occurred.
        :param str dns_status: The DNS record match status as of the last DNS fetch.
        :param Sequence[str] expected_ips: The list of IPs to which the domain is expected to resolve.
        """
        pulumi.set(__self__, "cert_challenge_discovered_txt", cert_challenge_discovered_txt)
        pulumi.set(__self__, "cert_challenge_dns", cert_challenge_dns)
        pulumi.set(__self__, "cert_challenge_http", cert_challenge_http)
        pulumi.set(__self__, "cert_status", cert_status)
        pulumi.set(__self__, "discovered_ips", discovered_ips)
        pulumi.set(__self__, "dns_fetch_time", dns_fetch_time)
        pulumi.set(__self__, "dns_status", dns_status)
        pulumi.set(__self__, "expected_ips", expected_ips)

    @property
    @pulumi.getter(name="certChallengeDiscoveredTxt")
    def cert_challenge_discovered_txt(self) -> Sequence[str]:
        """
        The TXT records (for the certificate challenge) that were found at the last DNS fetch.
        """
        return pulumi.get(self, "cert_challenge_discovered_txt")

    @property
    @pulumi.getter(name="certChallengeDns")
    def cert_challenge_dns(self) -> 'outputs.CertDnsChallengeResponse':
        """
        The DNS challenge for generating a certificate.
        """
        return pulumi.get(self, "cert_challenge_dns")

    @property
    @pulumi.getter(name="certChallengeHttp")
    def cert_challenge_http(self) -> 'outputs.CertHttpChallengeResponse':
        """
        The HTTP challenge for generating a certificate.
        """
        return pulumi.get(self, "cert_challenge_http")

    @property
    @pulumi.getter(name="certStatus")
    def cert_status(self) -> str:
        """
        The certificate provisioning status; updated when Firebase Hosting provisions an SSL certificate for the domain.
        """
        return pulumi.get(self, "cert_status")

    @property
    @pulumi.getter(name="discoveredIps")
    def discovered_ips(self) -> Sequence[str]:
        """
        The IPs found at the last DNS fetch.
        """
        return pulumi.get(self, "discovered_ips")

    @property
    @pulumi.getter(name="dnsFetchTime")
    def dns_fetch_time(self) -> str:
        """
        The time at which the last DNS fetch occurred.
        """
        return pulumi.get(self, "dns_fetch_time")

    @property
    @pulumi.getter(name="dnsStatus")
    def dns_status(self) -> str:
        """
        The DNS record match status as of the last DNS fetch.
        """
        return pulumi.get(self, "dns_status")

    @property
    @pulumi.getter(name="expectedIps")
    def expected_ips(self) -> Sequence[str]:
        """
        The list of IPs to which the domain is expected to resolve.
        """
        return pulumi.get(self, "expected_ips")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainRedirectResponse(dict):
    """
    Defines the behavior of a domain-level redirect. Domain redirects preserve the path of the redirect but replace the requested domain with the one specified in the redirect configuration.
    """
    def __init__(__self__, *,
                 domain_name: str,
                 type: str):
        """
        Defines the behavior of a domain-level redirect. Domain redirects preserve the path of the redirect but replace the requested domain with the one specified in the redirect configuration.
        :param str domain_name: Required. The domain name to redirect to.
        :param str type: Required. The redirect status code.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        """
        Required. The domain name to redirect to.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Required. The redirect status code.
        """
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class HeaderResponse(dict):
    """
    A [`Header`](https://firebase.google.com/docs/hosting/full-config#headers) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to apply the specified custom response headers.
    """
    def __init__(__self__, *,
                 glob: str,
                 headers: Mapping[str, str],
                 regex: str):
        """
        A [`Header`](https://firebase.google.com/docs/hosting/full-config#headers) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to apply the specified custom response headers.
        :param str glob: The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path.
        :param Mapping[str, str] headers: Required. The additional headers to add to the response.
        :param str regex: The user-supplied RE2 regular expression to match against the request URL path.
        """
        pulumi.set(__self__, "glob", glob)
        pulumi.set(__self__, "headers", headers)
        pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def glob(self) -> str:
        """
        The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path.
        """
        return pulumi.get(self, "glob")

    @property
    @pulumi.getter
    def headers(self) -> Mapping[str, str]:
        """
        Required. The additional headers to add to the response.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter
    def regex(self) -> str:
        """
        The user-supplied RE2 regular expression to match against the request URL path.
        """
        return pulumi.get(self, "regex")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class I18nConfigResponse(dict):
    """
    If provided, i18n rewrites are enabled.
    """
    def __init__(__self__, *,
                 root: str):
        """
        If provided, i18n rewrites are enabled.
        :param str root: Required. The user-supplied path where country and language specific content will be looked for within the public directory.
        """
        pulumi.set(__self__, "root", root)

    @property
    @pulumi.getter
    def root(self) -> str:
        """
        Required. The user-supplied path where country and language specific content will be looked for within the public directory.
        """
        return pulumi.get(self, "root")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PreviewConfigResponse(dict):
    """
    Deprecated in favor of [site channels](sites.channels).
    """
    def __init__(__self__, *,
                 active: bool,
                 expire_time: str):
        """
        Deprecated in favor of [site channels](sites.channels).
        :param bool active: If true, preview URLs are enabled for this version.
        :param str expire_time: Indicates the expiration time for previewing this version; preview URL requests received after this time will 404.
        """
        pulumi.set(__self__, "active", active)
        pulumi.set(__self__, "expire_time", expire_time)

    @property
    @pulumi.getter
    def active(self) -> bool:
        """
        If true, preview URLs are enabled for this version.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> str:
        """
        Indicates the expiration time for previewing this version; preview URL requests received after this time will 404.
        """
        return pulumi.get(self, "expire_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RedirectResponse(dict):
    """
    A [`Redirect`](https://firebase.google.com/docs/hosting/full-config#redirects) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond with a redirect to the specified destination path.
    """
    def __init__(__self__, *,
                 glob: str,
                 location: str,
                 regex: str,
                 status_code: int):
        """
        A [`Redirect`](https://firebase.google.com/docs/hosting/full-config#redirects) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond with a redirect to the specified destination path.
        :param str glob: The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path.
        :param str location: Required. The value to put in the HTTP location header of the response. The location can contain capture group values from the pattern using a `:` prefix to identify the segment and an optional `*` to capture the rest of the URL. For example: "glob": "/:capture*", "statusCode": 301, "location": "https://example.com/foo/:capture"
        :param str regex: The user-supplied RE2 regular expression to match against the request URL path.
        :param int status_code: Required. The status HTTP code to return in the response. It must be a valid 3xx status code.
        """
        pulumi.set(__self__, "glob", glob)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "regex", regex)
        pulumi.set(__self__, "status_code", status_code)

    @property
    @pulumi.getter
    def glob(self) -> str:
        """
        The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path.
        """
        return pulumi.get(self, "glob")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Required. The value to put in the HTTP location header of the response. The location can contain capture group values from the pattern using a `:` prefix to identify the segment and an optional `*` to capture the rest of the URL. For example: "glob": "/:capture*", "statusCode": 301, "location": "https://example.com/foo/:capture"
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def regex(self) -> str:
        """
        The user-supplied RE2 regular expression to match against the request URL path.
        """
        return pulumi.get(self, "regex")

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> int:
        """
        Required. The status HTTP code to return in the response. It must be a valid 3xx status code.
        """
        return pulumi.get(self, "status_code")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReleaseResponse(dict):
    """
     A `Release` is a particular [collection of configurations and files](sites.versions) that is set to be public at a particular time.
    """
    def __init__(__self__, *,
                 message: str,
                 name: str,
                 release_time: str,
                 release_user: 'outputs.ActingUserResponse',
                 type: str,
                 version: 'outputs.VersionResponse'):
        """
         A `Release` is a particular [collection of configurations and files](sites.versions) that is set to be public at a particular time.
        :param str message: The deploy description when the release was created. The value can be up to 512 characters.
        :param str name: The unique identifier for the release, in either of the following formats: - sites/SITE_ID/releases/RELEASE_ID - sites/SITE_ID/channels/CHANNEL_ID/releases/RELEASE_ID This name is provided in the response body when you call [`releases.create`](sites.releases/create) or [`channels.releases.create`](sites.channels.releases/create).
        :param str release_time: The time at which the version is set to be public.
        :param 'ActingUserResponseArgs' release_user: Identifies the user who created the release.
        :param str type: Explains the reason for the release. Specify a value for this field only when creating a `SITE_DISABLE` type release.
        :param 'VersionResponseArgs' version: The configuration and content that was released.
        """
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "release_time", release_time)
        pulumi.set(__self__, "release_user", release_user)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The deploy description when the release was created. The value can be up to 512 characters.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique identifier for the release, in either of the following formats: - sites/SITE_ID/releases/RELEASE_ID - sites/SITE_ID/channels/CHANNEL_ID/releases/RELEASE_ID This name is provided in the response body when you call [`releases.create`](sites.releases/create) or [`channels.releases.create`](sites.channels.releases/create).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="releaseTime")
    def release_time(self) -> str:
        """
        The time at which the version is set to be public.
        """
        return pulumi.get(self, "release_time")

    @property
    @pulumi.getter(name="releaseUser")
    def release_user(self) -> 'outputs.ActingUserResponse':
        """
        Identifies the user who created the release.
        """
        return pulumi.get(self, "release_user")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Explains the reason for the release. Specify a value for this field only when creating a `SITE_DISABLE` type release.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> 'outputs.VersionResponse':
        """
        The configuration and content that was released.
        """
        return pulumi.get(self, "version")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RewriteResponse(dict):
    """
    A [`Rewrite`](https://firebase.google.com/docs/hosting/full-config#rewrites) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond as if the service were given the specified destination URL.
    """
    def __init__(__self__, *,
                 dynamic_links: bool,
                 function: str,
                 glob: str,
                 path: str,
                 regex: str,
                 run: 'outputs.CloudRunRewriteResponse'):
        """
        A [`Rewrite`](https://firebase.google.com/docs/hosting/full-config#rewrites) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond as if the service were given the specified destination URL.
        :param bool dynamic_links: The request will be forwarded to Firebase Dynamic Links.
        :param str function: The function to proxy requests to. Must match the exported function name exactly.
        :param str glob: The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path.
        :param str path: The URL path to rewrite the request to.
        :param str regex: The user-supplied RE2 regular expression to match against the request URL path.
        :param 'CloudRunRewriteResponseArgs' run: The request will be forwarded to Cloud Run.
        """
        pulumi.set(__self__, "dynamic_links", dynamic_links)
        pulumi.set(__self__, "function", function)
        pulumi.set(__self__, "glob", glob)
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "regex", regex)
        pulumi.set(__self__, "run", run)

    @property
    @pulumi.getter(name="dynamicLinks")
    def dynamic_links(self) -> bool:
        """
        The request will be forwarded to Firebase Dynamic Links.
        """
        return pulumi.get(self, "dynamic_links")

    @property
    @pulumi.getter
    def function(self) -> str:
        """
        The function to proxy requests to. Must match the exported function name exactly.
        """
        return pulumi.get(self, "function")

    @property
    @pulumi.getter
    def glob(self) -> str:
        """
        The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path.
        """
        return pulumi.get(self, "glob")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        The URL path to rewrite the request to.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def regex(self) -> str:
        """
        The user-supplied RE2 regular expression to match against the request URL path.
        """
        return pulumi.get(self, "regex")

    @property
    @pulumi.getter
    def run(self) -> 'outputs.CloudRunRewriteResponse':
        """
        The request will be forwarded to Cloud Run.
        """
        return pulumi.get(self, "run")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ServingConfigResponse(dict):
    """
    The configuration for how incoming requests to a site should be routed and processed before serving content. The URL request paths are matched against the specified URL patterns in the configuration, then Hosting applies the applicable configuration according to a specific [priority order](https://firebase.google.com/docs/hosting/full-config#hosting_priority_order).
    """
    def __init__(__self__, *,
                 app_association: str,
                 clean_urls: bool,
                 headers: Sequence['outputs.HeaderResponse'],
                 i18n: 'outputs.I18nConfigResponse',
                 redirects: Sequence['outputs.RedirectResponse'],
                 rewrites: Sequence['outputs.RewriteResponse'],
                 trailing_slash_behavior: str):
        """
        The configuration for how incoming requests to a site should be routed and processed before serving content. The URL request paths are matched against the specified URL patterns in the configuration, then Hosting applies the applicable configuration according to a specific [priority order](https://firebase.google.com/docs/hosting/full-config#hosting_priority_order).
        :param str app_association: How to handle well known App Association files.
        :param bool clean_urls: Defines whether to drop the file extension from uploaded files.
        :param Sequence['HeaderResponseArgs'] headers: An array of objects, where each object specifies a URL pattern that, if matched to the request URL path, triggers Hosting to apply the specified custom response headers.
        :param 'I18nConfigResponseArgs' i18n: Optional. Defines i18n rewrite behavior.
        :param Sequence['RedirectResponseArgs'] redirects: An array of objects (called redirect rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond with a redirect to the specified destination path.
        :param Sequence['RewriteResponseArgs'] rewrites: An array of objects (called rewrite rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond as if the service were given the specified destination URL.
        :param str trailing_slash_behavior: Defines how to handle a trailing slash in the URL path.
        """
        pulumi.set(__self__, "app_association", app_association)
        pulumi.set(__self__, "clean_urls", clean_urls)
        pulumi.set(__self__, "headers", headers)
        pulumi.set(__self__, "i18n", i18n)
        pulumi.set(__self__, "redirects", redirects)
        pulumi.set(__self__, "rewrites", rewrites)
        pulumi.set(__self__, "trailing_slash_behavior", trailing_slash_behavior)

    @property
    @pulumi.getter(name="appAssociation")
    def app_association(self) -> str:
        """
        How to handle well known App Association files.
        """
        return pulumi.get(self, "app_association")

    @property
    @pulumi.getter(name="cleanUrls")
    def clean_urls(self) -> bool:
        """
        Defines whether to drop the file extension from uploaded files.
        """
        return pulumi.get(self, "clean_urls")

    @property
    @pulumi.getter
    def headers(self) -> Sequence['outputs.HeaderResponse']:
        """
        An array of objects, where each object specifies a URL pattern that, if matched to the request URL path, triggers Hosting to apply the specified custom response headers.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter
    def i18n(self) -> 'outputs.I18nConfigResponse':
        """
        Optional. Defines i18n rewrite behavior.
        """
        return pulumi.get(self, "i18n")

    @property
    @pulumi.getter
    def redirects(self) -> Sequence['outputs.RedirectResponse']:
        """
        An array of objects (called redirect rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond with a redirect to the specified destination path.
        """
        return pulumi.get(self, "redirects")

    @property
    @pulumi.getter
    def rewrites(self) -> Sequence['outputs.RewriteResponse']:
        """
        An array of objects (called rewrite rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond as if the service were given the specified destination URL.
        """
        return pulumi.get(self, "rewrites")

    @property
    @pulumi.getter(name="trailingSlashBehavior")
    def trailing_slash_behavior(self) -> str:
        """
        Defines how to handle a trailing slash in the URL path.
        """
        return pulumi.get(self, "trailing_slash_behavior")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VersionResponse(dict):
    """
    A `Version` is a configuration and a collection of static files which determine how a site is displayed.
    """
    def __init__(__self__, *,
                 config: 'outputs.ServingConfigResponse',
                 create_time: str,
                 create_user: 'outputs.ActingUserResponse',
                 delete_time: str,
                 delete_user: 'outputs.ActingUserResponse',
                 file_count: str,
                 finalize_time: str,
                 finalize_user: 'outputs.ActingUserResponse',
                 labels: Mapping[str, str],
                 name: str,
                 preview: 'outputs.PreviewConfigResponse',
                 status: str,
                 version_bytes: str):
        """
        A `Version` is a configuration and a collection of static files which determine how a site is displayed.
        :param 'ServingConfigResponseArgs' config: The configuration for the behavior of the site. This configuration exists in the [`firebase.json`](https://firebase.google.com/docs/cli/#the_firebasejson_file) file.
        :param str create_time: The time at which the version was created.
        :param 'ActingUserResponseArgs' create_user: Identifies the user who created the version.
        :param str delete_time: The time at which the version was `DELETED`.
        :param 'ActingUserResponseArgs' delete_user: Identifies the user who `DELETED` the version.
        :param str file_count: The total number of files associated with the version. This value is calculated after a version is `FINALIZED`.
        :param str finalize_time: The time at which the version was `FINALIZED`.
        :param 'ActingUserResponseArgs' finalize_user: Identifies the user who `FINALIZED` the version.
        :param Mapping[str, str] labels: The labels used for extra metadata and/or filtering.
        :param str name: The fully-qualified resource name for the version, in the format: sites/ SITE_ID/versions/VERSION_ID This name is provided in the response body when you call [`CreateVersion`](sites.versions/create).
        :param 'PreviewConfigResponseArgs' preview: Deprecated in favor of [site channels](sites.channels).
        :param str status: The deploy status of the version. For a successful deploy, call [`CreateVersion`](sites.versions/create) to make a new version (`CREATED` status), [upload all desired files](sites.versions/populateFiles) to the version, then [update](sites.versions/patch) the version to the `FINALIZED` status. Note that if you leave the version in the `CREATED` state for more than 12 hours, the system will automatically mark the version as `ABANDONED`. You can also change the status of a version to `DELETED` by calling [`DeleteVersion`](sites.versions/delete).
        :param str version_bytes: The total stored bytesize of the version. This value is calculated after a version is `FINALIZED`.
        """
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "create_user", create_user)
        pulumi.set(__self__, "delete_time", delete_time)
        pulumi.set(__self__, "delete_user", delete_user)
        pulumi.set(__self__, "file_count", file_count)
        pulumi.set(__self__, "finalize_time", finalize_time)
        pulumi.set(__self__, "finalize_user", finalize_user)
        pulumi.set(__self__, "labels", labels)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "preview", preview)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "version_bytes", version_bytes)

    @property
    @pulumi.getter
    def config(self) -> 'outputs.ServingConfigResponse':
        """
        The configuration for the behavior of the site. This configuration exists in the [`firebase.json`](https://firebase.google.com/docs/cli/#the_firebasejson_file) file.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time at which the version was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="createUser")
    def create_user(self) -> 'outputs.ActingUserResponse':
        """
        Identifies the user who created the version.
        """
        return pulumi.get(self, "create_user")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> str:
        """
        The time at which the version was `DELETED`.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter(name="deleteUser")
    def delete_user(self) -> 'outputs.ActingUserResponse':
        """
        Identifies the user who `DELETED` the version.
        """
        return pulumi.get(self, "delete_user")

    @property
    @pulumi.getter(name="fileCount")
    def file_count(self) -> str:
        """
        The total number of files associated with the version. This value is calculated after a version is `FINALIZED`.
        """
        return pulumi.get(self, "file_count")

    @property
    @pulumi.getter(name="finalizeTime")
    def finalize_time(self) -> str:
        """
        The time at which the version was `FINALIZED`.
        """
        return pulumi.get(self, "finalize_time")

    @property
    @pulumi.getter(name="finalizeUser")
    def finalize_user(self) -> 'outputs.ActingUserResponse':
        """
        Identifies the user who `FINALIZED` the version.
        """
        return pulumi.get(self, "finalize_user")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The labels used for extra metadata and/or filtering.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The fully-qualified resource name for the version, in the format: sites/ SITE_ID/versions/VERSION_ID This name is provided in the response body when you call [`CreateVersion`](sites.versions/create).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def preview(self) -> 'outputs.PreviewConfigResponse':
        """
        Deprecated in favor of [site channels](sites.channels).
        """
        return pulumi.get(self, "preview")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The deploy status of the version. For a successful deploy, call [`CreateVersion`](sites.versions/create) to make a new version (`CREATED` status), [upload all desired files](sites.versions/populateFiles) to the version, then [update](sites.versions/patch) the version to the `FINALIZED` status. Note that if you leave the version in the `CREATED` state for more than 12 hours, the system will automatically mark the version as `ABANDONED`. You can also change the status of a version to `DELETED` by calling [`DeleteVersion`](sites.versions/delete).
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="versionBytes")
    def version_bytes(self) -> str:
        """
        The total stored bytesize of the version. This value is calculated after a version is `FINALIZED`.
        """
        return pulumi.get(self, "version_bytes")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


