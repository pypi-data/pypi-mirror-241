# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Awaitable
from typing import Callable

import fastapi

from oauthx.types import PKCEChallengeMethod
from oauthx.types import ResponseType
from ..models import AuthorizationRequest
from ..models import AuthorizationState
from ..types import IServerStorage


__all__: list[str] = ['CurrentAuthorizationRequest']


def CurrentAuthorizationRequest(
    storage_class: type[IServerStorage]
) -> Callable[..., Awaitable[AuthorizationRequest]]:
    async def get(
        storage: IServerStorage = fastapi.Depends(storage_class),

        # RFC 6749
        client_id: str | None = fastapi.Query(
            default=None,
            title="Client ID",
            description="Identifies the client that is requesting an access token."
        ),
        redirect_uri: str | None = fastapi.Query(
            default=None,
            title="Redirect URI",
            description=(
                "The client redirection endpoint. This URI **must** be priorly "
                "whitelisted for the client specified by `client_id`. If the "
                "client has multiple allowed redirect URIs and did not "
                "configure a default, then this parameter is **required**."
            )
        ),
        response_type: ResponseType | None = fastapi.Query(
            default=None,
            title="Response type",
            description="Specifies the response type.",
            enum=[e.value for e in ResponseType]
        ),
        scope: str | None = fastapi.Query(
            default=None,
            title="Scope",
            description=(
                "The space-delimited scope that is requested by the client."
            )
        ),
        state: str | None = fastapi.Query(
            default=None,
            alias='state',
            title="State",
            description=(
                "An opaque value used by the client to maintain state between the "
                "request and callback.  The authorization server includes this "
                "value when redirecting the user-agent back to the client."
            )
        ),

        # RFC 7635 Proof Key for Code Exchange by OAuth Public Clients
        code_challenge: str | None = fastapi.Query(
            default=None,
            title="PKCE Challenge",
            description=(
                "Challenge code to use with Proof Key for Code Exchange."
            )
        ),

        code_challenge_method: PKCEChallengeMethod | None = fastapi.Query(
            default=None,
            title="PKCE Challenge Transformation",
            description=(
                "Defaults to `plain` if not present in the request. Code"
                "verifier transformation method is `S256` or `plain`."
            ),
            enum=[e.value for e in PKCEChallengeMethod]
        ),

        # Pushed Authorization Request (PAR).
        request: str | None = fastapi.Query(
            default=None,
            alias='request',
            title="Request",
            description=(
                "A JSON Web Token (JWT) whose JWT Claims Set holds the "
                "JSON-encoded OAuth 2.0 authorization request parameters. "
                "Must not be used in combination with the `request_uri` "
                "parameter, and all other parameters except `client_id` "
                "must be absent.\n\n"
                "Confidential and credentialed clients must first sign "
                "the claims using their private key, and then encrypt the "
                "result with the public keys that are provided by the "
                "authorization server through the `jwks_uri` specified "
                "in its metadata."
            )
        ),
        request_uri: str | None = fastapi.Query(
            default=None,
            title="Request URI",
            description=(
                "References a Pushed Authorization Request (PAR) or a remote "
                "object containing the authorization request.\n\n"
                "If the authorization request was pushed to this authorization "
                "server, then the format of the `request_uri` parameter is "
                "`urn:ietf:params:oauth:request_uri:<reference-value>`. "
                "Otherwise, it is an URI using the `https` scheme. If the "
                "`request_uri` parameter is a remote object, then the external "
                "domain must have been priorly whitelisted by the client."
            )
        ),
    ) -> AuthorizationState:
        assert storage != NotImplemented
        params = AuthorizationRequest.model_validate({
            'client_id': client_id,
            'code_challenge': code_challenge,
            'code_challenge_method': code_challenge_method,
            'redirect_uri': redirect_uri,
            'request': request,
            'request_uri': request_uri,
            'response_type': response_type,
            'scope': scope,
            'state': state
        })
        return await params.resolve(storage)

    return fastapi.Depends(get)