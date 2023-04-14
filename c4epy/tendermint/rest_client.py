# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""Implementation of IBC Applications Transfer  interface using REST."""
from google.protobuf.json_format import Parse

from c4epy.common.rest_client import RestClient
from c4epy.protos.cosmos.base.tendermint.v1beta1 import (
    GetBlockByHeightRequest,
    GetBlockByHeightResponse,
    GetLatestBlockRequest,
    GetLatestBlockResponse,
    GetLatestValidatorSetRequest,
    GetLatestValidatorSetResponse,
    GetNodeInfoRequest,
    GetNodeInfoResponse,
    GetSyncingRequest,
    GetSyncingResponse,
    GetValidatorSetByHeightRequest,
    GetValidatorSetByHeightResponse,
)
from c4epy.tendermint.interface import CosmosBaseTendermint


class CosmosBaseTendermintRestClient(CosmosBaseTendermint):
    """Cosmos Base Tendermint REST client."""

    API_URL = "/cosmos/base/tendermint/v1beta1"

    def __init__(self, rest_api: RestClient) -> None:
        """
        Initialize.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def GetNodeInfo(self, request: GetNodeInfoRequest) -> GetNodeInfoResponse:
        """
        GetNodeInfo queries the current node info.

        :param request: GetNodeInfoRequest
        :return: GetNodeInfoResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/node_info",
        )
        return GetNodeInfoResponse().from_json(json_response)

    def GetSyncing(self, request: GetSyncingRequest) -> GetSyncingResponse:
        """
        GetSyncing queries node syncing.

        :param request: GetSyncingRequest
        :return: GetSyncingResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/syncing",
        )
        return GetSyncingResponse().from_json(json_response)

    def GetLatestBlock(self, request: GetLatestBlockRequest) -> GetLatestBlockResponse:
        """
        GetLatestBlock returns the latest block.

        :param request: GetLatestBlockRequest
        :return: GetLatestBlockResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/blocks/latest",
        )
        return GetLatestBlockResponse().from_json(json_response)

    def GetBlockByHeight(
        self, request: GetBlockByHeightRequest
    ) -> GetBlockByHeightResponse:
        """
        GetBlockByHeight queries block for given height.

        :param request: GetBlockByHeightRequest
        :return: GetBlockByHeightResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/blocks/{request.height}")
        return GetBlockByHeightResponse().from_json(json_response)

    def GetLatestValidatorSet(
        self, request: GetLatestValidatorSetRequest
    ) -> GetLatestValidatorSetResponse:
        """
        GetLatestValidatorSet queries latest validator-set.

        :param request: GetLatestValidatorSetRequest
        :return: GetLatestValidatorSetResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/validatorsets/latest", request
        )
        return GetLatestValidatorSetResponse().from_json(json_response)

    def GetValidatorSetByHeight(
        self, request: GetValidatorSetByHeightRequest
    ) -> GetValidatorSetByHeightResponse:
        """
        GetValidatorSetByHeight queries validator-set at a given height.

        :param request: GetValidatorSetByHeightRequest
        :return: GetValidatorSetByHeightResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/validatorsets/{request.height}", request
        )
        return GetValidatorSetByHeightResponse().from_json(json_response)