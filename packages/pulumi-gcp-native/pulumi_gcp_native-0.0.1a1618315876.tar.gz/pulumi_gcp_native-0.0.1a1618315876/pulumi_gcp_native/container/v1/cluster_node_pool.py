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

__all__ = ['ClusterNodePool']


class ClusterNodePool(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autoscaling: Optional[pulumi.Input[pulumi.InputType['NodePoolAutoscalingArgs']]] = None,
                 clusters_id: Optional[pulumi.Input[str]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StatusConditionArgs']]]]] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['NodeConfigArgs']]] = None,
                 initial_node_count: Optional[pulumi.Input[int]] = None,
                 instance_group_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 management: Optional[pulumi.Input[pulumi.InputType['NodeManagementArgs']]] = None,
                 max_pods_constraint: Optional[pulumi.Input[pulumi.InputType['MaxPodsConstraintArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_pools_id: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 pod_ipv4_cidr_size: Optional[pulumi.Input[int]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 upgrade_settings: Optional[pulumi.Input[pulumi.InputType['UpgradeSettingsArgs']]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a node pool for a cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['NodePoolAutoscalingArgs']] autoscaling: Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StatusConditionArgs']]]] conditions: Which conditions caused the current node pool state.
        :param pulumi.Input[pulumi.InputType['NodeConfigArgs']] config: The node configuration of the pool.
        :param pulumi.Input[int] initial_node_count: The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_group_urls: [Output only] The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located. If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead. Warning: changing node pool locations will result in nodes being added and/or removed.
        :param pulumi.Input[pulumi.InputType['NodeManagementArgs']] management: NodeManagement configuration for this NodePool.
        :param pulumi.Input[pulumi.InputType['MaxPodsConstraintArgs']] max_pods_constraint: The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool.
        :param pulumi.Input[str] name: The name of the node pool.
        :param pulumi.Input[str] parent: The parent (project, location, cluster id) where the node pool will be created. Specified in the format `projects/*/locations/*/clusters/*`.
        :param pulumi.Input[int] pod_ipv4_cidr_size: [Output only] The pod CIDR block size per node in this node pool.
        :param pulumi.Input[str] self_link: [Output only] Server-defined URL for the resource.
        :param pulumi.Input[str] status: [Output only] The status of the nodes in this pool instance.
        :param pulumi.Input[pulumi.InputType['UpgradeSettingsArgs']] upgrade_settings: Upgrade settings control disruption and speed of the upgrade.
        :param pulumi.Input[str] version: The version of the Kubernetes of this node.
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

            __props__['autoscaling'] = autoscaling
            if clusters_id is None and not opts.urn:
                raise TypeError("Missing required property 'clusters_id'")
            __props__['clusters_id'] = clusters_id
            __props__['conditions'] = conditions
            __props__['config'] = config
            __props__['initial_node_count'] = initial_node_count
            __props__['instance_group_urls'] = instance_group_urls
            __props__['locations'] = locations
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['management'] = management
            __props__['max_pods_constraint'] = max_pods_constraint
            __props__['name'] = name
            if node_pools_id is None and not opts.urn:
                raise TypeError("Missing required property 'node_pools_id'")
            __props__['node_pools_id'] = node_pools_id
            __props__['parent'] = parent
            __props__['pod_ipv4_cidr_size'] = pod_ipv4_cidr_size
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['self_link'] = self_link
            __props__['status'] = status
            __props__['upgrade_settings'] = upgrade_settings
            __props__['version'] = version
        super(ClusterNodePool, __self__).__init__(
            'gcp-native:container/v1:ClusterNodePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ClusterNodePool':
        """
        Get an existing ClusterNodePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["autoscaling"] = None
        __props__["conditions"] = None
        __props__["config"] = None
        __props__["initial_node_count"] = None
        __props__["instance_group_urls"] = None
        __props__["locations"] = None
        __props__["management"] = None
        __props__["max_pods_constraint"] = None
        __props__["name"] = None
        __props__["pod_ipv4_cidr_size"] = None
        __props__["self_link"] = None
        __props__["status"] = None
        __props__["upgrade_settings"] = None
        __props__["version"] = None
        return ClusterNodePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def autoscaling(self) -> pulumi.Output['outputs.NodePoolAutoscalingResponse']:
        """
        Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present.
        """
        return pulumi.get(self, "autoscaling")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence['outputs.StatusConditionResponse']]:
        """
        Which conditions caused the current node pool state.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.NodeConfigResponse']:
        """
        The node configuration of the pool.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> pulumi.Output[int]:
        """
        The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota.
        """
        return pulumi.get(self, "initial_node_count")

    @property
    @pulumi.getter(name="instanceGroupUrls")
    def instance_group_urls(self) -> pulumi.Output[Sequence[str]]:
        """
        [Output only] The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool.
        """
        return pulumi.get(self, "instance_group_urls")

    @property
    @pulumi.getter
    def locations(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located. If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead. Warning: changing node pool locations will result in nodes being added and/or removed.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def management(self) -> pulumi.Output['outputs.NodeManagementResponse']:
        """
        NodeManagement configuration for this NodePool.
        """
        return pulumi.get(self, "management")

    @property
    @pulumi.getter(name="maxPodsConstraint")
    def max_pods_constraint(self) -> pulumi.Output['outputs.MaxPodsConstraintResponse']:
        """
        The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool.
        """
        return pulumi.get(self, "max_pods_constraint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the node pool.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="podIpv4CidrSize")
    def pod_ipv4_cidr_size(self) -> pulumi.Output[int]:
        """
        [Output only] The pod CIDR block size per node in this node pool.
        """
        return pulumi.get(self, "pod_ipv4_cidr_size")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        [Output only] The status of the nodes in this pool instance.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> pulumi.Output['outputs.UpgradeSettingsResponse']:
        """
        Upgrade settings control disruption and speed of the upgrade.
        """
        return pulumi.get(self, "upgrade_settings")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the Kubernetes of this node.
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

