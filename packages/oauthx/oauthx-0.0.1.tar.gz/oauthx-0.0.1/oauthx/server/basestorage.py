# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
from typing import Any
from typing import TypeVar

from canonical import ResourceIdentifier

from oauthx.models import Client
from .config import Config
from .params import CurrentConfig
from .types import IServerStorage


T = TypeVar('T')


class BaseStorage(IServerStorage):
    __module__: str = 'oauthx.server.ref'
    client: Client | None
    config: Config

    def __init__(self, config: Config = CurrentConfig) -> None:
        self.client = config.client
        self.config = config

    @functools.singledispatchmethod
    async def _get(self, key: Any) -> Any:
        raise NotImplementedError

    @_get.register
    async def _get_client(self, key: Client.KeyType) -> Client | None:
        if self.client and self.client.id == key:
            return self.client
        return await self.get_client(key)

    async def get(self, key: ResourceIdentifier[Any, T]) -> T | None:
        return await self._get(key)

    async def get_client(self, key: Client.KeyType) -> Client | None:
        raise NotImplementedError

    async def persist(self, object: Any) -> None:
        return await super().persist(object)