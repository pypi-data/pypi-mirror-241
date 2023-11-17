# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

from canonical.protocols import ITemplateService
from jinja2 import Environment
from jinja2 import PackageLoader


class TemplateService(ITemplateService):
    env: Environment = Environment(
        loader=PackageLoader('oauthx.server.ref')
    )

    def __init__(self) -> None:
        pass

    async def get_template(self, template_name: str, using: str | None = None):
        return self.env.get_template(template_name)

    async def render_template(
        self,
        templates: list[str] | str,
        context: dict[str, Any]
    ) -> str:
        if isinstance(templates, list):
            raise NotImplementedError
        t = self.env.get_template(templates)
        return t.render(**context)
    
    async def select_template(self, templates: list[str], using: str | None = None):
        return self.env.select_template(templates)