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

__all__ = ['Interconnect']


class Interconnect(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_enabled: Optional[pulumi.Input[bool]] = None,
                 circuit_infos: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InterconnectCircuitInfoArgs']]]]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 customer_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expected_outages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InterconnectOutageNotificationArgs']]]]] = None,
                 google_ip_address: Optional[pulumi.Input[str]] = None,
                 google_reference_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 interconnect: Optional[pulumi.Input[str]] = None,
                 interconnect_attachments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 interconnect_type: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 label_fingerprint: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 link_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 noc_contact_email: Optional[pulumi.Input[str]] = None,
                 operational_status: Optional[pulumi.Input[str]] = None,
                 peer_ip_address: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 provisioned_link_count: Optional[pulumi.Input[int]] = None,
                 requested_link_count: Optional[pulumi.Input[int]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a Interconnect in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_enabled: Administrative status of the interconnect. When this is set to true, the Interconnect is functional and can carry traffic. When set to false, no packets can be carried over the interconnect and no BGP routes are exchanged over it. By default, the status is set to true.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InterconnectCircuitInfoArgs']]]] circuit_infos: [Output Only] A list of CircuitInfo objects, that describe the individual circuits in this LAG.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] customer_name: Customer name, to put in the Letter of Authorization as the party authorized to request a crossconnect.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InterconnectOutageNotificationArgs']]]] expected_outages: [Output Only] A list of outages expected for this Interconnect.
        :param pulumi.Input[str] google_ip_address: [Output Only] IP address configured on the Google side of the Interconnect link. This can be used only for ping tests.
        :param pulumi.Input[str] google_reference_id: [Output Only] Google reference ID to be used when raising support tickets with Google or otherwise to debug backend connectivity issues.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] interconnect_attachments: [Output Only] A list of the URLs of all InterconnectAttachments configured to use this Interconnect.
        :param pulumi.Input[str] interconnect_type: Type of interconnect, which can take one of the following values: 
               - PARTNER: A partner-managed interconnection shared between customers though a partner. 
               - DEDICATED: A dedicated physical interconnection with the customer. Note that a value IT_PRIVATE has been deprecated in favor of DEDICATED.
        :param pulumi.Input[str] kind: [Output Only] Type of the resource. Always compute#interconnect for interconnects.
        :param pulumi.Input[str] label_fingerprint: A fingerprint for the labels being applied to this Interconnect, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet.
               
               To see the latest fingerprint, make a get() request to retrieve an Interconnect.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty.
        :param pulumi.Input[str] link_type: Type of link requested, which can take one of the following values: 
               - LINK_TYPE_ETHERNET_10G_LR: A 10G Ethernet with LR optics 
               - LINK_TYPE_ETHERNET_100G_LR: A 100G Ethernet with LR optics. Note that this field indicates the speed of each of the links in the bundle, not the speed of the entire bundle.
        :param pulumi.Input[str] location: URL of the InterconnectLocation object that represents where this connection is to be provisioned.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] noc_contact_email: Email address to contact the customer NOC for operations and maintenance notifications regarding this Interconnect. If specified, this will be used for notifications in addition to all other forms described, such as Stackdriver logs alerting and Cloud Notifications.
        :param pulumi.Input[str] operational_status: [Output Only] The current status of this Interconnect's functionality, which can take one of the following values: 
               - OS_ACTIVE: A valid Interconnect, which is turned up and is ready to use. Attachments may be provisioned on this Interconnect. 
               - OS_UNPROVISIONED: An Interconnect that has not completed turnup. No attachments may be provisioned on this Interconnect. 
               - OS_UNDER_MAINTENANCE: An Interconnect that is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.
        :param pulumi.Input[str] peer_ip_address: [Output Only] IP address configured on the customer side of the Interconnect link. The customer should configure this IP address during turnup when prompted by Google NOC. This can be used only for ping tests.
        :param pulumi.Input[int] provisioned_link_count: [Output Only] Number of links actually provisioned in this interconnect.
        :param pulumi.Input[int] requested_link_count: Target number of physical links in the link bundle, as requested by the customer.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[str] state: [Output Only] The current state of Interconnect functionality, which can take one of the following values: 
               - ACTIVE: The Interconnect is valid, turned up and ready to use. Attachments may be provisioned on this Interconnect. 
               - UNPROVISIONED: The Interconnect has not completed turnup. No attachments may be provisioned on this Interconnect. 
               - UNDER_MAINTENANCE: The Interconnect is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.
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

            __props__['admin_enabled'] = admin_enabled
            __props__['circuit_infos'] = circuit_infos
            __props__['creation_timestamp'] = creation_timestamp
            __props__['customer_name'] = customer_name
            __props__['description'] = description
            __props__['expected_outages'] = expected_outages
            __props__['google_ip_address'] = google_ip_address
            __props__['google_reference_id'] = google_reference_id
            __props__['id'] = id
            if interconnect is None and not opts.urn:
                raise TypeError("Missing required property 'interconnect'")
            __props__['interconnect'] = interconnect
            __props__['interconnect_attachments'] = interconnect_attachments
            __props__['interconnect_type'] = interconnect_type
            __props__['kind'] = kind
            __props__['label_fingerprint'] = label_fingerprint
            __props__['labels'] = labels
            __props__['link_type'] = link_type
            __props__['location'] = location
            __props__['name'] = name
            __props__['noc_contact_email'] = noc_contact_email
            __props__['operational_status'] = operational_status
            __props__['peer_ip_address'] = peer_ip_address
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['provisioned_link_count'] = provisioned_link_count
            __props__['requested_link_count'] = requested_link_count
            __props__['self_link'] = self_link
            __props__['state'] = state
        super(Interconnect, __self__).__init__(
            'gcp-native:compute/beta:Interconnect',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Interconnect':
        """
        Get an existing Interconnect resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_enabled"] = None
        __props__["circuit_infos"] = None
        __props__["creation_timestamp"] = None
        __props__["customer_name"] = None
        __props__["description"] = None
        __props__["expected_outages"] = None
        __props__["google_ip_address"] = None
        __props__["google_reference_id"] = None
        __props__["interconnect_attachments"] = None
        __props__["interconnect_type"] = None
        __props__["kind"] = None
        __props__["label_fingerprint"] = None
        __props__["labels"] = None
        __props__["link_type"] = None
        __props__["location"] = None
        __props__["name"] = None
        __props__["noc_contact_email"] = None
        __props__["operational_status"] = None
        __props__["peer_ip_address"] = None
        __props__["provisioned_link_count"] = None
        __props__["requested_link_count"] = None
        __props__["self_link"] = None
        __props__["state"] = None
        return Interconnect(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> pulumi.Output[bool]:
        """
        Administrative status of the interconnect. When this is set to true, the Interconnect is functional and can carry traffic. When set to false, no packets can be carried over the interconnect and no BGP routes are exchanged over it. By default, the status is set to true.
        """
        return pulumi.get(self, "admin_enabled")

    @property
    @pulumi.getter(name="circuitInfos")
    def circuit_infos(self) -> pulumi.Output[Sequence['outputs.InterconnectCircuitInfoResponse']]:
        """
        [Output Only] A list of CircuitInfo objects, that describe the individual circuits in this LAG.
        """
        return pulumi.get(self, "circuit_infos")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        [Output Only] Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="customerName")
    def customer_name(self) -> pulumi.Output[str]:
        """
        Customer name, to put in the Letter of Authorization as the party authorized to request a crossconnect.
        """
        return pulumi.get(self, "customer_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expectedOutages")
    def expected_outages(self) -> pulumi.Output[Sequence['outputs.InterconnectOutageNotificationResponse']]:
        """
        [Output Only] A list of outages expected for this Interconnect.
        """
        return pulumi.get(self, "expected_outages")

    @property
    @pulumi.getter(name="googleIpAddress")
    def google_ip_address(self) -> pulumi.Output[str]:
        """
        [Output Only] IP address configured on the Google side of the Interconnect link. This can be used only for ping tests.
        """
        return pulumi.get(self, "google_ip_address")

    @property
    @pulumi.getter(name="googleReferenceId")
    def google_reference_id(self) -> pulumi.Output[str]:
        """
        [Output Only] Google reference ID to be used when raising support tickets with Google or otherwise to debug backend connectivity issues.
        """
        return pulumi.get(self, "google_reference_id")

    @property
    @pulumi.getter(name="interconnectAttachments")
    def interconnect_attachments(self) -> pulumi.Output[Sequence[str]]:
        """
        [Output Only] A list of the URLs of all InterconnectAttachments configured to use this Interconnect.
        """
        return pulumi.get(self, "interconnect_attachments")

    @property
    @pulumi.getter(name="interconnectType")
    def interconnect_type(self) -> pulumi.Output[str]:
        """
        Type of interconnect, which can take one of the following values: 
        - PARTNER: A partner-managed interconnection shared between customers though a partner. 
        - DEDICATED: A dedicated physical interconnection with the customer. Note that a value IT_PRIVATE has been deprecated in favor of DEDICATED.
        """
        return pulumi.get(self, "interconnect_type")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output Only] Type of the resource. Always compute#interconnect for interconnects.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[str]:
        """
        A fingerprint for the labels being applied to this Interconnect, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet.

        To see the latest fingerprint, make a get() request to retrieve an Interconnect.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="linkType")
    def link_type(self) -> pulumi.Output[str]:
        """
        Type of link requested, which can take one of the following values: 
        - LINK_TYPE_ETHERNET_10G_LR: A 10G Ethernet with LR optics 
        - LINK_TYPE_ETHERNET_100G_LR: A 100G Ethernet with LR optics. Note that this field indicates the speed of each of the links in the bundle, not the speed of the entire bundle.
        """
        return pulumi.get(self, "link_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        URL of the InterconnectLocation object that represents where this connection is to be provisioned.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nocContactEmail")
    def noc_contact_email(self) -> pulumi.Output[str]:
        """
        Email address to contact the customer NOC for operations and maintenance notifications regarding this Interconnect. If specified, this will be used for notifications in addition to all other forms described, such as Stackdriver logs alerting and Cloud Notifications.
        """
        return pulumi.get(self, "noc_contact_email")

    @property
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> pulumi.Output[str]:
        """
        [Output Only] The current status of this Interconnect's functionality, which can take one of the following values: 
        - OS_ACTIVE: A valid Interconnect, which is turned up and is ready to use. Attachments may be provisioned on this Interconnect. 
        - OS_UNPROVISIONED: An Interconnect that has not completed turnup. No attachments may be provisioned on this Interconnect. 
        - OS_UNDER_MAINTENANCE: An Interconnect that is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.
        """
        return pulumi.get(self, "operational_status")

    @property
    @pulumi.getter(name="peerIpAddress")
    def peer_ip_address(self) -> pulumi.Output[str]:
        """
        [Output Only] IP address configured on the customer side of the Interconnect link. The customer should configure this IP address during turnup when prompted by Google NOC. This can be used only for ping tests.
        """
        return pulumi.get(self, "peer_ip_address")

    @property
    @pulumi.getter(name="provisionedLinkCount")
    def provisioned_link_count(self) -> pulumi.Output[int]:
        """
        [Output Only] Number of links actually provisioned in this interconnect.
        """
        return pulumi.get(self, "provisioned_link_count")

    @property
    @pulumi.getter(name="requestedLinkCount")
    def requested_link_count(self) -> pulumi.Output[int]:
        """
        Target number of physical links in the link bundle, as requested by the customer.
        """
        return pulumi.get(self, "requested_link_count")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        [Output Only] The current state of Interconnect functionality, which can take one of the following values: 
        - ACTIVE: The Interconnect is valid, turned up and ready to use. Attachments may be provisioned on this Interconnect. 
        - UNPROVISIONED: The Interconnect has not completed turnup. No attachments may be provisioned on this Interconnect. 
        - UNDER_MAINTENANCE: The Interconnect is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.
        """
        return pulumi.get(self, "state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

