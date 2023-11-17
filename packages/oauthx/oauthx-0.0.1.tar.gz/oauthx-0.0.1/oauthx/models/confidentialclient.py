# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic
from aiopki.ext.jose import JWKS
from canonical import ResourceName

from .baseclient import BaseClient


class ConfidentialClient(BaseClient):
    credential: JWKS | ResourceName | str = pydantic.Field(
        default=...,
        alias='client_secret'
    )

    model_config = {
        'populate_by_name': True
    }