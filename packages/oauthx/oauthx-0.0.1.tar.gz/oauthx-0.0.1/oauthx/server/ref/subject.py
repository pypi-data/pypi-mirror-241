# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import Literal

import fastapi
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials

from oauthx.server.types import IRequestSubject


security = HTTPBasic()


class RequestSubject(IRequestSubject):
    __module__: str = 'oauthx.server.ref'
    id: Literal[123] = 123
    password: Literal['password'] = 'password'
    username: Literal['username'] = 'username'

    @classmethod
    async def resolve(
        cls,
        request: fastapi.Request,
        credentials: Annotated[HTTPBasicCredentials, fastapi.Depends(security)],
    ) -> IRequestSubject:
        self = cls()
        if credentials.username != self.username\
        or credentials.password != self.password:
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Basic"},
            )
        return self