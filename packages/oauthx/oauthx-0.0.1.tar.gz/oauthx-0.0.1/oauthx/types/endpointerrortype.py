# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import enum


class EndpointErrorType(str, enum.Enum):
    invalid_request         = 'invalid_request'
    invalid_client          = 'invalid_client'
    invalid_grant           = 'invalid_grant'
    unauthorized_client     = 'unauthorized_client'
    unsupported_grant_type  = 'unsupported_grant_type'
    invalid_scope           = 'invalid_scope'