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

from msrest.serialization import Model


class ResourceProperties(Model):
    """Base for resource properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
     Possible values include: 'Updating', 'Deleting', 'Failed', 'Succeeded'
    :vartype provisioning_state: str or
     ~azure.mgmt.managednetwork.v2019_06_01_pre.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.etag = None
