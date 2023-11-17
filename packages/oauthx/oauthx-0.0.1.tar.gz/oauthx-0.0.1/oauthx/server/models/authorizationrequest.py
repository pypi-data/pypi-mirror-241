# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import secrets

import oauthx.types
from oauthx.models import Client
from ..types import IServerStorage
from .authorizationstate import AuthorizationState


class AuthorizationRequest(oauthx.types.AuthorizationRequest):

    @property
    def client_id(self) -> Client.KeyType:
        return Client.key(self.root.client_id)

    async def resolve(
        self,
        storage: IServerStorage
    ) -> AuthorizationState:
        """Ensure that the authorization request is decrypted, decoded and
        locally persisted.
        """
        state: AuthorizationState | None
        client = await storage.get(self.client_id)
        if client is None:
            raise oauthx.types.UnknownClient("The specified client is does not exist.")
        if isinstance(self.root, oauthx.types.AuthorizationRequestReference)\
        and self.root.request_uri.is_external():
            raise NotImplementedError
        elif isinstance(self.root, oauthx.types.AuthorizationRequestReference):
            assert self.root.request_uri.id is not None
            state = await storage.get(AuthorizationState.KeyType(self.root.request_uri.id))
        else:
            if isinstance(self.root, oauthx.types.AuthorizationRequestObject):
                raise NotImplementedError
            state = AuthorizationState.model_validate({
                'id': secrets.token_urlsafe(32),
                'source': 'ENDPOINT',
                'params': self.root
            })

        assert state is not None
        return state