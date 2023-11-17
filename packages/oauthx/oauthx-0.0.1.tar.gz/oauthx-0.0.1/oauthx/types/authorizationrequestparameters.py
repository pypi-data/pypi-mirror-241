# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import re

import pydantic

from .baseauthorizationrequest import BaseAuthorizationRequest
from .pckechallengemethod import PKCEChallengeMethod
from .redirecturi import RedirectURI
from .responsetype import ResponseType


class AuthorizationRequestParameters(BaseAuthorizationRequest):
    redirect_uri: RedirectURI | None
    response_type: ResponseType
    scope: set[str]
    state: str | None = None

    # RFC 7635 Proof Key for Code Exchange by OAuth Public Clients
    code_challenge: str | None = None
    code_challenge_method: PKCEChallengeMethod | None = None

    @pydantic.field_validator('scope', mode='before')
    def validate_scope(cls, scope: str | set[str] | None) -> set[str]:
        if isinstance(scope, str):
            scope = {str.strip(x) for x in re.split(r'\s+', scope)}
        scope = scope or set()
        return set(filter(bool, scope))