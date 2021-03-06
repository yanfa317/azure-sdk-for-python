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
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.managed_networks_operations import ManagedNetworksOperations
from .operations.scope_assignments_operations import ScopeAssignmentsOperations
from .operations.managed_network_groups_operations import ManagedNetworkGroupsOperations
from .operations.managed_network_peering_policies_operations import ManagedNetworkPeeringPoliciesOperations
from .operations.operations import Operations
from . import models


class ManagedNetworkManagementClientConfiguration(AzureConfiguration):
    """Configuration for ManagedNetworkManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ManagedNetworkManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-network/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ManagedNetworkManagementClient(SDKClient):
    """The Microsoft Azure Managed Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to programmatically view, control, change, and monitor your entire Azure network centrally and with ease.

    :ivar config: Configuration for client.
    :vartype config: ManagedNetworkManagementClientConfiguration

    :ivar managed_networks: ManagedNetworks operations
    :vartype managed_networks: azure.mgmt.managednetwork.v2019_06_01_pre.operations.ManagedNetworksOperations
    :ivar scope_assignments: ScopeAssignments operations
    :vartype scope_assignments: azure.mgmt.managednetwork.v2019_06_01_pre.operations.ScopeAssignmentsOperations
    :ivar managed_network_groups: ManagedNetworkGroups operations
    :vartype managed_network_groups: azure.mgmt.managednetwork.v2019_06_01_pre.operations.ManagedNetworkGroupsOperations
    :ivar managed_network_peering_policies: ManagedNetworkPeeringPolicies operations
    :vartype managed_network_peering_policies: azure.mgmt.managednetwork.v2019_06_01_pre.operations.ManagedNetworkPeeringPoliciesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.managednetwork.v2019_06_01_pre.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ManagedNetworkManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ManagedNetworkManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-06-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.managed_networks = ManagedNetworksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scope_assignments = ScopeAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.managed_network_groups = ManagedNetworkGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.managed_network_peering_policies = ManagedNetworkPeeringPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
