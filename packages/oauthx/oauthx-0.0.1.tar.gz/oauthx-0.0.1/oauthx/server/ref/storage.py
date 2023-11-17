# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.models import Client
from ..basestorage import BaseStorage


class Storage(BaseStorage):
    __module__: str = 'oauthx.server.ref'

    async def get_client(self, key: Client.KeyType) -> Client | None:
        return None