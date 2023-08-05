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

__all__ = ['RegionCluster']


class RegionCluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['ClusterConfigArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1beta2#clusteroperationmetadata).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Required. The cluster name. Cluster names within a project must be unique. Names of deleted clusters can be reused.
        :param pulumi.Input[pulumi.InputType['ClusterConfigArgs']] config: Required. The cluster config. Note that Dataproc may set default values, and values may change when clusters are updated.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster.
        :param pulumi.Input[str] project_id: Required. The Google Cloud Platform project ID that the cluster belongs to.
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

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['config'] = config
            __props__['labels'] = labels
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            __props__['cluster_uuid'] = None
            __props__['metrics'] = None
            __props__['status'] = None
            __props__['status_history'] = None
        super(RegionCluster, __self__).__init__(
            'gcp-native:dataproc/v1beta2:RegionCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegionCluster':
        """
        Get an existing RegionCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_name"] = None
        __props__["cluster_uuid"] = None
        __props__["config"] = None
        __props__["labels"] = None
        __props__["metrics"] = None
        __props__["project_id"] = None
        __props__["status"] = None
        __props__["status_history"] = None
        return RegionCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Required. The cluster name. Cluster names within a project must be unique. Names of deleted clusters can be reused.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> pulumi.Output[str]:
        """
        A cluster UUID (Unique Universal Identifier). Dataproc generates this value when it creates the cluster.
        """
        return pulumi.get(self, "cluster_uuid")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.ClusterConfigResponse']:
        """
        Required. The cluster config. Note that Dataproc may set default values, and values may change when clusters are updated.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def metrics(self) -> pulumi.Output['outputs.ClusterMetricsResponse']:
        """
        Contains cluster daemon metrics such as HDFS and YARN stats.Beta Feature: This report is available for testing purposes only. It may be changed before final release.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        Required. The Google Cloud Platform project ID that the cluster belongs to.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.ClusterStatusResponse']:
        """
        Cluster status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusHistory")
    def status_history(self) -> pulumi.Output[Sequence['outputs.ClusterStatusResponse']]:
        """
        The previous cluster status.
        """
        return pulumi.get(self, "status_history")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

