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

__all__ = ['Company']


class Company(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 career_site_uri: Optional[pulumi.Input[str]] = None,
                 companies_id: Optional[pulumi.Input[str]] = None,
                 derived_info: Optional[pulumi.Input[pulumi.InputType['CompanyDerivedInfoArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 eeo_text: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 headquarters_address: Optional[pulumi.Input[str]] = None,
                 hiring_agency: Optional[pulumi.Input[bool]] = None,
                 image_uri: Optional[pulumi.Input[str]] = None,
                 keyword_searchable_job_custom_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 suspended: Optional[pulumi.Input[bool]] = None,
                 website_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new company entity.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] career_site_uri: Optional. The URI to employer's career site or careers page on the employer's web site, for example, "https://careers.google.com".
        :param pulumi.Input[pulumi.InputType['CompanyDerivedInfoArgs']] derived_info: Derived details about the company.
        :param pulumi.Input[str] display_name: Required. The display name of the company, for example, "Google LLC".
        :param pulumi.Input[str] eeo_text: Optional. Equal Employment Opportunity legal disclaimer text to be associated with all jobs, and typically to be displayed in all roles. The maximum number of allowed characters is 500.
        :param pulumi.Input[str] external_id: Required. Client side company identifier, used to uniquely identify the company. The maximum number of allowed characters is 255.
        :param pulumi.Input[str] headquarters_address: Optional. The street address of the company's main headquarters, which may be different from the job location. The service attempts to geolocate the provided address, and populates a more specific location wherever possible in DerivedInfo.headquarters_location.
        :param pulumi.Input[bool] hiring_agency: Optional. Set to true if it is the hiring agency that post jobs for other employers. Defaults to false if not provided.
        :param pulumi.Input[str] image_uri: Optional. A URI that hosts the employer's company logo.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keyword_searchable_job_custom_attributes: Optional. A list of keys of filterable Job.custom_attributes, whose corresponding `string_values` are used in keyword search. Jobs with `string_values` under these specified field keys are returned if any of the values matches the search keyword. Custom field values with parenthesis, brackets and special symbols won't be properly searchable, and those keyword queries need to be surrounded by quotes.
        :param pulumi.Input[str] name: Required during company update. The resource name for a company. This is generated by the service when a company is created. The format is "projects/{project_id}/companies/{company_id}", for example, "projects/api-test-project/companies/foo".
        :param pulumi.Input[str] size: Optional. The employer's company size.
        :param pulumi.Input[bool] suspended: Indicates whether a company is flagged to be suspended from public availability by the service when job content appears suspicious, abusive, or spammy.
        :param pulumi.Input[str] website_uri: Optional. The URI representing the company's primary web site or home page, for example, "https://www.google.com". The maximum number of allowed characters is 255.
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

            __props__['career_site_uri'] = career_site_uri
            if companies_id is None and not opts.urn:
                raise TypeError("Missing required property 'companies_id'")
            __props__['companies_id'] = companies_id
            __props__['derived_info'] = derived_info
            __props__['display_name'] = display_name
            __props__['eeo_text'] = eeo_text
            __props__['external_id'] = external_id
            __props__['headquarters_address'] = headquarters_address
            __props__['hiring_agency'] = hiring_agency
            __props__['image_uri'] = image_uri
            __props__['keyword_searchable_job_custom_attributes'] = keyword_searchable_job_custom_attributes
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['size'] = size
            __props__['suspended'] = suspended
            __props__['website_uri'] = website_uri
        super(Company, __self__).__init__(
            'gcp-native:jobs/v3:Company',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Company':
        """
        Get an existing Company resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["career_site_uri"] = None
        __props__["derived_info"] = None
        __props__["display_name"] = None
        __props__["eeo_text"] = None
        __props__["external_id"] = None
        __props__["headquarters_address"] = None
        __props__["hiring_agency"] = None
        __props__["image_uri"] = None
        __props__["keyword_searchable_job_custom_attributes"] = None
        __props__["name"] = None
        __props__["size"] = None
        __props__["suspended"] = None
        __props__["website_uri"] = None
        return Company(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="careerSiteUri")
    def career_site_uri(self) -> pulumi.Output[str]:
        """
        Optional. The URI to employer's career site or careers page on the employer's web site, for example, "https://careers.google.com".
        """
        return pulumi.get(self, "career_site_uri")

    @property
    @pulumi.getter(name="derivedInfo")
    def derived_info(self) -> pulumi.Output['outputs.CompanyDerivedInfoResponse']:
        """
        Derived details about the company.
        """
        return pulumi.get(self, "derived_info")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The display name of the company, for example, "Google LLC".
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="eeoText")
    def eeo_text(self) -> pulumi.Output[str]:
        """
        Optional. Equal Employment Opportunity legal disclaimer text to be associated with all jobs, and typically to be displayed in all roles. The maximum number of allowed characters is 500.
        """
        return pulumi.get(self, "eeo_text")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        """
        Required. Client side company identifier, used to uniquely identify the company. The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="headquartersAddress")
    def headquarters_address(self) -> pulumi.Output[str]:
        """
        Optional. The street address of the company's main headquarters, which may be different from the job location. The service attempts to geolocate the provided address, and populates a more specific location wherever possible in DerivedInfo.headquarters_location.
        """
        return pulumi.get(self, "headquarters_address")

    @property
    @pulumi.getter(name="hiringAgency")
    def hiring_agency(self) -> pulumi.Output[bool]:
        """
        Optional. Set to true if it is the hiring agency that post jobs for other employers. Defaults to false if not provided.
        """
        return pulumi.get(self, "hiring_agency")

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Output[str]:
        """
        Optional. A URI that hosts the employer's company logo.
        """
        return pulumi.get(self, "image_uri")

    @property
    @pulumi.getter(name="keywordSearchableJobCustomAttributes")
    def keyword_searchable_job_custom_attributes(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. A list of keys of filterable Job.custom_attributes, whose corresponding `string_values` are used in keyword search. Jobs with `string_values` under these specified field keys are returned if any of the values matches the search keyword. Custom field values with parenthesis, brackets and special symbols won't be properly searchable, and those keyword queries need to be surrounded by quotes.
        """
        return pulumi.get(self, "keyword_searchable_job_custom_attributes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required during company update. The resource name for a company. This is generated by the service when a company is created. The format is "projects/{project_id}/companies/{company_id}", for example, "projects/api-test-project/companies/foo".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[str]:
        """
        Optional. The employer's company size.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def suspended(self) -> pulumi.Output[bool]:
        """
        Indicates whether a company is flagged to be suspended from public availability by the service when job content appears suspicious, abusive, or spammy.
        """
        return pulumi.get(self, "suspended")

    @property
    @pulumi.getter(name="websiteUri")
    def website_uri(self) -> pulumi.Output[str]:
        """
        Optional. The URI representing the company's primary web site or home page, for example, "https://www.google.com". The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "website_uri")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

