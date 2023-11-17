# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio

from typing import Any

from .models import Provider


class ProviderCache:
    __module__: str = 'oauthx'
    _providers: dict[str, Provider]

    def __init__(self):
        self._providers = {}

    def add(self, issuer: str, **kwargs: Any) -> Provider:
        """Adds a compliant OAuth 2.x/OpenID Connect server to
        the registry.
        """
        self._providers[issuer] = Provider.model_validate({
            **kwargs,
            'iss': issuer
        })
        return self._providers[issuer]

    def get(self, issuer: str) -> Provider:
        return self._providers[issuer]

    async def discover(self):
        """Invoke the metadata endpoints to discover the providers."""
        await asyncio.gather(*map(Provider.discover, self._providers.values()))

    def __await__(self):
        return self.discover().__await__()


providers: ProviderCache = ProviderCache()
del ProviderCache