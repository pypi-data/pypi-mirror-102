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
    'GoogleCloudChannelV1AssociationInfoResponse',
    'GoogleCloudChannelV1CloudIdentityInfoResponse',
    'GoogleCloudChannelV1CommitmentSettingsResponse',
    'GoogleCloudChannelV1ContactInfoResponse',
    'GoogleCloudChannelV1EduDataResponse',
    'GoogleCloudChannelV1ParameterResponse',
    'GoogleCloudChannelV1PeriodResponse',
    'GoogleCloudChannelV1ProvisionedServiceResponse',
    'GoogleCloudChannelV1RenewalSettingsResponse',
    'GoogleCloudChannelV1TrialSettingsResponse',
    'GoogleCloudChannelV1ValueResponse',
    'GoogleTypePostalAddressResponse',
]

@pulumi.output_type
class GoogleCloudChannelV1AssociationInfoResponse(dict):
    """
    Association links that an entitlement has to other entitlements.
    """
    def __init__(__self__, *,
                 base_entitlement: str):
        """
        Association links that an entitlement has to other entitlements.
        :param str base_entitlement: The name of the base entitlement, for which this entitlement is an add-on.
        """
        pulumi.set(__self__, "base_entitlement", base_entitlement)

    @property
    @pulumi.getter(name="baseEntitlement")
    def base_entitlement(self) -> str:
        """
        The name of the base entitlement, for which this entitlement is an add-on.
        """
        return pulumi.get(self, "base_entitlement")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1CloudIdentityInfoResponse(dict):
    """
    Cloud Identity information for the Cloud Channel Customer.
    """
    def __init__(__self__, *,
                 admin_console_uri: str,
                 alternate_email: str,
                 customer_type: str,
                 edu_data: 'outputs.GoogleCloudChannelV1EduDataResponse',
                 is_domain_verified: bool,
                 language_code: str,
                 phone_number: str,
                 primary_domain: str):
        """
        Cloud Identity information for the Cloud Channel Customer.
        :param str admin_console_uri: URI of Customer's Admin console dashboard.
        :param str alternate_email: The alternate email.
        :param str customer_type: CustomerType indicates verification type needed for using services.
        :param 'GoogleCloudChannelV1EduDataResponseArgs' edu_data: Edu information about the customer.
        :param bool is_domain_verified: Whether the domain is verified. This field is not returned for a Customer's cloud_identity_info resource. Partners can use the domains.get() method of the Workspace SDK's Directory API, or listen to the PRIMARY_DOMAIN_VERIFIED Pub/Sub event in to track domain verification of their resolve Workspace customers.
        :param str language_code: Language code.
        :param str phone_number: Phone number associated with the Cloud Identity.
        :param str primary_domain: The primary domain name.
        """
        pulumi.set(__self__, "admin_console_uri", admin_console_uri)
        pulumi.set(__self__, "alternate_email", alternate_email)
        pulumi.set(__self__, "customer_type", customer_type)
        pulumi.set(__self__, "edu_data", edu_data)
        pulumi.set(__self__, "is_domain_verified", is_domain_verified)
        pulumi.set(__self__, "language_code", language_code)
        pulumi.set(__self__, "phone_number", phone_number)
        pulumi.set(__self__, "primary_domain", primary_domain)

    @property
    @pulumi.getter(name="adminConsoleUri")
    def admin_console_uri(self) -> str:
        """
        URI of Customer's Admin console dashboard.
        """
        return pulumi.get(self, "admin_console_uri")

    @property
    @pulumi.getter(name="alternateEmail")
    def alternate_email(self) -> str:
        """
        The alternate email.
        """
        return pulumi.get(self, "alternate_email")

    @property
    @pulumi.getter(name="customerType")
    def customer_type(self) -> str:
        """
        CustomerType indicates verification type needed for using services.
        """
        return pulumi.get(self, "customer_type")

    @property
    @pulumi.getter(name="eduData")
    def edu_data(self) -> 'outputs.GoogleCloudChannelV1EduDataResponse':
        """
        Edu information about the customer.
        """
        return pulumi.get(self, "edu_data")

    @property
    @pulumi.getter(name="isDomainVerified")
    def is_domain_verified(self) -> bool:
        """
        Whether the domain is verified. This field is not returned for a Customer's cloud_identity_info resource. Partners can use the domains.get() method of the Workspace SDK's Directory API, or listen to the PRIMARY_DOMAIN_VERIFIED Pub/Sub event in to track domain verification of their resolve Workspace customers.
        """
        return pulumi.get(self, "is_domain_verified")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> str:
        """
        Language code.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> str:
        """
        Phone number associated with the Cloud Identity.
        """
        return pulumi.get(self, "phone_number")

    @property
    @pulumi.getter(name="primaryDomain")
    def primary_domain(self) -> str:
        """
        The primary domain name.
        """
        return pulumi.get(self, "primary_domain")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1CommitmentSettingsResponse(dict):
    """
    Commitment settings for commitment-based offers.
    """
    def __init__(__self__, *,
                 end_time: str,
                 renewal_settings: 'outputs.GoogleCloudChannelV1RenewalSettingsResponse',
                 start_time: str):
        """
        Commitment settings for commitment-based offers.
        :param str end_time: Commitment end timestamp.
        :param 'GoogleCloudChannelV1RenewalSettingsResponseArgs' renewal_settings: Optional. Renewal settings applicable for a commitment-based Offer.
        :param str start_time: Commitment start timestamp.
        """
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "renewal_settings", renewal_settings)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        Commitment end timestamp.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="renewalSettings")
    def renewal_settings(self) -> 'outputs.GoogleCloudChannelV1RenewalSettingsResponse':
        """
        Optional. Renewal settings applicable for a commitment-based Offer.
        """
        return pulumi.get(self, "renewal_settings")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Commitment start timestamp.
        """
        return pulumi.get(self, "start_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1ContactInfoResponse(dict):
    """
    Contact information for a customer account.
    """
    def __init__(__self__, *,
                 display_name: str,
                 email: str,
                 first_name: str,
                 last_name: str,
                 phone: str,
                 title: str):
        """
        Contact information for a customer account.
        :param str display_name: Display name of the contact in the customer account. Populated by combining customer first name and last name.
        :param str email: Email of the contact in the customer account. Email is required for entitlements that need creation of admin.google.com accounts. The email will be the username used in credentials to access the admin.google.com account.
        :param str first_name: First name of the contact in the customer account.
        :param str last_name: Last name of the contact in the customer account.
        :param str phone: Phone number of the contact in the customer account.
        :param str title: Optional. Job title of the contact in the customer account.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "first_name", first_name)
        pulumi.set(__self__, "last_name", last_name)
        pulumi.set(__self__, "phone", phone)
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name of the contact in the customer account. Populated by combining customer first name and last name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the contact in the customer account. Email is required for entitlements that need creation of admin.google.com accounts. The email will be the username used in credentials to access the admin.google.com account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        First name of the contact in the customer account.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        Last name of the contact in the customer account.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def phone(self) -> str:
        """
        Phone number of the contact in the customer account.
        """
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Optional. Job title of the contact in the customer account.
        """
        return pulumi.get(self, "title")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1EduDataResponse(dict):
    """
    Required Edu Attributes
    """
    def __init__(__self__, *,
                 institute_size: str,
                 institute_type: str,
                 website: str):
        """
        Required Edu Attributes
        :param str institute_size: Size of the institute.
        :param str institute_type: Designated institute type of customer.
        :param str website: Web address for the edu customer's institution.
        """
        pulumi.set(__self__, "institute_size", institute_size)
        pulumi.set(__self__, "institute_type", institute_type)
        pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter(name="instituteSize")
    def institute_size(self) -> str:
        """
        Size of the institute.
        """
        return pulumi.get(self, "institute_size")

    @property
    @pulumi.getter(name="instituteType")
    def institute_type(self) -> str:
        """
        Designated institute type of customer.
        """
        return pulumi.get(self, "institute_type")

    @property
    @pulumi.getter
    def website(self) -> str:
        """
        Web address for the edu customer's institution.
        """
        return pulumi.get(self, "website")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1ParameterResponse(dict):
    """
    Definition for extended entitlement parameters.
    """
    def __init__(__self__, *,
                 editable: bool,
                 name: str,
                 value: 'outputs.GoogleCloudChannelV1ValueResponse'):
        """
        Definition for extended entitlement parameters.
        :param bool editable: Specifies whether this parameter is allowed to be changed. For example, for a Google Workspace Business Starter entitlement in commitment plan, num_units is editable when entitlement is active.
        :param str name: Name of the parameter.
        :param 'GoogleCloudChannelV1ValueResponseArgs' value: Value of the parameter.
        """
        pulumi.set(__self__, "editable", editable)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def editable(self) -> bool:
        """
        Specifies whether this parameter is allowed to be changed. For example, for a Google Workspace Business Starter entitlement in commitment plan, num_units is editable when entitlement is active.
        """
        return pulumi.get(self, "editable")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the parameter.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> 'outputs.GoogleCloudChannelV1ValueResponse':
        """
        Value of the parameter.
        """
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1PeriodResponse(dict):
    """
    Represents period in days/months/years.
    """
    def __init__(__self__, *,
                 duration: int,
                 period_type: str):
        """
        Represents period in days/months/years.
        :param int duration: Total duration of Period Type defined.
        :param str period_type: Period Type.
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "period_type", period_type)

    @property
    @pulumi.getter
    def duration(self) -> int:
        """
        Total duration of Period Type defined.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="periodType")
    def period_type(self) -> str:
        """
        Period Type.
        """
        return pulumi.get(self, "period_type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1ProvisionedServiceResponse(dict):
    """
    Service provisioned for an entitlement.
    """
    def __init__(__self__, *,
                 product_id: str,
                 provisioning_id: str,
                 sku_id: str):
        """
        Service provisioned for an entitlement.
        :param str product_id: The product pertaining to the provisioning resource as specified in the Offer.
        :param str provisioning_id: Provisioning ID of the entitlement. For Google Workspace, this would be the underlying Subscription ID.
        :param str sku_id: The SKU pertaining to the provisioning resource as specified in the Offer.
        """
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "provisioning_id", provisioning_id)
        pulumi.set(__self__, "sku_id", sku_id)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        The product pertaining to the provisioning resource as specified in the Offer.
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="provisioningId")
    def provisioning_id(self) -> str:
        """
        Provisioning ID of the entitlement. For Google Workspace, this would be the underlying Subscription ID.
        """
        return pulumi.get(self, "provisioning_id")

    @property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> str:
        """
        The SKU pertaining to the provisioning resource as specified in the Offer.
        """
        return pulumi.get(self, "sku_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1RenewalSettingsResponse(dict):
    """
    Renewal settings for renewable Offers.
    """
    def __init__(__self__, *,
                 enable_renewal: bool,
                 payment_cycle: 'outputs.GoogleCloudChannelV1PeriodResponse',
                 payment_plan: str,
                 resize_unit_count: bool):
        """
        Renewal settings for renewable Offers.
        :param bool enable_renewal: If false, the plan will be completed at the end date.
        :param 'GoogleCloudChannelV1PeriodResponseArgs' payment_cycle: Describes how frequently the reseller will be billed, such as once per month.
        :param str payment_plan: Describes how a reseller will be billed.
        :param bool resize_unit_count: If true and enable_renewal = true, the unit (for example seats or licenses) will be set to the number of active units at renewal time.
        """
        pulumi.set(__self__, "enable_renewal", enable_renewal)
        pulumi.set(__self__, "payment_cycle", payment_cycle)
        pulumi.set(__self__, "payment_plan", payment_plan)
        pulumi.set(__self__, "resize_unit_count", resize_unit_count)

    @property
    @pulumi.getter(name="enableRenewal")
    def enable_renewal(self) -> bool:
        """
        If false, the plan will be completed at the end date.
        """
        return pulumi.get(self, "enable_renewal")

    @property
    @pulumi.getter(name="paymentCycle")
    def payment_cycle(self) -> 'outputs.GoogleCloudChannelV1PeriodResponse':
        """
        Describes how frequently the reseller will be billed, such as once per month.
        """
        return pulumi.get(self, "payment_cycle")

    @property
    @pulumi.getter(name="paymentPlan")
    def payment_plan(self) -> str:
        """
        Describes how a reseller will be billed.
        """
        return pulumi.get(self, "payment_plan")

    @property
    @pulumi.getter(name="resizeUnitCount")
    def resize_unit_count(self) -> bool:
        """
        If true and enable_renewal = true, the unit (for example seats or licenses) will be set to the number of active units at renewal time.
        """
        return pulumi.get(self, "resize_unit_count")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1TrialSettingsResponse(dict):
    """
    Settings for trial offers.
    """
    def __init__(__self__, *,
                 end_time: str,
                 trial: bool):
        """
        Settings for trial offers.
        :param str end_time: Date when the trial ends. The value is in milliseconds using the UNIX Epoch format. See an example [Epoch converter](https://www.epochconverter.com).
        :param bool trial: Determines if the entitlement is in a trial or not: * `true` - The entitlement is in trial. * `false` - The entitlement is not in trial.
        """
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "trial", trial)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        Date when the trial ends. The value is in milliseconds using the UNIX Epoch format. See an example [Epoch converter](https://www.epochconverter.com).
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def trial(self) -> bool:
        """
        Determines if the entitlement is in a trial or not: * `true` - The entitlement is in trial. * `false` - The entitlement is not in trial.
        """
        return pulumi.get(self, "trial")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleCloudChannelV1ValueResponse(dict):
    """
    Data type and value of a parameter.
    """
    def __init__(__self__, *,
                 bool_value: bool,
                 double_value: float,
                 int64_value: str,
                 proto_value: Mapping[str, str],
                 string_value: str):
        """
        Data type and value of a parameter.
        :param bool bool_value: Represents a boolean value.
        :param float double_value: Represents a double value.
        :param str int64_value: Represents an int64 value.
        :param Mapping[str, str] proto_value: Represents an 'Any' proto value.
        :param str string_value: Represents a string value.
        """
        pulumi.set(__self__, "bool_value", bool_value)
        pulumi.set(__self__, "double_value", double_value)
        pulumi.set(__self__, "int64_value", int64_value)
        pulumi.set(__self__, "proto_value", proto_value)
        pulumi.set(__self__, "string_value", string_value)

    @property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> bool:
        """
        Represents a boolean value.
        """
        return pulumi.get(self, "bool_value")

    @property
    @pulumi.getter(name="doubleValue")
    def double_value(self) -> float:
        """
        Represents a double value.
        """
        return pulumi.get(self, "double_value")

    @property
    @pulumi.getter(name="int64Value")
    def int64_value(self) -> str:
        """
        Represents an int64 value.
        """
        return pulumi.get(self, "int64_value")

    @property
    @pulumi.getter(name="protoValue")
    def proto_value(self) -> Mapping[str, str]:
        """
        Represents an 'Any' proto value.
        """
        return pulumi.get(self, "proto_value")

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> str:
        """
        Represents a string value.
        """
        return pulumi.get(self, "string_value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GoogleTypePostalAddressResponse(dict):
    """
    Represents a postal address, e.g. for postal delivery or payments addresses. Given a postal address, a postal service can deliver items to a premise, P.O. Box or similar. It is not intended to model geographical locations (roads, towns, mountains). In typical usage an address would be created via user input or from importing existing data, depending on the type of process. Advice on address input / editing: - Use an i18n-ready address widget such as https://github.com/google/libaddressinput) - Users should not be presented with UI elements for input or editing of fields outside countries where that field is used. For more guidance on how to use this schema, please see: https://support.google.com/business/answer/6397478
    """
    def __init__(__self__, *,
                 address_lines: Sequence[str],
                 administrative_area: str,
                 language_code: str,
                 locality: str,
                 organization: str,
                 postal_code: str,
                 recipients: Sequence[str],
                 region_code: str,
                 revision: int,
                 sorting_code: str,
                 sublocality: str):
        """
        Represents a postal address, e.g. for postal delivery or payments addresses. Given a postal address, a postal service can deliver items to a premise, P.O. Box or similar. It is not intended to model geographical locations (roads, towns, mountains). In typical usage an address would be created via user input or from importing existing data, depending on the type of process. Advice on address input / editing: - Use an i18n-ready address widget such as https://github.com/google/libaddressinput) - Users should not be presented with UI elements for input or editing of fields outside countries where that field is used. For more guidance on how to use this schema, please see: https://support.google.com/business/answer/6397478
        :param Sequence[str] address_lines: Unstructured address lines describing the lower levels of an address. Because values in address_lines do not have type information and may sometimes contain multiple values in a single field (e.g. "Austin, TX"), it is important that the line order is clear. The order of address lines should be "envelope order" for the country/region of the address. In places where this can vary (e.g. Japan), address_language is used to make it explicit (e.g. "ja" for large-to-small ordering and "ja-Latn" or "en" for small-to-large). This way, the most specific line of an address can be selected based on the language. The minimum permitted structural representation of an address consists of a region_code with all remaining information placed in the address_lines. It would be possible to format such an address very approximately without geocoding, but no semantic reasoning could be made about any of the address components until it was at least partially resolved. Creating an address only containing a region_code and address_lines, and then geocoding is the recommended way to handle completely unstructured addresses (as opposed to guessing which parts of the address should be localities or administrative areas).
        :param str administrative_area: Optional. Highest administrative subdivision which is used for postal addresses of a country or region. For example, this can be a state, a province, an oblast, or a prefecture. Specifically, for Spain this is the province and not the autonomous community (e.g. "Barcelona" and not "Catalonia"). Many countries don't use an administrative area in postal addresses. E.g. in Switzerland this should be left unpopulated.
        :param str language_code: Optional. BCP-47 language code of the contents of this address (if known). This is often the UI language of the input form or is expected to match one of the languages used in the address' country/region, or their transliterated equivalents. This can affect formatting in certain countries, but is not critical to the correctness of the data and will never affect any validation or other non-formatting related operations. If this value is not known, it should be omitted (rather than specifying a possibly incorrect default). Examples: "zh-Hant", "ja", "ja-Latn", "en".
        :param str locality: Optional. Generally refers to the city/town portion of the address. Examples: US city, IT comune, UK post town. In regions of the world where localities are not well defined or do not fit into this structure well, leave locality empty and use address_lines.
        :param str organization: Optional. The name of the organization at the address.
        :param str postal_code: Optional. Postal code of the address. Not all countries use or require postal codes to be present, but where they are used, they may trigger additional validation with other parts of the address (e.g. state/zip validation in the U.S.A.).
        :param Sequence[str] recipients: Optional. The recipient at the address. This field may, under certain circumstances, contain multiline information. For example, it might contain "care of" information.
        :param str region_code: Required. CLDR region code of the country/region of the address. This is never inferred and it is up to the user to ensure the value is correct. See http://cldr.unicode.org/ and http://www.unicode.org/cldr/charts/30/supplemental/territory_information.html for details. Example: "CH" for Switzerland.
        :param int revision: The schema revision of the `PostalAddress`. This must be set to 0, which is the latest revision. All new revisions **must** be backward compatible with old revisions.
        :param str sorting_code: Optional. Additional, country-specific, sorting code. This is not used in most regions. Where it is used, the value is either a string like "CEDEX", optionally followed by a number (e.g. "CEDEX 7"), or just a number alone, representing the "sector code" (Jamaica), "delivery area indicator" (Malawi) or "post office indicator" (e.g. Côte d'Ivoire).
        :param str sublocality: Optional. Sublocality of the address. For example, this can be neighborhoods, boroughs, districts.
        """
        pulumi.set(__self__, "address_lines", address_lines)
        pulumi.set(__self__, "administrative_area", administrative_area)
        pulumi.set(__self__, "language_code", language_code)
        pulumi.set(__self__, "locality", locality)
        pulumi.set(__self__, "organization", organization)
        pulumi.set(__self__, "postal_code", postal_code)
        pulumi.set(__self__, "recipients", recipients)
        pulumi.set(__self__, "region_code", region_code)
        pulumi.set(__self__, "revision", revision)
        pulumi.set(__self__, "sorting_code", sorting_code)
        pulumi.set(__self__, "sublocality", sublocality)

    @property
    @pulumi.getter(name="addressLines")
    def address_lines(self) -> Sequence[str]:
        """
        Unstructured address lines describing the lower levels of an address. Because values in address_lines do not have type information and may sometimes contain multiple values in a single field (e.g. "Austin, TX"), it is important that the line order is clear. The order of address lines should be "envelope order" for the country/region of the address. In places where this can vary (e.g. Japan), address_language is used to make it explicit (e.g. "ja" for large-to-small ordering and "ja-Latn" or "en" for small-to-large). This way, the most specific line of an address can be selected based on the language. The minimum permitted structural representation of an address consists of a region_code with all remaining information placed in the address_lines. It would be possible to format such an address very approximately without geocoding, but no semantic reasoning could be made about any of the address components until it was at least partially resolved. Creating an address only containing a region_code and address_lines, and then geocoding is the recommended way to handle completely unstructured addresses (as opposed to guessing which parts of the address should be localities or administrative areas).
        """
        return pulumi.get(self, "address_lines")

    @property
    @pulumi.getter(name="administrativeArea")
    def administrative_area(self) -> str:
        """
        Optional. Highest administrative subdivision which is used for postal addresses of a country or region. For example, this can be a state, a province, an oblast, or a prefecture. Specifically, for Spain this is the province and not the autonomous community (e.g. "Barcelona" and not "Catalonia"). Many countries don't use an administrative area in postal addresses. E.g. in Switzerland this should be left unpopulated.
        """
        return pulumi.get(self, "administrative_area")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> str:
        """
        Optional. BCP-47 language code of the contents of this address (if known). This is often the UI language of the input form or is expected to match one of the languages used in the address' country/region, or their transliterated equivalents. This can affect formatting in certain countries, but is not critical to the correctness of the data and will never affect any validation or other non-formatting related operations. If this value is not known, it should be omitted (rather than specifying a possibly incorrect default). Examples: "zh-Hant", "ja", "ja-Latn", "en".
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def locality(self) -> str:
        """
        Optional. Generally refers to the city/town portion of the address. Examples: US city, IT comune, UK post town. In regions of the world where localities are not well defined or do not fit into this structure well, leave locality empty and use address_lines.
        """
        return pulumi.get(self, "locality")

    @property
    @pulumi.getter
    def organization(self) -> str:
        """
        Optional. The name of the organization at the address.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> str:
        """
        Optional. Postal code of the address. Not all countries use or require postal codes to be present, but where they are used, they may trigger additional validation with other parts of the address (e.g. state/zip validation in the U.S.A.).
        """
        return pulumi.get(self, "postal_code")

    @property
    @pulumi.getter
    def recipients(self) -> Sequence[str]:
        """
        Optional. The recipient at the address. This field may, under certain circumstances, contain multiline information. For example, it might contain "care of" information.
        """
        return pulumi.get(self, "recipients")

    @property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> str:
        """
        Required. CLDR region code of the country/region of the address. This is never inferred and it is up to the user to ensure the value is correct. See http://cldr.unicode.org/ and http://www.unicode.org/cldr/charts/30/supplemental/territory_information.html for details. Example: "CH" for Switzerland.
        """
        return pulumi.get(self, "region_code")

    @property
    @pulumi.getter
    def revision(self) -> int:
        """
        The schema revision of the `PostalAddress`. This must be set to 0, which is the latest revision. All new revisions **must** be backward compatible with old revisions.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter(name="sortingCode")
    def sorting_code(self) -> str:
        """
        Optional. Additional, country-specific, sorting code. This is not used in most regions. Where it is used, the value is either a string like "CEDEX", optionally followed by a number (e.g. "CEDEX 7"), or just a number alone, representing the "sector code" (Jamaica), "delivery area indicator" (Malawi) or "post office indicator" (e.g. Côte d'Ivoire).
        """
        return pulumi.get(self, "sorting_code")

    @property
    @pulumi.getter
    def sublocality(self) -> str:
        """
        Optional. Sublocality of the address. For example, this can be neighborhoods, boroughs, districts.
        """
        return pulumi.get(self, "sublocality")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


