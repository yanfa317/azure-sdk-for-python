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

from ._configuration import WebSiteManagementClientConfiguration
from .operations import WebSiteManagementClientOperationsMixin
from .operations import AppServiceCertificateOrdersOperations
from .operations import CertificateRegistrationProviderOperations
from .operations import DomainsOperations
from .operations import TopLevelDomainsOperations
from .operations import DomainRegistrationProviderOperations
from .operations import CertificatesOperations
from .operations import DeletedWebAppsOperations
from .operations import DiagnosticsOperations
from .operations import ProviderOperations
from .operations import RecommendationsOperations
from .operations import WebAppsOperations
from .operations import AppServiceEnvironmentsOperations
from .operations import AppServicePlansOperations
from .operations import ResourceHealthMetadataOperations
from . import models


class WebSiteManagementClient(WebSiteManagementClientOperationsMixin, SDKClient):
    """WebSite Management Client

    :ivar config: Configuration for client.
    :vartype config: WebSiteManagementClientConfiguration

    :ivar app_service_certificate_orders: AppServiceCertificateOrders operations
    :vartype app_service_certificate_orders: azure.mgmt.web.operations.AppServiceCertificateOrdersOperations
    :ivar certificate_registration_provider: CertificateRegistrationProvider operations
    :vartype certificate_registration_provider: azure.mgmt.web.operations.CertificateRegistrationProviderOperations
    :ivar domains: Domains operations
    :vartype domains: azure.mgmt.web.operations.DomainsOperations
    :ivar top_level_domains: TopLevelDomains operations
    :vartype top_level_domains: azure.mgmt.web.operations.TopLevelDomainsOperations
    :ivar domain_registration_provider: DomainRegistrationProvider operations
    :vartype domain_registration_provider: azure.mgmt.web.operations.DomainRegistrationProviderOperations
    :ivar certificates: Certificates operations
    :vartype certificates: azure.mgmt.web.operations.CertificatesOperations
    :ivar deleted_web_apps: DeletedWebApps operations
    :vartype deleted_web_apps: azure.mgmt.web.operations.DeletedWebAppsOperations
    :ivar diagnostics: Diagnostics operations
    :vartype diagnostics: azure.mgmt.web.operations.DiagnosticsOperations
    :ivar provider: Provider operations
    :vartype provider: azure.mgmt.web.operations.ProviderOperations
    :ivar recommendations: Recommendations operations
    :vartype recommendations: azure.mgmt.web.operations.RecommendationsOperations
    :ivar web_apps: WebApps operations
    :vartype web_apps: azure.mgmt.web.operations.WebAppsOperations
    :ivar app_service_environments: AppServiceEnvironments operations
    :vartype app_service_environments: azure.mgmt.web.operations.AppServiceEnvironmentsOperations
    :ivar app_service_plans: AppServicePlans operations
    :vartype app_service_plans: azure.mgmt.web.operations.AppServicePlansOperations
    :ivar resource_health_metadata: ResourceHealthMetadata operations
    :vartype resource_health_metadata: azure.mgmt.web.operations.ResourceHealthMetadataOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Your Azure subscription ID. This is a
     GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = WebSiteManagementClientConfiguration(credentials, subscription_id, base_url)
        super(WebSiteManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.app_service_certificate_orders = AppServiceCertificateOrdersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.certificate_registration_provider = CertificateRegistrationProviderOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.domains = DomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.top_level_domains = TopLevelDomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.domain_registration_provider = DomainRegistrationProviderOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deleted_web_apps = DeletedWebAppsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.diagnostics = DiagnosticsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.provider = ProviderOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recommendations = RecommendationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.web_apps = WebAppsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.app_service_environments = AppServiceEnvironmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.app_service_plans = AppServicePlansOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resource_health_metadata = ResourceHealthMetadataOperations(
            self._client, self.config, self._serialize, self._deserialize)
