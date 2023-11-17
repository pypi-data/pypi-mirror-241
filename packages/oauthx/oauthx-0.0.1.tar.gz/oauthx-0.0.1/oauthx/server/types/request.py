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
from canonical.protocols import ITemplateService


class Request(fastapi.Request):
    templates: ITemplateService

    async def render_to_response(
        self,
        template_names: list[str] | str,
        context: dict[str, Any] | None = None,
        status_code: int = 200,
        headers: dict[str, Any] | None = None
    ) -> fastapi.Response:
        return fastapi.responses.HTMLResponse(
            status_code=status_code,
            headers=headers,
            content=await self.templates.render_template(
                template_names,
                context=context or {}
            )
        )