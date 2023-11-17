# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from .clientassertiontype import ClientAssertionType


class BaseGrant(pydantic.BaseModel):
    client_id: str | None = pydantic.Field(
        default=None,
        title="Client ID",
        description=(
            "This parameter is **required** if the client is not authenticating with "
            "the authorization server and the grant requires client identifiation, "
            "otherwise it **must** be omitted.\n\n"
            "If the client authenticates using an implementation of the RFC 7521 "
            "assertion framework, then the `client_id` parameter is unnecessary "
            "for client assertion authentication because the client is identified "
            "by the subject of the assertion.  If present, the value of the "
            "`client_id` parameter **must** identify the same client as is "
            "identified by the client assertion."
        )
    )

    client_secret: str | None = pydantic.Field(
        default=None,
        title="Client secret",
        description=(
            "This parameter is **required** if the client is authenticating using "
            "the `client_secret_post` method, otherwise is **must** be "
            "omitted."
        )
    )

    # RFC 7521 Assertion Framework for OAuth 2.0 Client
    # Authentication and Authorization Grants
    client_assertion_type: ClientAssertionType | None = pydantic.Field(
        default=None,
        title="Client assertion type",
        description=(
            "The format of the assertion as defined by the authorization server. "
            "The value is an absolute URI."
        )
    )

    client_assertion: str | None = pydantic.Field(
        default=None,
        title='Client assertion',
        description=(
            "The assertion being used to authenticate the client. "
            "Specific serialization of the assertion is defined by "
            "profile documents for `client_assertion_type`."
        )
    )

    # RFC 8707 Resource Indicators for OAuth 2.0
    resource: str | None = pydantic.Field(
        default=None,
        description=(
            "Specifies the intended resource to use the issued access token and "
            "(optionally) ID token with."
        )
    )