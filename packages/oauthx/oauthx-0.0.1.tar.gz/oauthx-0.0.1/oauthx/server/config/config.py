# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic
from canonical.protocols import ITemplateService

from oauthx.models import Client
from oauthx.types import GrantType
from oauthx.utils.loader import import_symbol
from ..types import IRequestSubject
from ..types import IServerStorage
from .implementationconfig import ImplementationConfig
from .issuerconfig import IssuerConfig


class Config(pydantic.BaseModel):
    client: Client | None
    grant_types_supported: set[GrantType] = set()
    impl: ImplementationConfig
    issuer: IssuerConfig

    @property
    def storage_class(self) -> type[IServerStorage]:
        return import_symbol(self.impl.storage)

    @property
    def subject_class(self) -> type[IRequestSubject]:
        return import_symbol(self.impl.subject)

    @property
    def template_service_class(self) -> type[ITemplateService]:
        return import_symbol(self.impl.template)

    def has_authorize_endpoint(self) -> bool:
        """Return a boolean indicating if the authorization server should
        expose the Authorization Endpoint.
        """
        return 'authorization_code' in self.grant_types_supported