# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import VMwareCloudSimpleClientConfiguration
from .operations import VMwareCloudSimpleClientOperationsMixin
from .operations import AvailableOperations
from .operations import DedicatedCloudNodeOperations
from .operations import DedicatedCloudServiceOperations
from .operations import SkusAvailabilityWithinRegionOperations
from .operations import PrivateCloudByRegionOperations
from .operations import ResourcePoolsByPCOperations
from .operations import ResourcePoolByPCOperations
from .operations import VirtualMachineTemplatesByPCOperations
from .operations import VirtualMachineTemplateByPCOperations
from .operations import VirtualNetworksByPCOperations
from .operations import VirtualNetworkByPCOperations
from .operations import UsagesWithinRegionOperations
from .operations import VirtualMachineOperations
from . import models


class VMwareCloudSimpleClient(VMwareCloudSimpleClientOperationsMixin, SDKClient):
    """Description of the new service

    :ivar config: Configuration for client.
    :vartype config: VMwareCloudSimpleClientConfiguration

    :ivar available_operations: AvailableOperations operations
    :vartype available_operations: azure.mgmt.vmwarecloudsimple.operations.AvailableOperations
    :ivar dedicated_cloud_node: DedicatedCloudNode operations
    :vartype dedicated_cloud_node: azure.mgmt.vmwarecloudsimple.operations.DedicatedCloudNodeOperations
    :ivar dedicated_cloud_service: DedicatedCloudService operations
    :vartype dedicated_cloud_service: azure.mgmt.vmwarecloudsimple.operations.DedicatedCloudServiceOperations
    :ivar skus_availability_within_region: SkusAvailabilityWithinRegion operations
    :vartype skus_availability_within_region: azure.mgmt.vmwarecloudsimple.operations.SkusAvailabilityWithinRegionOperations
    :ivar private_cloud_by_region: PrivateCloudByRegion operations
    :vartype private_cloud_by_region: azure.mgmt.vmwarecloudsimple.operations.PrivateCloudByRegionOperations
    :ivar resource_pools_by_pc: ResourcePoolsByPC operations
    :vartype resource_pools_by_pc: azure.mgmt.vmwarecloudsimple.operations.ResourcePoolsByPCOperations
    :ivar resource_pool_by_pc: ResourcePoolByPC operations
    :vartype resource_pool_by_pc: azure.mgmt.vmwarecloudsimple.operations.ResourcePoolByPCOperations
    :ivar virtual_machine_templates_by_pc: VirtualMachineTemplatesByPC operations
    :vartype virtual_machine_templates_by_pc: azure.mgmt.vmwarecloudsimple.operations.VirtualMachineTemplatesByPCOperations
    :ivar virtual_machine_template_by_pc: VirtualMachineTemplateByPC operations
    :vartype virtual_machine_template_by_pc: azure.mgmt.vmwarecloudsimple.operations.VirtualMachineTemplateByPCOperations
    :ivar virtual_networks_by_pc: VirtualNetworksByPC operations
    :vartype virtual_networks_by_pc: azure.mgmt.vmwarecloudsimple.operations.VirtualNetworksByPCOperations
    :ivar virtual_network_by_pc: VirtualNetworkByPC operations
    :vartype virtual_network_by_pc: azure.mgmt.vmwarecloudsimple.operations.VirtualNetworkByPCOperations
    :ivar usages_within_region: UsagesWithinRegion operations
    :vartype usages_within_region: azure.mgmt.vmwarecloudsimple.operations.UsagesWithinRegionOperations
    :ivar virtual_machine: VirtualMachine operations
    :vartype virtual_machine: azure.mgmt.vmwarecloudsimple.operations.VirtualMachineOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param referer: referer url
    :type referer: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, referer, region_id, subscription_id, base_url=None):

        self.config = VMwareCloudSimpleClientConfiguration(credentials, referer, region_id, subscription_id, base_url)
        super(VMwareCloudSimpleClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.available_operations = AvailableOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dedicated_cloud_node = DedicatedCloudNodeOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dedicated_cloud_service = DedicatedCloudServiceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.skus_availability_within_region = SkusAvailabilityWithinRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_cloud_by_region = PrivateCloudByRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resource_pools_by_pc = ResourcePoolsByPCOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resource_pool_by_pc = ResourcePoolByPCOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_templates_by_pc = VirtualMachineTemplatesByPCOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_template_by_pc = VirtualMachineTemplateByPCOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_networks_by_pc = VirtualNetworksByPCOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_network_by_pc = VirtualNetworkByPCOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages_within_region = UsagesWithinRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine = VirtualMachineOperations(
            self._client, self.config, self._serialize, self._deserialize)
