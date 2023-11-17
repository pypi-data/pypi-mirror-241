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
from typing import Coroutine

import fastapi
import fastapi.routing
import starlette.responses

from oauthx.types import Error
from oauthx.types import EndpointError
from .config import Config
from .types import Request


class OIDCRouteHandler(fastapi.routing.APIRoute):
    config: Config

    def get_route_handler(self) -> Callable[[fastapi.Request], Coroutine[Any, Any, starlette.responses.Response]]:
        handler = super().get_route_handler()

        async def f(request: fastapi.Request) -> starlette.responses.Response:
            request = Request(request.scope, request.receive)
            request.config = self.config # type: ignore
            try:
                response = await handler(request)
            except Error as exception:
                response = EndpointError.model_validate({
                    'error': exception.error,
                    'error_description': exception.error_description,
                    'error_url': exception.error_url
                })
                is_authorization = request.url.path == request.url_for('oauth2.authorize').path
                if is_authorization:
                    response = await request.render_to_response('oauth/error.html.j2', {
                        'page_title': 'Access denied: authorization error',
                        'error': exception
                    })
                else:
                    raise NotImplementedError
            return response
        
        return f