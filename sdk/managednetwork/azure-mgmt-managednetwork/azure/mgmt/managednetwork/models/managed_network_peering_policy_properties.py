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

from .resource_properties import ResourceProperties


class ManagedNetworkPeeringPolicyProperties(ResourceProperties):
    """Properties of a Managed Network Peering Policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
     Possible values include: 'Updating', 'Deleting', 'Failed', 'Succeeded'
    :vartype provisioning_state: str or
     ~azure.mgmt.managednetwork.v2019_06_01_pre.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    :param type: Required. Gets or sets the connectivity type of a network
     structure policy. Possible values include: 'HubAndSpokeTopology',
     'MeshTopology'
    :type type: str or ~azure.mgmt.managednetwork.v2019_06_01_pre.models.Type
    :param hub: Gets or sets the hub virtual network ID
    :type hub: ~azure.mgmt.managednetwork.v2019_06_01_pre.models.ResourceId
    :param spokes: Gets or sets the spokes group IDs
    :type spokes:
     list[~azure.mgmt.managednetwork.v2019_06_01_pre.models.ResourceId]
    :param mesh: Gets or sets the mesh group IDs
    :type mesh:
     list[~azure.mgmt.managednetwork.v2019_06_01_pre.models.ResourceId]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'hub': {'key': 'hub', 'type': 'ResourceId'},
        'spokes': {'key': 'spokes', 'type': '[ResourceId]'},
        'mesh': {'key': 'mesh', 'type': '[ResourceId]'},
    }

    def __init__(self, **kwargs):
        super(ManagedNetworkPeeringPolicyProperties, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.hub = kwargs.get('hub', None)
        self.spokes = kwargs.get('spokes', None)
        self.mesh = kwargs.get('mesh', None)
