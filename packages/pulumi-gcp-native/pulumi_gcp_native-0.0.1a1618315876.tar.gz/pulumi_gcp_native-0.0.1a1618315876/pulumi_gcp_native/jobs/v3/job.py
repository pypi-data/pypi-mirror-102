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

__all__ = ['Job']


class Job(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 application_info: Optional[pulumi.Input[pulumi.InputType['ApplicationInfoArgs']]] = None,
                 company_display_name: Optional[pulumi.Input[str]] = None,
                 company_name: Optional[pulumi.Input[str]] = None,
                 compensation_info: Optional[pulumi.Input[pulumi.InputType['CompensationInfoArgs']]] = None,
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 degree_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 department: Optional[pulumi.Input[str]] = None,
                 derived_info: Optional[pulumi.Input[pulumi.InputType['JobDerivedInfoArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 employment_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 incentives: Optional[pulumi.Input[str]] = None,
                 job_benefits: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 job_end_time: Optional[pulumi.Input[str]] = None,
                 job_level: Optional[pulumi.Input[str]] = None,
                 job_start_time: Optional[pulumi.Input[str]] = None,
                 jobs_id: Optional[pulumi.Input[str]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 posting_create_time: Optional[pulumi.Input[str]] = None,
                 posting_expire_time: Optional[pulumi.Input[str]] = None,
                 posting_publish_time: Optional[pulumi.Input[str]] = None,
                 posting_region: Optional[pulumi.Input[str]] = None,
                 posting_update_time: Optional[pulumi.Input[str]] = None,
                 processing_options: Optional[pulumi.Input[pulumi.InputType['ProcessingOptionsArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 promotion_value: Optional[pulumi.Input[int]] = None,
                 qualifications: Optional[pulumi.Input[str]] = None,
                 requisition_id: Optional[pulumi.Input[str]] = None,
                 responsibilities: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new job. Typically, the job becomes searchable within 10 seconds, but it may take up to 5 minutes.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] addresses: Optional but strongly recommended for the best service experience. Location(s) where the employer is looking to hire for this job posting. Specifying the full street address(es) of the hiring location enables better API results, especially job searches by commute time. At most 50 locations are allowed for best search performance. If a job has more locations, it is suggested to split it into multiple jobs with unique requisition_ids (e.g. 'ReqA' becomes 'ReqA-1', 'ReqA-2', etc.) as multiple jobs with the same company_name, language_code and requisition_id are not allowed. If the original requisition_id must be preserved, a custom field should be used for storage. It is also suggested to group the locations that close to each other in the same job for better search experience. The maximum number of allowed characters is 500.
        :param pulumi.Input[pulumi.InputType['ApplicationInfoArgs']] application_info: Required. At least one field within ApplicationInfo must be specified. Job application information.
        :param pulumi.Input[str] company_display_name: Display name of the company listing the job.
        :param pulumi.Input[str] company_name: Required. The resource name of the company listing the job, such as "projects/api-test-project/companies/foo".
        :param pulumi.Input[pulumi.InputType['CompensationInfoArgs']] compensation_info: Optional. Job compensation information.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_attributes: Optional. A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields. The keys of the map are strings up to 64 bytes and must match the pattern: a-zA-Z*. For example, key0LikeThis or KEY_1_LIKE_THIS. At most 100 filterable and at most 100 unfilterable keys are supported. For filterable `string_values`, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable `string_values`, the maximum total size of `string_values` across all keys is 50KB.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] degree_types: Optional. The desired education degrees for the job, such as Bachelors, Masters.
        :param pulumi.Input[str] department: Optional. The department or functional area within the company with the open position. The maximum number of allowed characters is 255.
        :param pulumi.Input[pulumi.InputType['JobDerivedInfoArgs']] derived_info: Derived details about the job posting.
        :param pulumi.Input[str] description: Required. The description of the job, which typically includes a multi-paragraph description of the company and related information. Separate fields are provided on the job object for responsibilities, qualifications, and other job characteristics. Use of these separate job fields is recommended. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 100,000.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] employment_types: Optional. The employment type(s) of a job, for example, full time or part time.
        :param pulumi.Input[str] incentives: Optional. A description of bonus, commission, and other compensation incentives associated with the job not including salary or pay. The maximum number of allowed characters is 10,000.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] job_benefits: Optional. The benefits included with the job.
        :param pulumi.Input[str] job_end_time: Optional. The end timestamp of the job. Typically this field is used for contracting engagements. Invalid timestamps are ignored.
        :param pulumi.Input[str] job_level: Optional. The experience level associated with the job, such as "Entry Level".
        :param pulumi.Input[str] job_start_time: Optional. The start timestamp of the job in UTC time zone. Typically this field is used for contracting engagements. Invalid timestamps are ignored.
        :param pulumi.Input[str] language_code: Optional. The language of the posting. This field is distinct from any requirements for fluency that are associated with the job. Language codes must be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47){: class="external" target="_blank" }. If this field is unspecified and Job.description is present, detected language code based on Job.description is assigned, otherwise defaults to 'en_US'.
        :param pulumi.Input[str] name: Required during job update. The resource name for the job. This is generated by the service when a job is created. The format is "projects/{project_id}/jobs/{job_id}", for example, "projects/api-test-project/jobs/1234". Use of this field in job queries and API calls is preferred over the use of requisition_id since this value is unique.
        :param pulumi.Input[str] posting_create_time: The timestamp when this job posting was created.
        :param pulumi.Input[str] posting_expire_time: Optional but strongly recommended for the best service experience. The expiration timestamp of the job. After this timestamp, the job is marked as expired, and it no longer appears in search results. The expired job can't be deleted or listed by the DeleteJob and ListJobs APIs, but it can be retrieved with the GetJob API or updated with the UpdateJob API. An expired job can be updated and opened again by using a future expiration timestamp. Updating an expired job fails if there is another existing open job with same company_name, language_code and requisition_id. The expired jobs are retained in our system for 90 days. However, the overall expired job count cannot exceed 3 times the maximum of open jobs count over the past week, otherwise jobs with earlier expire time are cleaned first. Expired jobs are no longer accessible after they are cleaned out. Invalid timestamps are ignored, and treated as expire time not provided. Timestamp before the instant request is made is considered valid, the job will be treated as expired immediately. If this value is not provided at the time of job creation or is invalid, the job posting expires after 30 days from the job's creation time. For example, if the job was created on 2017/01/01 13:00AM UTC with an unspecified expiration date, the job expires after 2017/01/31 13:00AM UTC. If this value is not provided on job update, it depends on the field masks set by UpdateJobRequest.update_mask. If the field masks include expiry_time, or the masks are empty meaning that every field is updated, the job posting expires after 30 days from the job's last update time. Otherwise the expiration date isn't updated.
        :param pulumi.Input[str] posting_publish_time: Optional. The timestamp this job posting was most recently published. The default value is the time the request arrives at the server. Invalid timestamps are ignored.
        :param pulumi.Input[str] posting_region: Optional. The job PostingRegion (for example, state, country) throughout which the job is available. If this field is set, a LocationFilter in a search query within the job region finds this job posting if an exact location match isn't specified. If this field is set to PostingRegion.NATION or PostingRegion.ADMINISTRATIVE_AREA, setting job Job.addresses to the same location level as this field is strongly recommended.
        :param pulumi.Input[str] posting_update_time: The timestamp when this job posting was last updated.
        :param pulumi.Input[pulumi.InputType['ProcessingOptionsArgs']] processing_options: Optional. Options for job processing.
        :param pulumi.Input[int] promotion_value: Optional. A promotion value of the job, as determined by the client. The value determines the sort order of the jobs returned when searching for jobs using the featured jobs search call, with higher promotional values being returned first and ties being resolved by relevance sort. Only the jobs with a promotionValue >0 are returned in a FEATURED_JOB_SEARCH. Default value is 0, and negative values are treated as 0.
        :param pulumi.Input[str] qualifications: Optional. A description of the qualifications required to perform the job. The use of this field is recommended as an alternative to using the more general description field. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 10,000.
        :param pulumi.Input[str] requisition_id: Required. The requisition ID, also referred to as the posting ID, assigned by the client to identify a job. This field is intended to be used by clients for client identification and tracking of postings. A job is not allowed to be created if there is another job with the same [company_name], language_code and requisition_id. The maximum number of allowed characters is 255.
        :param pulumi.Input[str] responsibilities: Optional. A description of job responsibilities. The use of this field is recommended as an alternative to using the more general description field. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 10,000.
        :param pulumi.Input[str] title: Required. The title of the job, such as "Software Engineer" The maximum number of allowed characters is 500.
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

            __props__['addresses'] = addresses
            __props__['application_info'] = application_info
            __props__['company_display_name'] = company_display_name
            __props__['company_name'] = company_name
            __props__['compensation_info'] = compensation_info
            __props__['custom_attributes'] = custom_attributes
            __props__['degree_types'] = degree_types
            __props__['department'] = department
            __props__['derived_info'] = derived_info
            __props__['description'] = description
            __props__['employment_types'] = employment_types
            __props__['incentives'] = incentives
            __props__['job_benefits'] = job_benefits
            __props__['job_end_time'] = job_end_time
            __props__['job_level'] = job_level
            __props__['job_start_time'] = job_start_time
            if jobs_id is None and not opts.urn:
                raise TypeError("Missing required property 'jobs_id'")
            __props__['jobs_id'] = jobs_id
            __props__['language_code'] = language_code
            __props__['name'] = name
            __props__['posting_create_time'] = posting_create_time
            __props__['posting_expire_time'] = posting_expire_time
            __props__['posting_publish_time'] = posting_publish_time
            __props__['posting_region'] = posting_region
            __props__['posting_update_time'] = posting_update_time
            __props__['processing_options'] = processing_options
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['promotion_value'] = promotion_value
            __props__['qualifications'] = qualifications
            __props__['requisition_id'] = requisition_id
            __props__['responsibilities'] = responsibilities
            __props__['title'] = title
        super(Job, __self__).__init__(
            'gcp-native:jobs/v3:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["addresses"] = None
        __props__["application_info"] = None
        __props__["company_display_name"] = None
        __props__["company_name"] = None
        __props__["compensation_info"] = None
        __props__["custom_attributes"] = None
        __props__["degree_types"] = None
        __props__["department"] = None
        __props__["derived_info"] = None
        __props__["description"] = None
        __props__["employment_types"] = None
        __props__["incentives"] = None
        __props__["job_benefits"] = None
        __props__["job_end_time"] = None
        __props__["job_level"] = None
        __props__["job_start_time"] = None
        __props__["language_code"] = None
        __props__["name"] = None
        __props__["posting_create_time"] = None
        __props__["posting_expire_time"] = None
        __props__["posting_publish_time"] = None
        __props__["posting_region"] = None
        __props__["posting_update_time"] = None
        __props__["processing_options"] = None
        __props__["promotion_value"] = None
        __props__["qualifications"] = None
        __props__["requisition_id"] = None
        __props__["responsibilities"] = None
        __props__["title"] = None
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional but strongly recommended for the best service experience. Location(s) where the employer is looking to hire for this job posting. Specifying the full street address(es) of the hiring location enables better API results, especially job searches by commute time. At most 50 locations are allowed for best search performance. If a job has more locations, it is suggested to split it into multiple jobs with unique requisition_ids (e.g. 'ReqA' becomes 'ReqA-1', 'ReqA-2', etc.) as multiple jobs with the same company_name, language_code and requisition_id are not allowed. If the original requisition_id must be preserved, a custom field should be used for storage. It is also suggested to group the locations that close to each other in the same job for better search experience. The maximum number of allowed characters is 500.
        """
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter(name="applicationInfo")
    def application_info(self) -> pulumi.Output['outputs.ApplicationInfoResponse']:
        """
        Required. At least one field within ApplicationInfo must be specified. Job application information.
        """
        return pulumi.get(self, "application_info")

    @property
    @pulumi.getter(name="companyDisplayName")
    def company_display_name(self) -> pulumi.Output[str]:
        """
        Display name of the company listing the job.
        """
        return pulumi.get(self, "company_display_name")

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Output[str]:
        """
        Required. The resource name of the company listing the job, such as "projects/api-test-project/companies/foo".
        """
        return pulumi.get(self, "company_name")

    @property
    @pulumi.getter(name="compensationInfo")
    def compensation_info(self) -> pulumi.Output['outputs.CompensationInfoResponse']:
        """
        Optional. Job compensation information.
        """
        return pulumi.get(self, "compensation_info")

    @property
    @pulumi.getter(name="customAttributes")
    def custom_attributes(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields. The keys of the map are strings up to 64 bytes and must match the pattern: a-zA-Z*. For example, key0LikeThis or KEY_1_LIKE_THIS. At most 100 filterable and at most 100 unfilterable keys are supported. For filterable `string_values`, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable `string_values`, the maximum total size of `string_values` across all keys is 50KB.
        """
        return pulumi.get(self, "custom_attributes")

    @property
    @pulumi.getter(name="degreeTypes")
    def degree_types(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. The desired education degrees for the job, such as Bachelors, Masters.
        """
        return pulumi.get(self, "degree_types")

    @property
    @pulumi.getter
    def department(self) -> pulumi.Output[str]:
        """
        Optional. The department or functional area within the company with the open position. The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "department")

    @property
    @pulumi.getter(name="derivedInfo")
    def derived_info(self) -> pulumi.Output['outputs.JobDerivedInfoResponse']:
        """
        Derived details about the job posting.
        """
        return pulumi.get(self, "derived_info")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Required. The description of the job, which typically includes a multi-paragraph description of the company and related information. Separate fields are provided on the job object for responsibilities, qualifications, and other job characteristics. Use of these separate job fields is recommended. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 100,000.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="employmentTypes")
    def employment_types(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. The employment type(s) of a job, for example, full time or part time.
        """
        return pulumi.get(self, "employment_types")

    @property
    @pulumi.getter
    def incentives(self) -> pulumi.Output[str]:
        """
        Optional. A description of bonus, commission, and other compensation incentives associated with the job not including salary or pay. The maximum number of allowed characters is 10,000.
        """
        return pulumi.get(self, "incentives")

    @property
    @pulumi.getter(name="jobBenefits")
    def job_benefits(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. The benefits included with the job.
        """
        return pulumi.get(self, "job_benefits")

    @property
    @pulumi.getter(name="jobEndTime")
    def job_end_time(self) -> pulumi.Output[str]:
        """
        Optional. The end timestamp of the job. Typically this field is used for contracting engagements. Invalid timestamps are ignored.
        """
        return pulumi.get(self, "job_end_time")

    @property
    @pulumi.getter(name="jobLevel")
    def job_level(self) -> pulumi.Output[str]:
        """
        Optional. The experience level associated with the job, such as "Entry Level".
        """
        return pulumi.get(self, "job_level")

    @property
    @pulumi.getter(name="jobStartTime")
    def job_start_time(self) -> pulumi.Output[str]:
        """
        Optional. The start timestamp of the job in UTC time zone. Typically this field is used for contracting engagements. Invalid timestamps are ignored.
        """
        return pulumi.get(self, "job_start_time")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[str]:
        """
        Optional. The language of the posting. This field is distinct from any requirements for fluency that are associated with the job. Language codes must be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47){: class="external" target="_blank" }. If this field is unspecified and Job.description is present, detected language code based on Job.description is assigned, otherwise defaults to 'en_US'.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required during job update. The resource name for the job. This is generated by the service when a job is created. The format is "projects/{project_id}/jobs/{job_id}", for example, "projects/api-test-project/jobs/1234". Use of this field in job queries and API calls is preferred over the use of requisition_id since this value is unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="postingCreateTime")
    def posting_create_time(self) -> pulumi.Output[str]:
        """
        The timestamp when this job posting was created.
        """
        return pulumi.get(self, "posting_create_time")

    @property
    @pulumi.getter(name="postingExpireTime")
    def posting_expire_time(self) -> pulumi.Output[str]:
        """
        Optional but strongly recommended for the best service experience. The expiration timestamp of the job. After this timestamp, the job is marked as expired, and it no longer appears in search results. The expired job can't be deleted or listed by the DeleteJob and ListJobs APIs, but it can be retrieved with the GetJob API or updated with the UpdateJob API. An expired job can be updated and opened again by using a future expiration timestamp. Updating an expired job fails if there is another existing open job with same company_name, language_code and requisition_id. The expired jobs are retained in our system for 90 days. However, the overall expired job count cannot exceed 3 times the maximum of open jobs count over the past week, otherwise jobs with earlier expire time are cleaned first. Expired jobs are no longer accessible after they are cleaned out. Invalid timestamps are ignored, and treated as expire time not provided. Timestamp before the instant request is made is considered valid, the job will be treated as expired immediately. If this value is not provided at the time of job creation or is invalid, the job posting expires after 30 days from the job's creation time. For example, if the job was created on 2017/01/01 13:00AM UTC with an unspecified expiration date, the job expires after 2017/01/31 13:00AM UTC. If this value is not provided on job update, it depends on the field masks set by UpdateJobRequest.update_mask. If the field masks include expiry_time, or the masks are empty meaning that every field is updated, the job posting expires after 30 days from the job's last update time. Otherwise the expiration date isn't updated.
        """
        return pulumi.get(self, "posting_expire_time")

    @property
    @pulumi.getter(name="postingPublishTime")
    def posting_publish_time(self) -> pulumi.Output[str]:
        """
        Optional. The timestamp this job posting was most recently published. The default value is the time the request arrives at the server. Invalid timestamps are ignored.
        """
        return pulumi.get(self, "posting_publish_time")

    @property
    @pulumi.getter(name="postingRegion")
    def posting_region(self) -> pulumi.Output[str]:
        """
        Optional. The job PostingRegion (for example, state, country) throughout which the job is available. If this field is set, a LocationFilter in a search query within the job region finds this job posting if an exact location match isn't specified. If this field is set to PostingRegion.NATION or PostingRegion.ADMINISTRATIVE_AREA, setting job Job.addresses to the same location level as this field is strongly recommended.
        """
        return pulumi.get(self, "posting_region")

    @property
    @pulumi.getter(name="postingUpdateTime")
    def posting_update_time(self) -> pulumi.Output[str]:
        """
        The timestamp when this job posting was last updated.
        """
        return pulumi.get(self, "posting_update_time")

    @property
    @pulumi.getter(name="processingOptions")
    def processing_options(self) -> pulumi.Output['outputs.ProcessingOptionsResponse']:
        """
        Optional. Options for job processing.
        """
        return pulumi.get(self, "processing_options")

    @property
    @pulumi.getter(name="promotionValue")
    def promotion_value(self) -> pulumi.Output[int]:
        """
        Optional. A promotion value of the job, as determined by the client. The value determines the sort order of the jobs returned when searching for jobs using the featured jobs search call, with higher promotional values being returned first and ties being resolved by relevance sort. Only the jobs with a promotionValue >0 are returned in a FEATURED_JOB_SEARCH. Default value is 0, and negative values are treated as 0.
        """
        return pulumi.get(self, "promotion_value")

    @property
    @pulumi.getter
    def qualifications(self) -> pulumi.Output[str]:
        """
        Optional. A description of the qualifications required to perform the job. The use of this field is recommended as an alternative to using the more general description field. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 10,000.
        """
        return pulumi.get(self, "qualifications")

    @property
    @pulumi.getter(name="requisitionId")
    def requisition_id(self) -> pulumi.Output[str]:
        """
        Required. The requisition ID, also referred to as the posting ID, assigned by the client to identify a job. This field is intended to be used by clients for client identification and tracking of postings. A job is not allowed to be created if there is another job with the same [company_name], language_code and requisition_id. The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "requisition_id")

    @property
    @pulumi.getter
    def responsibilities(self) -> pulumi.Output[str]:
        """
        Optional. A description of job responsibilities. The use of this field is recommended as an alternative to using the more general description field. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 10,000.
        """
        return pulumi.get(self, "responsibilities")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        Required. The title of the job, such as "Software Engineer" The maximum number of allowed characters is 500.
        """
        return pulumi.get(self, "title")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

