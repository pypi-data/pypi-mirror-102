# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = ['AccountChannelPartnerLink']


class AccountChannelPartnerLink(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accounts_id: Optional[pulumi.Input[str]] = None,
                 channel_partner_links_id: Optional[pulumi.Input[str]] = None,
                 link_state: Optional[pulumi.Input[str]] = None,
                 reseller_cloud_identity_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists. * NOT_FOUND: No Cloud Identity customer exists for provided domain. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The new ChannelPartnerLink resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] link_state: Required. State of the channel partner link.
        :param pulumi.Input[str] reseller_cloud_identity_id: Required. Cloud Identity ID of the linked reseller.
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

            if accounts_id is None and not opts.urn:
                raise TypeError("Missing required property 'accounts_id'")
            __props__['accounts_id'] = accounts_id
            if channel_partner_links_id is None and not opts.urn:
                raise TypeError("Missing required property 'channel_partner_links_id'")
            __props__['channel_partner_links_id'] = channel_partner_links_id
            __props__['link_state'] = link_state
            __props__['reseller_cloud_identity_id'] = reseller_cloud_identity_id
            __props__['channel_partner_cloud_identity_info'] = None
            __props__['create_time'] = None
            __props__['invite_link_uri'] = None
            __props__['name'] = None
            __props__['public_id'] = None
            __props__['update_time'] = None
        super(AccountChannelPartnerLink, __self__).__init__(
            'gcp-native:cloudchannel/v1:AccountChannelPartnerLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccountChannelPartnerLink':
        """
        Get an existing AccountChannelPartnerLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["channel_partner_cloud_identity_info"] = None
        __props__["create_time"] = None
        __props__["invite_link_uri"] = None
        __props__["link_state"] = None
        __props__["name"] = None
        __props__["public_id"] = None
        __props__["reseller_cloud_identity_id"] = None
        __props__["update_time"] = None
        return AccountChannelPartnerLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="channelPartnerCloudIdentityInfo")
    def channel_partner_cloud_identity_info(self) -> pulumi.Output['outputs.GoogleCloudChannelV1CloudIdentityInfoResponse']:
        """
        Cloud Identity info of the channel partner (IR).
        """
        return pulumi.get(self, "channel_partner_cloud_identity_info")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Timestamp of when the channel partner link is created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="inviteLinkUri")
    def invite_link_uri(self) -> pulumi.Output[str]:
        """
        URI of the web page where partner accepts the link invitation.
        """
        return pulumi.get(self, "invite_link_uri")

    @property
    @pulumi.getter(name="linkState")
    def link_state(self) -> pulumi.Output[str]:
        """
        Required. State of the channel partner link.
        """
        return pulumi.get(self, "link_state")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name for the channel partner link, in the format accounts/{account_id}/channelPartnerLinks/{id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicId")
    def public_id(self) -> pulumi.Output[str]:
        """
        Public identifier that a customer must use to generate a transfer token to move to this distributor-reseller combination.
        """
        return pulumi.get(self, "public_id")

    @property
    @pulumi.getter(name="resellerCloudIdentityId")
    def reseller_cloud_identity_id(self) -> pulumi.Output[str]:
        """
        Required. Cloud Identity ID of the linked reseller.
        """
        return pulumi.get(self, "reseller_cloud_identity_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Timestamp of when the channel partner link is updated.
        """
        return pulumi.get(self, "update_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

