# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import secrets
from typing import Literal

import pydantic
from canonical import ResourceIdentifier

from oauthx.types import AuthorizationRequestParameters


class AuthorizationState(pydantic.BaseModel):

    class KeyType(ResourceIdentifier[str, 'AuthorizationState']):
        client_id: str
        openapi_example: str = 'FOpou5oouxBHGGXBYI23R7vfEc3HcRjd4-_5EYYzsuQ'
        openapi_title: str = 'Request ID'

        def __init__(self, request_id: str):
            self.request_id = request_id

        def __str__(self) -> str:
            return self.request_id
        
        def __eq__(self, key: object) -> bool:
            return isinstance(key, type(self)) and key.request_id == self.request_id

    code: str = pydantic.Field(
        default=lambda: secrets.token_urlsafe(32)
    )

    created: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    id: str = pydantic.Field(
        default=...
    )

    params: AuthorizationRequestParameters = pydantic.Field(
        default=...
    )

    signed: bool = pydantic.Field(
        default=False
    )

    source: Literal['ENDPOINT', 'REMOTE', 'PUSHED'] = pydantic.Field(
        default=...
    )