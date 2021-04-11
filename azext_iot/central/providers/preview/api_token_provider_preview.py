# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

from azext_iot.constants import CENTRAL_ENDPOINT
from azext_iot.central import services as central_services
from azext_iot.central.models.enum import Role
from azext_iot.central.iot_central_api_preview import IotCentralApiPreview
from azext_iot.central.services import _utility
from azext_iot.central.utils import parse_device_status

logger = get_logger(__name__)


class CentralApiTokenProviderPreview:
    def __init__(self, cmd, app_id: str, token=None):
        """
        Provider for API token APIs

        Args:
            cmd: command passed into az
            app_id: name of app (used for forming request URL)
            token: (OPTIONAL) authorization token to fetch API token details from IoTC.
                MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
                Useful in scenarios where user doesn't own the app
                therefore AAD token won't work, but a SAS token generated by owner will
        """
        self._cmd = cmd
        self._app_id = app_id
        self._token = token

    def add_api_token(
        self, token_id: str, role: Role, central_dns_suffix=CENTRAL_ENDPOINT,
    ):
        token = _utility.get_token_credential(self._cmd)
        apiClient = IotCentralApiPreview(token, self._app_id, central_dns_suffix)
        payload = {
            "roles": [{"role": role.value}],
        }
        return apiClient.api_tokens.set(token_id, payload)

    def get_api_token_list(
        self, central_dns_suffix=CENTRAL_ENDPOINT,
    ):
        token = _utility.get_token_credential(self._cmd)
        apiClient = IotCentralApiPreview(token, self._app_id, central_dns_suffix)
        return apiClient.api_tokens.list()

    def get_api_token(
        self, token_id, central_dns_suffix=CENTRAL_ENDPOINT,
    ):
        token = _utility.get_token_credential(self._cmd)
        apiClient = IotCentralApiPreview(token, self._app_id, central_dns_suffix)
        return apiClient.api_tokens.get(token_id)

    def delete_api_token(
        self, token_id, central_dns_suffix=CENTRAL_ENDPOINT,
    ):
        token = _utility.get_token_credential(self._cmd)
        apiClient = IotCentralApiPreview(token, self._app_id, central_dns_suffix)
        return apiClient.api_tokens.remove(token_id)
