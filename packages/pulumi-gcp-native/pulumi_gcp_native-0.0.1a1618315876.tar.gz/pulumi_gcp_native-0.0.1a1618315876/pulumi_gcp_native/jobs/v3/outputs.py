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
    'ApplicationInfoResponse',
    'CompanyDerivedInfoResponse',
    'CompensationEntryResponse',
    'CompensationInfoResponse',
    'CompensationRangeResponse',
    'JobDerivedInfoResponse',
    'LatLngResponse',
    'LocationResponse',
    'MoneyResponse',
    'PostalAddressResponse',
    'ProcessingOptionsResponse',
]

@pulumi.output_type
class ApplicationInfoResponse(dict):
    """
    Application related details of a job posting.
    """
    def __init__(__self__, *,
                 emails: Sequence[str],
                 instruction: str,
                 uris: Sequence[str]):
        """
        Application related details of a job posting.
        :param Sequence[str] emails: Optional but at least one of uris, emails or instruction must be specified. Use this field to specify email address(es) to which resumes or applications can be sent. The maximum number of allowed characters for each entry is 255.
        :param str instruction: Optional but at least one of uris, emails or instruction must be specified. Use this field to provide instructions, such as "Mail your application to ...", that a candidate can follow to apply for the job. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 3,000.
        :param Sequence[str] uris: Optional but at least one of uris, emails or instruction must be specified. Use this URI field to direct an applicant to a website, for example to link to an online application form. The maximum number of allowed characters for each entry is 2,000.
        """
        pulumi.set(__self__, "emails", emails)
        pulumi.set(__self__, "instruction", instruction)
        pulumi.set(__self__, "uris", uris)

    @property
    @pulumi.getter
    def emails(self) -> Sequence[str]:
        """
        Optional but at least one of uris, emails or instruction must be specified. Use this field to specify email address(es) to which resumes or applications can be sent. The maximum number of allowed characters for each entry is 255.
        """
        return pulumi.get(self, "emails")

    @property
    @pulumi.getter
    def instruction(self) -> str:
        """
        Optional but at least one of uris, emails or instruction must be specified. Use this field to provide instructions, such as "Mail your application to ...", that a candidate can follow to apply for the job. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 3,000.
        """
        return pulumi.get(self, "instruction")

    @property
    @pulumi.getter
    def uris(self) -> Sequence[str]:
        """
        Optional but at least one of uris, emails or instruction must be specified. Use this URI field to direct an applicant to a website, for example to link to an online application form. The maximum number of allowed characters for each entry is 2,000.
        """
        return pulumi.get(self, "uris")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CompanyDerivedInfoResponse(dict):
    """
    Derived details about the company.
    """
    def __init__(__self__, *,
                 headquarters_location: 'outputs.LocationResponse'):
        """
        Derived details about the company.
        :param 'LocationResponseArgs' headquarters_location: A structured headquarters location of the company, resolved from Company.hq_location if provided.
        """
        pulumi.set(__self__, "headquarters_location", headquarters_location)

    @property
    @pulumi.getter(name="headquartersLocation")
    def headquarters_location(self) -> 'outputs.LocationResponse':
        """
        A structured headquarters location of the company, resolved from Company.hq_location if provided.
        """
        return pulumi.get(self, "headquarters_location")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CompensationEntryResponse(dict):
    """
    A compensation entry that represents one component of compensation, such as base pay, bonus, or other compensation type. Annualization: One compensation entry can be annualized if - it contains valid amount or range. - and its expected_units_per_year is set or can be derived. Its annualized range is determined as (amount or range) times expected_units_per_year.
    """
    def __init__(__self__, *,
                 amount: 'outputs.MoneyResponse',
                 description: str,
                 expected_units_per_year: float,
                 range: 'outputs.CompensationRangeResponse',
                 type: str,
                 unit: str):
        """
        A compensation entry that represents one component of compensation, such as base pay, bonus, or other compensation type. Annualization: One compensation entry can be annualized if - it contains valid amount or range. - and its expected_units_per_year is set or can be derived. Its annualized range is determined as (amount or range) times expected_units_per_year.
        :param 'MoneyResponseArgs' amount: Optional. Compensation amount.
        :param str description: Optional. Compensation description. For example, could indicate equity terms or provide additional context to an estimated bonus.
        :param float expected_units_per_year: Optional. Expected number of units paid each year. If not specified, when Job.employment_types is FULLTIME, a default value is inferred based on unit. Default values: - HOURLY: 2080 - DAILY: 260 - WEEKLY: 52 - MONTHLY: 12 - ANNUAL: 1
        :param 'CompensationRangeResponseArgs' range: Optional. Compensation range.
        :param str type: Optional. Compensation type. Default is CompensationUnit.COMPENSATION_TYPE_UNSPECIFIED.
        :param str unit: Optional. Frequency of the specified amount. Default is CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED.
        """
        pulumi.set(__self__, "amount", amount)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "expected_units_per_year", expected_units_per_year)
        pulumi.set(__self__, "range", range)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter
    def amount(self) -> 'outputs.MoneyResponse':
        """
        Optional. Compensation amount.
        """
        return pulumi.get(self, "amount")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. Compensation description. For example, could indicate equity terms or provide additional context to an estimated bonus.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expectedUnitsPerYear")
    def expected_units_per_year(self) -> float:
        """
        Optional. Expected number of units paid each year. If not specified, when Job.employment_types is FULLTIME, a default value is inferred based on unit. Default values: - HOURLY: 2080 - DAILY: 260 - WEEKLY: 52 - MONTHLY: 12 - ANNUAL: 1
        """
        return pulumi.get(self, "expected_units_per_year")

    @property
    @pulumi.getter
    def range(self) -> 'outputs.CompensationRangeResponse':
        """
        Optional. Compensation range.
        """
        return pulumi.get(self, "range")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Optional. Compensation type. Default is CompensationUnit.COMPENSATION_TYPE_UNSPECIFIED.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def unit(self) -> str:
        """
        Optional. Frequency of the specified amount. Default is CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED.
        """
        return pulumi.get(self, "unit")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CompensationInfoResponse(dict):
    """
    Job compensation details.
    """
    def __init__(__self__, *,
                 annualized_base_compensation_range: 'outputs.CompensationRangeResponse',
                 annualized_total_compensation_range: 'outputs.CompensationRangeResponse',
                 entries: Sequence['outputs.CompensationEntryResponse']):
        """
        Job compensation details.
        :param 'CompensationRangeResponseArgs' annualized_base_compensation_range: Annualized base compensation range. Computed as base compensation entry's CompensationEntry.compensation times CompensationEntry.expected_units_per_year. See CompensationEntry for explanation on compensation annualization.
        :param 'CompensationRangeResponseArgs' annualized_total_compensation_range: Annualized total compensation range. Computed as all compensation entries' CompensationEntry.compensation times CompensationEntry.expected_units_per_year. See CompensationEntry for explanation on compensation annualization.
        :param Sequence['CompensationEntryResponseArgs'] entries: Optional. Job compensation information. At most one entry can be of type CompensationInfo.CompensationType.BASE, which is referred as ** base compensation entry ** for the job.
        """
        pulumi.set(__self__, "annualized_base_compensation_range", annualized_base_compensation_range)
        pulumi.set(__self__, "annualized_total_compensation_range", annualized_total_compensation_range)
        pulumi.set(__self__, "entries", entries)

    @property
    @pulumi.getter(name="annualizedBaseCompensationRange")
    def annualized_base_compensation_range(self) -> 'outputs.CompensationRangeResponse':
        """
        Annualized base compensation range. Computed as base compensation entry's CompensationEntry.compensation times CompensationEntry.expected_units_per_year. See CompensationEntry for explanation on compensation annualization.
        """
        return pulumi.get(self, "annualized_base_compensation_range")

    @property
    @pulumi.getter(name="annualizedTotalCompensationRange")
    def annualized_total_compensation_range(self) -> 'outputs.CompensationRangeResponse':
        """
        Annualized total compensation range. Computed as all compensation entries' CompensationEntry.compensation times CompensationEntry.expected_units_per_year. See CompensationEntry for explanation on compensation annualization.
        """
        return pulumi.get(self, "annualized_total_compensation_range")

    @property
    @pulumi.getter
    def entries(self) -> Sequence['outputs.CompensationEntryResponse']:
        """
        Optional. Job compensation information. At most one entry can be of type CompensationInfo.CompensationType.BASE, which is referred as ** base compensation entry ** for the job.
        """
        return pulumi.get(self, "entries")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CompensationRangeResponse(dict):
    """
    Compensation range.
    """
    def __init__(__self__, *,
                 max_compensation: 'outputs.MoneyResponse',
                 min_compensation: 'outputs.MoneyResponse'):
        """
        Compensation range.
        :param 'MoneyResponseArgs' max_compensation: Optional. The maximum amount of compensation. If left empty, the value is set to a maximal compensation value and the currency code is set to match the currency code of min_compensation.
        :param 'MoneyResponseArgs' min_compensation: Optional. The minimum amount of compensation. If left empty, the value is set to zero and the currency code is set to match the currency code of max_compensation.
        """
        pulumi.set(__self__, "max_compensation", max_compensation)
        pulumi.set(__self__, "min_compensation", min_compensation)

    @property
    @pulumi.getter(name="maxCompensation")
    def max_compensation(self) -> 'outputs.MoneyResponse':
        """
        Optional. The maximum amount of compensation. If left empty, the value is set to a maximal compensation value and the currency code is set to match the currency code of min_compensation.
        """
        return pulumi.get(self, "max_compensation")

    @property
    @pulumi.getter(name="minCompensation")
    def min_compensation(self) -> 'outputs.MoneyResponse':
        """
        Optional. The minimum amount of compensation. If left empty, the value is set to zero and the currency code is set to match the currency code of max_compensation.
        """
        return pulumi.get(self, "min_compensation")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class JobDerivedInfoResponse(dict):
    """
    Output only. Derived details about the job posting.
    """
    def __init__(__self__, *,
                 job_categories: Sequence[str],
                 locations: Sequence['outputs.LocationResponse']):
        """
        Output only. Derived details about the job posting.
        :param Sequence[str] job_categories: Job categories derived from Job.title and Job.description.
        :param Sequence['LocationResponseArgs'] locations: Structured locations of the job, resolved from Job.addresses. locations are exactly matched to Job.addresses in the same order.
        """
        pulumi.set(__self__, "job_categories", job_categories)
        pulumi.set(__self__, "locations", locations)

    @property
    @pulumi.getter(name="jobCategories")
    def job_categories(self) -> Sequence[str]:
        """
        Job categories derived from Job.title and Job.description.
        """
        return pulumi.get(self, "job_categories")

    @property
    @pulumi.getter
    def locations(self) -> Sequence['outputs.LocationResponse']:
        """
        Structured locations of the job, resolved from Job.addresses. locations are exactly matched to Job.addresses in the same order.
        """
        return pulumi.get(self, "locations")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LatLngResponse(dict):
    """
    An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this must conform to the WGS84 standard. Values must be within normalized ranges.
    """
    def __init__(__self__, *,
                 latitude: float,
                 longitude: float):
        """
        An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this must conform to the WGS84 standard. Values must be within normalized ranges.
        :param float latitude: The latitude in degrees. It must be in the range [-90.0, +90.0].
        :param float longitude: The longitude in degrees. It must be in the range [-180.0, +180.0].
        """
        pulumi.set(__self__, "latitude", latitude)
        pulumi.set(__self__, "longitude", longitude)

    @property
    @pulumi.getter
    def latitude(self) -> float:
        """
        The latitude in degrees. It must be in the range [-90.0, +90.0].
        """
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter
    def longitude(self) -> float:
        """
        The longitude in degrees. It must be in the range [-180.0, +180.0].
        """
        return pulumi.get(self, "longitude")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LocationResponse(dict):
    """
    Output only. A resource that represents a location with full geographic information.
    """
    def __init__(__self__, *,
                 lat_lng: 'outputs.LatLngResponse',
                 location_type: str,
                 postal_address: 'outputs.PostalAddressResponse',
                 radius_in_miles: float):
        """
        Output only. A resource that represents a location with full geographic information.
        :param 'LatLngResponseArgs' lat_lng: An object representing a latitude/longitude pair.
        :param str location_type: The type of a location, which corresponds to the address lines field of PostalAddress. For example, "Downtown, Atlanta, GA, USA" has a type of LocationType#NEIGHBORHOOD, and "Kansas City, KS, USA" has a type of LocationType#LOCALITY.
        :param 'PostalAddressResponseArgs' postal_address: Postal address of the location that includes human readable information, such as postal delivery and payments addresses. Given a postal address, a postal service can deliver items to a premises, P.O. Box, or other delivery location.
        :param float radius_in_miles: Radius in miles of the job location. This value is derived from the location bounding box in which a circle with the specified radius centered from LatLng covers the area associated with the job location. For example, currently, "Mountain View, CA, USA" has a radius of 6.17 miles.
        """
        pulumi.set(__self__, "lat_lng", lat_lng)
        pulumi.set(__self__, "location_type", location_type)
        pulumi.set(__self__, "postal_address", postal_address)
        pulumi.set(__self__, "radius_in_miles", radius_in_miles)

    @property
    @pulumi.getter(name="latLng")
    def lat_lng(self) -> 'outputs.LatLngResponse':
        """
        An object representing a latitude/longitude pair.
        """
        return pulumi.get(self, "lat_lng")

    @property
    @pulumi.getter(name="locationType")
    def location_type(self) -> str:
        """
        The type of a location, which corresponds to the address lines field of PostalAddress. For example, "Downtown, Atlanta, GA, USA" has a type of LocationType#NEIGHBORHOOD, and "Kansas City, KS, USA" has a type of LocationType#LOCALITY.
        """
        return pulumi.get(self, "location_type")

    @property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> 'outputs.PostalAddressResponse':
        """
        Postal address of the location that includes human readable information, such as postal delivery and payments addresses. Given a postal address, a postal service can deliver items to a premises, P.O. Box, or other delivery location.
        """
        return pulumi.get(self, "postal_address")

    @property
    @pulumi.getter(name="radiusInMiles")
    def radius_in_miles(self) -> float:
        """
        Radius in miles of the job location. This value is derived from the location bounding box in which a circle with the specified radius centered from LatLng covers the area associated with the job location. For example, currently, "Mountain View, CA, USA" has a radius of 6.17 miles.
        """
        return pulumi.get(self, "radius_in_miles")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MoneyResponse(dict):
    """
    Represents an amount of money with its currency type.
    """
    def __init__(__self__, *,
                 currency_code: str,
                 nanos: int,
                 units: str):
        """
        Represents an amount of money with its currency type.
        :param str currency_code: The three-letter currency code defined in ISO 4217.
        :param int nanos: Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
        :param str units: The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.
        """
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "nanos", nanos)
        pulumi.set(__self__, "units", units)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        """
        The three-letter currency code defined in ISO 4217.
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def nanos(self) -> int:
        """
        Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
        """
        return pulumi.get(self, "nanos")

    @property
    @pulumi.getter
    def units(self) -> str:
        """
        The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.
        """
        return pulumi.get(self, "units")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PostalAddressResponse(dict):
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


@pulumi.output_type
class ProcessingOptionsResponse(dict):
    """
    Input only. Options for job processing.
    """
    def __init__(__self__, *,
                 disable_street_address_resolution: bool,
                 html_sanitization: str):
        """
        Input only. Options for job processing.
        :param bool disable_street_address_resolution: Optional. If set to `true`, the service does not attempt to resolve a more precise address for the job.
        :param str html_sanitization: Optional. Option for job HTML content sanitization. Applied fields are: * description * applicationInfo.instruction * incentives * qualifications * responsibilities HTML tags in these fields may be stripped if sanitiazation is not disabled. Defaults to HtmlSanitization.SIMPLE_FORMATTING_ONLY.
        """
        pulumi.set(__self__, "disable_street_address_resolution", disable_street_address_resolution)
        pulumi.set(__self__, "html_sanitization", html_sanitization)

    @property
    @pulumi.getter(name="disableStreetAddressResolution")
    def disable_street_address_resolution(self) -> bool:
        """
        Optional. If set to `true`, the service does not attempt to resolve a more precise address for the job.
        """
        return pulumi.get(self, "disable_street_address_resolution")

    @property
    @pulumi.getter(name="htmlSanitization")
    def html_sanitization(self) -> str:
        """
        Optional. Option for job HTML content sanitization. Applied fields are: * description * applicationInfo.instruction * incentives * qualifications * responsibilities HTML tags in these fields may be stripped if sanitiazation is not disabled. Defaults to HtmlSanitization.SIMPLE_FORMATTING_ONLY.
        """
        return pulumi.get(self, "html_sanitization")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


