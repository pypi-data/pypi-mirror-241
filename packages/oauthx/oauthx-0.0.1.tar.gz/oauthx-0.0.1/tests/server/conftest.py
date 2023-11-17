# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import fastapi
import httpx
import pytest
import yaml

from oauthx.server import OIDCRouter
from oauthx.server.config import Config


@pytest.fixture(scope='session')
def config_data() -> dict[str, Any]:
    return yaml.safe_load(open('etc/oidc.conf', 'r').read())


@pytest.fixture(scope='function')
def config(config_data: dict[str, Any]) -> Config:
    return Config.model_validate(config_data)


@pytest.fixture
def app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    app.include_router(
        prefix='/oauth/v2',
        router=OIDCRouter.from_config('etc/oidc.conf')
    )
    return app


@pytest.fixture(scope='function')
async def agent(app: fastapi.FastAPI):
    async with httpx.AsyncClient(app=app) as client:
        yield client