# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Callable

import fastapi
import fastapi.params
import yaml
from aiopki.ext.jose import JWKS
from canonical.protocols import ITemplateService

from oauthx.types import AuthorizedGrant
from oauthx.types import EndpointError
from oauthx.types import Grant
from oauthx.models import ServerMetadata
from oauthx.utils import set_signature_defaults
from .config import Config
from .models import AuthorizationRequest
from .oidcroutehandler import OIDCRouteHandler
from .params import CurrentAuthorizationRequest
from .types import IRequestSubject
from .types import IServerStorage
from .types import Request


class OIDCRouter(fastapi.APIRouter):
    __module__: str = 'oauthx.server'
    config: Config

    @classmethod
    def from_config(cls, app: fastapi.FastAPI, config: str | Config):
        if not isinstance(config, Config):
            config = Config.model_validate(
                yaml.safe_load(open(config).read())
            )
        return cls(
            app=app,
            config=config,
            storage_class=config.storage_class,
            subject_class=config.subject_class,
            template_service=config.template_service_class
        )

    def __init__(
        self,
        *,
        app: fastapi.FastAPI,
        config: Config,
        storage_class: type[IServerStorage],
        subject_class: type[IRequestSubject],
        template_service: type[ITemplateService],
    ):
        super().__init__(
            dependencies=[
                self.wrap_global_dependency('templates', template_service)
            ],
            route_class=type('OIDCRouteHandler', (OIDCRouteHandler,), {
                'config': config
            })
        )
        self.app = app
        self.config = config

        # RFC 8414 OAuth 2.0 Authorization Server Metadata
        app.add_api_route(
            methods=['GET'],
            path=f'/.well-known/oauth-authorization-server',
            endpoint=self.metadata,
            name='oauth2.metadata',
            summary='Metadata Endpoint',
            response_model=ServerMetadata,
            tags=['OAuth 2.x/OpenID Connect']
        )

        app.add_api_route(
            methods=['GET'],
            path='/.well-known/jwks.json',
            endpoint=self.jwks,
            name='oauth2.jwks',
            summary='JSON Web Key Set (JWKS)',
            response_model=JWKS,
            tags=['OAuth 2.x/OpenID Connect']
        )

        self.add_api_route(
            methods=['POST'],
            path='/token',
            endpoint=self.token,
            name='oauth2.token',
            summary="Token Endpoint",
            response_model=AuthorizedGrant,
            responses={
                400: {'model': EndpointError},
                401: {'model': EndpointError},
                422: {
                    'model': EndpointError,
                    'description': "Malformed request",
                    'summary': (
                        "The request is missing a required parameter, includes "
                        "an unsupported parameter value (other than grant type), "
                        "repeats a parameter, includes multiple credentials, "
                        "utilizes more than one mechanism for authenticating "
                        "the client, or is otherwise malformed"
                    )
                },
            },
            tags=['OAuth 2.x/OpenID Connect']
        )

        if config.has_authorize_endpoint():
            self.add_api_route(
                path='/authorize',
                endpoint=set_signature_defaults(self.authorize, {
                    'state': CurrentAuthorizationRequest(storage_class),
                    'subject': fastapi.Depends(subject_class.resolve)
                }),
                name='oauth2.authorize',
                summary="Authorization Endpoint",
                status_code=302,
                response_class=fastapi.responses.RedirectResponse,
                response_description="Redirect to the client redirection endpoint.",
                response_model=None,
                responses={
                    400: {
                        'description': (
                            "Unrecoverable error that is not allowed to redirect"
                        )
                    }
                },
                tags=['OAuth 2.x/OpenID Connect']
            )

    async def authorize(
        self,
        request: fastapi.Request,
        state: AuthorizationRequest,
        subject: IRequestSubject = NotImplemented,
    ) -> str | fastapi.responses.HTMLResponse:
        """The **Authorization Endpoint** provides an interface for Resource Owners
        to interact with the Authorization Server in order to authenticate and
        authorize client requests.
        """
        raise NotImplementedError(state)

    async def jwks(self) -> fastapi.responses.PlainTextResponse:
        raise NotImplementedError

    async def metadata(
        self,
        request: fastapi.Request
    ) -> fastapi.responses.PlainTextResponse:
        obj = ServerMetadata.model_validate({
            'issuer': self.config.issuer.id,
            'authorization_response_iss_parameter_supported': True,
            'jwks_uri': str(request.url_for('oauth2.jwks')),
            'subject_types_supported': ['public', 'pairwise'],
            'token_endpoint': str(request.url_for('oauth2.token')),
        })
        if self.config.has_authorize_endpoint():
            obj.authorization_endpoint = str(request.url_for('oauth2.authorize'))
        return fastapi.responses.PlainTextResponse(
            media_type='application/json',
            content=obj.model_dump_json(
                exclude_defaults=True,
                exclude_none=True
            )
        )
    
    async def token(self, grant: Grant) -> fastapi.responses.JSONResponse:
        raise NotImplementedError
    
    def wrap_global_dependency(
        self,
        name: str,
        dependency: Callable[..., Any]
    ) -> fastapi.params.Depends:
        """Set an attribute on the request object that has an instance of the
        given callable.
        """
        async def f(request: Request, dep: Any = fastapi.Depends(dependency)) -> None:
            setattr(request, name, dep)

        return fastapi.Depends(f)