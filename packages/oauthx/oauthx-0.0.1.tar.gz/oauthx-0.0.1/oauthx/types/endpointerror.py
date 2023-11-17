# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from .endpointerrortype import EndpointErrorType


class EndpointError(pydantic.BaseModel):
    error: EndpointErrorType = pydantic.Field(
        default=...,
    )

    error_description: str | None = pydantic.Field(
        default=None,
        title="Error description"
    )

    error_uri: str | None = pydantic.Field(
        default=None,
        title='Error URI'
    )

    model_config = {
        'title': 'Error',
        'json_schema_extra': {
            'examples': [
                {
                    'error': 'invalid_request',
                    'error_description': (
                        "The request is missing a required parameter, includes "
                        "an unsupported parameter value (other than grant type), "
                        "repeats a parameter, includes multiple credentials, "
                        "utilizes more than one mechanism for authenticating "
                        "the client, or is otherwise malformed."
                    )
                },
            ]
        }
    }