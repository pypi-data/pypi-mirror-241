# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic
from canonical import ResourceIdentifier

from .confidentialclient import ConfidentialClient
from .publicclient import PublicClient


class Client(pydantic.RootModel[ConfidentialClient | PublicClient]):

    class KeyType(ResourceIdentifier[str, 'Client']):
        client_id: str
        openapi_example: str = 'client-123'
        openapi_title: str = 'Client ID'

        def __init__(self, client_id: str):
            self.client_id = client_id

        def __str__(self) -> str:
            return self.client_id
        
        def __eq__(self, key: object) -> bool:
            return isinstance(key, type(self)) and key.client_id == self.client_id

    @property
    def id(self) -> KeyType:
        return self.key(self.root.client_id)

    @classmethod
    def key(cls, client_id: str) -> KeyType:
        return cls.KeyType(client_id)

    def is_confidential(self) -> bool:
        return isinstance(self.root, ConfidentialClient)

    def is_public(self) -> bool:
        return isinstance(self.root, PublicClient)