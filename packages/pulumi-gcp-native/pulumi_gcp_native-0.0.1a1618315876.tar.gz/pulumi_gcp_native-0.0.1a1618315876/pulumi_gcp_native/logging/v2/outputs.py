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
    'BigQueryOptionsResponse',
    'BucketOptionsResponse',
    'ExplicitResponse',
    'ExponentialResponse',
    'LabelDescriptorResponse',
    'LinearResponse',
    'LogExclusionResponse',
    'MetricDescriptorMetadataResponse',
    'MetricDescriptorResponse',
]

@pulumi.output_type
class BigQueryOptionsResponse(dict):
    """
    Options that change functionality of a sink exporting data to BigQuery.
    """
    def __init__(__self__, *,
                 use_partitioned_tables: bool,
                 uses_timestamp_column_partitioning: bool):
        """
        Options that change functionality of a sink exporting data to BigQuery.
        :param bool use_partitioned_tables: Optional. Whether to use BigQuery's partition tables (https://cloud.google.com/bigquery/docs/partitioned-tables). By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned tables the date suffix is no longer present and special query syntax (https://cloud.google.com/bigquery/docs/querying-partitioned-tables) has to be used instead. In both cases, tables are sharded based on UTC timezone.
        :param bool uses_timestamp_column_partitioning: True if new timestamp column based partitioning is in use, false if legacy ingestion-time partitioning is in use. All new sinks will have this field set true and will use timestamp column based partitioning. If use_partitioned_tables is false, this value has no meaning and will be false. Legacy sinks using partitioned tables will have this field set to false.
        """
        pulumi.set(__self__, "use_partitioned_tables", use_partitioned_tables)
        pulumi.set(__self__, "uses_timestamp_column_partitioning", uses_timestamp_column_partitioning)

    @property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> bool:
        """
        Optional. Whether to use BigQuery's partition tables (https://cloud.google.com/bigquery/docs/partitioned-tables). By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned tables the date suffix is no longer present and special query syntax (https://cloud.google.com/bigquery/docs/querying-partitioned-tables) has to be used instead. In both cases, tables are sharded based on UTC timezone.
        """
        return pulumi.get(self, "use_partitioned_tables")

    @property
    @pulumi.getter(name="usesTimestampColumnPartitioning")
    def uses_timestamp_column_partitioning(self) -> bool:
        """
        True if new timestamp column based partitioning is in use, false if legacy ingestion-time partitioning is in use. All new sinks will have this field set true and will use timestamp column based partitioning. If use_partitioned_tables is false, this value has no meaning and will be false. Legacy sinks using partitioned tables will have this field set to false.
        """
        return pulumi.get(self, "uses_timestamp_column_partitioning")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class BucketOptionsResponse(dict):
    """
    BucketOptions describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. BucketOptions does not include the number of values in each bucket.A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite.
    """
    def __init__(__self__, *,
                 explicit_buckets: 'outputs.ExplicitResponse',
                 exponential_buckets: 'outputs.ExponentialResponse',
                 linear_buckets: 'outputs.LinearResponse'):
        """
        BucketOptions describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. BucketOptions does not include the number of values in each bucket.A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite.
        :param 'ExplicitResponseArgs' explicit_buckets: The explicit buckets.
        :param 'ExponentialResponseArgs' exponential_buckets: The exponential buckets.
        :param 'LinearResponseArgs' linear_buckets: The linear bucket.
        """
        pulumi.set(__self__, "explicit_buckets", explicit_buckets)
        pulumi.set(__self__, "exponential_buckets", exponential_buckets)
        pulumi.set(__self__, "linear_buckets", linear_buckets)

    @property
    @pulumi.getter(name="explicitBuckets")
    def explicit_buckets(self) -> 'outputs.ExplicitResponse':
        """
        The explicit buckets.
        """
        return pulumi.get(self, "explicit_buckets")

    @property
    @pulumi.getter(name="exponentialBuckets")
    def exponential_buckets(self) -> 'outputs.ExponentialResponse':
        """
        The exponential buckets.
        """
        return pulumi.get(self, "exponential_buckets")

    @property
    @pulumi.getter(name="linearBuckets")
    def linear_buckets(self) -> 'outputs.LinearResponse':
        """
        The linear bucket.
        """
        return pulumi.get(self, "linear_buckets")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ExplicitResponse(dict):
    """
    Specifies a set of buckets with arbitrary widths.There are size(bounds) + 1 (= N) buckets. Bucket i has the following boundaries:Upper bound (0 <= i < N-1): boundsi Lower bound (1 <= i < N); boundsi - 1The bounds field must contain at least one element. If bounds has only one element, then there are no finite buckets, and that single element is the common boundary of the overflow and underflow buckets.
    """
    def __init__(__self__, *,
                 bounds: Sequence[float]):
        """
        Specifies a set of buckets with arbitrary widths.There are size(bounds) + 1 (= N) buckets. Bucket i has the following boundaries:Upper bound (0 <= i < N-1): boundsi Lower bound (1 <= i < N); boundsi - 1The bounds field must contain at least one element. If bounds has only one element, then there are no finite buckets, and that single element is the common boundary of the overflow and underflow buckets.
        :param Sequence[float] bounds: The values must be monotonically increasing.
        """
        pulumi.set(__self__, "bounds", bounds)

    @property
    @pulumi.getter
    def bounds(self) -> Sequence[float]:
        """
        The values must be monotonically increasing.
        """
        return pulumi.get(self, "bounds")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ExponentialResponse(dict):
    """
    Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.There are num_finite_buckets + 2 (= N) buckets. Bucket i has the following boundaries:Upper bound (0 <= i < N-1): scale * (growth_factor ^ i). Lower bound (1 <= i < N): scale * (growth_factor ^ (i - 1)).
    """
    def __init__(__self__, *,
                 growth_factor: float,
                 num_finite_buckets: int,
                 scale: float):
        """
        Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.There are num_finite_buckets + 2 (= N) buckets. Bucket i has the following boundaries:Upper bound (0 <= i < N-1): scale * (growth_factor ^ i). Lower bound (1 <= i < N): scale * (growth_factor ^ (i - 1)).
        :param float growth_factor: Must be greater than 1.
        :param int num_finite_buckets: Must be greater than 0.
        :param float scale: Must be greater than 0.
        """
        pulumi.set(__self__, "growth_factor", growth_factor)
        pulumi.set(__self__, "num_finite_buckets", num_finite_buckets)
        pulumi.set(__self__, "scale", scale)

    @property
    @pulumi.getter(name="growthFactor")
    def growth_factor(self) -> float:
        """
        Must be greater than 1.
        """
        return pulumi.get(self, "growth_factor")

    @property
    @pulumi.getter(name="numFiniteBuckets")
    def num_finite_buckets(self) -> int:
        """
        Must be greater than 0.
        """
        return pulumi.get(self, "num_finite_buckets")

    @property
    @pulumi.getter
    def scale(self) -> float:
        """
        Must be greater than 0.
        """
        return pulumi.get(self, "scale")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LabelDescriptorResponse(dict):
    """
    A description of a label.
    """
    def __init__(__self__, *,
                 description: str,
                 key: str,
                 value_type: str):
        """
        A description of a label.
        :param str description: A human-readable description for the label.
        :param str key: The label key.
        :param str value_type: The type of data that can be assigned to the label.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value_type", value_type)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A human-readable description for the label.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The label key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> str:
        """
        The type of data that can be assigned to the label.
        """
        return pulumi.get(self, "value_type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LinearResponse(dict):
    """
    Specifies a linear sequence of buckets that all have the same width (except overflow and underflow). Each bucket represents a constant absolute uncertainty on the specific value in the bucket.There are num_finite_buckets + 2 (= N) buckets. Bucket i has the following boundaries:Upper bound (0 <= i < N-1): offset + (width * i). Lower bound (1 <= i < N): offset + (width * (i - 1)).
    """
    def __init__(__self__, *,
                 num_finite_buckets: int,
                 offset: float,
                 width: float):
        """
        Specifies a linear sequence of buckets that all have the same width (except overflow and underflow). Each bucket represents a constant absolute uncertainty on the specific value in the bucket.There are num_finite_buckets + 2 (= N) buckets. Bucket i has the following boundaries:Upper bound (0 <= i < N-1): offset + (width * i). Lower bound (1 <= i < N): offset + (width * (i - 1)).
        :param int num_finite_buckets: Must be greater than 0.
        :param float offset: Lower bound of the first bucket.
        :param float width: Must be greater than 0.
        """
        pulumi.set(__self__, "num_finite_buckets", num_finite_buckets)
        pulumi.set(__self__, "offset", offset)
        pulumi.set(__self__, "width", width)

    @property
    @pulumi.getter(name="numFiniteBuckets")
    def num_finite_buckets(self) -> int:
        """
        Must be greater than 0.
        """
        return pulumi.get(self, "num_finite_buckets")

    @property
    @pulumi.getter
    def offset(self) -> float:
        """
        Lower bound of the first bucket.
        """
        return pulumi.get(self, "offset")

    @property
    @pulumi.getter
    def width(self) -> float:
        """
        Must be greater than 0.
        """
        return pulumi.get(self, "width")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LogExclusionResponse(dict):
    """
    Specifies a set of log entries that are not to be stored in Logging. If your GCP resource receives a large volume of logs, you can use exclusions to reduce your chargeable logs. Exclusions are processed after log sinks, so you can export log entries before they are excluded. Note that organization-level and folder-level exclusions don't apply to child resources, and that you can't exclude audit log entries.
    """
    def __init__(__self__, *,
                 create_time: str,
                 description: str,
                 disabled: bool,
                 filter: str,
                 name: str,
                 update_time: str):
        """
        Specifies a set of log entries that are not to be stored in Logging. If your GCP resource receives a large volume of logs, you can use exclusions to reduce your chargeable logs. Exclusions are processed after log sinks, so you can export log entries before they are excluded. Note that organization-level and folder-level exclusions don't apply to child resources, and that you can't exclude audit log entries.
        :param str create_time: The creation timestamp of the exclusion.This field may not be present for older exclusions.
        :param str description: Optional. A description of this exclusion.
        :param bool disabled: Optional. If set to True, then this exclusion is disabled and it does not exclude any log entries. You can update an exclusion to change the value of this field.
        :param str filter: Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries) that matches the log entries to be excluded. By using the sample function (https://cloud.google.com/logging/docs/view/advanced-queries#sample), you can exclude less than 100% of the matching log entries. For example, the following query matches 99% of low-severity log entries from Google Cloud Storage buckets:"resource.type=gcs_bucket severity<ERROR sample(insertId, 0.99)"
        :param str name: Required. A client-assigned identifier, such as "load-balancer-exclusion". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric.
        :param str update_time: The last update timestamp of the exclusion.This field may not be present for older exclusions.
        """
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "disabled", disabled)
        pulumi.set(__self__, "filter", filter)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation timestamp of the exclusion.This field may not be present for older exclusions.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. A description of this exclusion.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disabled(self) -> bool:
        """
        Optional. If set to True, then this exclusion is disabled and it does not exclude any log entries. You can update an exclusion to change the value of this field.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def filter(self) -> str:
        """
        Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries) that matches the log entries to be excluded. By using the sample function (https://cloud.google.com/logging/docs/view/advanced-queries#sample), you can exclude less than 100% of the matching log entries. For example, the following query matches 99% of low-severity log entries from Google Cloud Storage buckets:"resource.type=gcs_bucket severity<ERROR sample(insertId, 0.99)"
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Required. A client-assigned identifier, such as "load-balancer-exclusion". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last update timestamp of the exclusion.This field may not be present for older exclusions.
        """
        return pulumi.get(self, "update_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MetricDescriptorMetadataResponse(dict):
    """
    Additional annotations that can be used to guide the usage of a metric.
    """
    def __init__(__self__, *,
                 ingest_delay: str,
                 sample_period: str):
        """
        Additional annotations that can be used to guide the usage of a metric.
        :param str ingest_delay: The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.
        :param str sample_period: The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.
        """
        pulumi.set(__self__, "ingest_delay", ingest_delay)
        pulumi.set(__self__, "sample_period", sample_period)

    @property
    @pulumi.getter(name="ingestDelay")
    def ingest_delay(self) -> str:
        """
        The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.
        """
        return pulumi.get(self, "ingest_delay")

    @property
    @pulumi.getter(name="samplePeriod")
    def sample_period(self) -> str:
        """
        The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.
        """
        return pulumi.get(self, "sample_period")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MetricDescriptorResponse(dict):
    """
    Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.
    """
    def __init__(__self__, *,
                 description: str,
                 display_name: str,
                 labels: Sequence['outputs.LabelDescriptorResponse'],
                 launch_stage: str,
                 metadata: 'outputs.MetricDescriptorMetadataResponse',
                 metric_kind: str,
                 monitored_resource_types: Sequence[str],
                 name: str,
                 type: str,
                 unit: str,
                 value_type: str):
        """
        Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.
        :param str description: A detailed description of the metric, which can be used in documentation.
        :param str display_name: A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.
        :param Sequence['LabelDescriptorResponseArgs'] labels: The set of labels that can be used to describe a specific instance of this metric type. For example, the appengine.googleapis.com/http/server/response_latencies metric type has a label for the HTTP response code, response_code, so you can look at latencies for successful responses or just for responses that failed.
        :param str launch_stage: Optional. The launch stage of the metric definition.
        :param 'MetricDescriptorMetadataResponseArgs' metadata: Optional. Metadata which can be used to guide usage of the metric.
        :param str metric_kind: Whether the metric records instantaneous values, changes to a value, etc. Some combinations of metric_kind and value_type might not be supported.
        :param Sequence[str] monitored_resource_types: Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.
        :param str name: The resource name of the metric descriptor.
        :param str type: The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name custom.googleapis.com or external.googleapis.com. Metric types should use a natural hierarchical grouping. For example: "custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies" 
        :param str unit: The units in which the metric value is reported. It is only applicable if the value_type is INT64, DOUBLE, or DISTRIBUTION. The unit defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of 0.02kBy might be displayed as 20By, and a value of 3523kBy might be displayed as 3.5MBy). However, if the unit is kBy, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an INT64 CUMULATIVE metric whose unit is s{CPU} (or equivalently 1s{CPU} or just s). If the job uses 12,005 CPU-seconds, then the value is written as 12005.Alternatively, if you want a custom metric to record data in a more granular way, you can create a DOUBLE CUMULATIVE metric whose unit is ks{CPU}, and then write the value 12.005 (which is 12005/1000), or use Kis{CPU} and write 11.723 (which is 12005/1024).The supported units are a subset of The Unified Code for Units of Measure (https://unitsofmeasure.org/ucum.html) standard:Basic units (UNIT) bit bit By byte s second min minute h hour d day 1 dimensionlessPrefixes (PREFIX) k kilo (10^3) M mega (10^6) G giga (10^9) T tera (10^12) P peta (10^15) E exa (10^18) Z zetta (10^21) Y yotta (10^24) m milli (10^-3) u micro (10^-6) n nano (10^-9) p pico (10^-12) f femto (10^-15) a atto (10^-18) z zepto (10^-21) y yocto (10^-24) Ki kibi (2^10) Mi mebi (2^20) Gi gibi (2^30) Ti tebi (2^40) Pi pebi (2^50)GrammarThe grammar also includes these connectors: / division or ratio (as an infix operator). For examples, kBy/{email} or MiBy/10ms (although you should almost never have /s in a metric unit; rates should always be computed at query time from the underlying cumulative or delta value). . multiplication or composition (as an infix operator). For examples, GBy.d or k{watt}.h.The grammar for a unit is as follows: Expression = Component { "." Component } { "/" Component } ; Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ] | Annotation | "1" ; Annotation = "{" NAME "}" ; Notes: Annotation is just a comment if it follows a UNIT. If the annotation is used alone, then the unit is equivalent to 1. For examples, {request}/s == 1/s, By{transmitted}/s == By/s. NAME is a sequence of non-blank printable ASCII characters not containing { or }. 1 represents a unitary dimensionless unit (https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in 1/s. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as 1/d or {new-users}/d (and a metric value 5 would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as 1000/d or k1/d or k{page_views}/d (and a metric value of 5.3 would mean "5300 page views per day"). % represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value 3 means "3 percent"). 10^2.% indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value 0.03 means "3 percent").
        :param str value_type: Whether the measurement is an integer, a floating-point number, etc. Some combinations of metric_kind and value_type might not be supported.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "labels", labels)
        pulumi.set(__self__, "launch_stage", launch_stage)
        pulumi.set(__self__, "metadata", metadata)
        pulumi.set(__self__, "metric_kind", metric_kind)
        pulumi.set(__self__, "monitored_resource_types", monitored_resource_types)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "unit", unit)
        pulumi.set(__self__, "value_type", value_type)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A detailed description of the metric, which can be used in documentation.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def labels(self) -> Sequence['outputs.LabelDescriptorResponse']:
        """
        The set of labels that can be used to describe a specific instance of this metric type. For example, the appengine.googleapis.com/http/server/response_latencies metric type has a label for the HTTP response code, response_code, so you can look at latencies for successful responses or just for responses that failed.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> str:
        """
        Optional. The launch stage of the metric definition.
        """
        return pulumi.get(self, "launch_stage")

    @property
    @pulumi.getter
    def metadata(self) -> 'outputs.MetricDescriptorMetadataResponse':
        """
        Optional. Metadata which can be used to guide usage of the metric.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="metricKind")
    def metric_kind(self) -> str:
        """
        Whether the metric records instantaneous values, changes to a value, etc. Some combinations of metric_kind and value_type might not be supported.
        """
        return pulumi.get(self, "metric_kind")

    @property
    @pulumi.getter(name="monitoredResourceTypes")
    def monitored_resource_types(self) -> Sequence[str]:
        """
        Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.
        """
        return pulumi.get(self, "monitored_resource_types")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the metric descriptor.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name custom.googleapis.com or external.googleapis.com. Metric types should use a natural hierarchical grouping. For example: "custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies" 
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def unit(self) -> str:
        """
        The units in which the metric value is reported. It is only applicable if the value_type is INT64, DOUBLE, or DISTRIBUTION. The unit defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of 0.02kBy might be displayed as 20By, and a value of 3523kBy might be displayed as 3.5MBy). However, if the unit is kBy, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an INT64 CUMULATIVE metric whose unit is s{CPU} (or equivalently 1s{CPU} or just s). If the job uses 12,005 CPU-seconds, then the value is written as 12005.Alternatively, if you want a custom metric to record data in a more granular way, you can create a DOUBLE CUMULATIVE metric whose unit is ks{CPU}, and then write the value 12.005 (which is 12005/1000), or use Kis{CPU} and write 11.723 (which is 12005/1024).The supported units are a subset of The Unified Code for Units of Measure (https://unitsofmeasure.org/ucum.html) standard:Basic units (UNIT) bit bit By byte s second min minute h hour d day 1 dimensionlessPrefixes (PREFIX) k kilo (10^3) M mega (10^6) G giga (10^9) T tera (10^12) P peta (10^15) E exa (10^18) Z zetta (10^21) Y yotta (10^24) m milli (10^-3) u micro (10^-6) n nano (10^-9) p pico (10^-12) f femto (10^-15) a atto (10^-18) z zepto (10^-21) y yocto (10^-24) Ki kibi (2^10) Mi mebi (2^20) Gi gibi (2^30) Ti tebi (2^40) Pi pebi (2^50)GrammarThe grammar also includes these connectors: / division or ratio (as an infix operator). For examples, kBy/{email} or MiBy/10ms (although you should almost never have /s in a metric unit; rates should always be computed at query time from the underlying cumulative or delta value). . multiplication or composition (as an infix operator). For examples, GBy.d or k{watt}.h.The grammar for a unit is as follows: Expression = Component { "." Component } { "/" Component } ; Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ] | Annotation | "1" ; Annotation = "{" NAME "}" ; Notes: Annotation is just a comment if it follows a UNIT. If the annotation is used alone, then the unit is equivalent to 1. For examples, {request}/s == 1/s, By{transmitted}/s == By/s. NAME is a sequence of non-blank printable ASCII characters not containing { or }. 1 represents a unitary dimensionless unit (https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in 1/s. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as 1/d or {new-users}/d (and a metric value 5 would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as 1000/d or k1/d or k{page_views}/d (and a metric value of 5.3 would mean "5300 page views per day"). % represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value 3 means "3 percent"). 10^2.% indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value 0.03 means "3 percent").
        """
        return pulumi.get(self, "unit")

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> str:
        """
        Whether the measurement is an integer, a floating-point number, etc. Some combinations of metric_kind and value_type might not be supported.
        """
        return pulumi.get(self, "value_type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


