from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any

class SourceAuth0Auth0Enum(str, Enum):
    AUTH0 = "auth0"

class SourceAuth0CredentialsOAuth2AccessTokenAuthenticationMethodEnum(str, Enum):
    OAUTH2_ACCESS_TOKEN = "oauth2_access_token"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAuth0CredentialsOAuth2AccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    auth_type: SourceAuth0CredentialsOAuth2AccessTokenAuthenticationMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    
class SourceAuth0CredentialsOAuth2ConfidentialApplicationAuthenticationMethodEnum(str, Enum):
    OAUTH2_CONFIDENTIAL_APPLICATION = "oauth2_confidential_application"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAuth0CredentialsOAuth2ConfidentialApplication:
    audience: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audience') }})
    auth_type: SourceAuth0CredentialsOAuth2ConfidentialApplicationAuthenticationMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAuth0:
    r"""SourceAuth0
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceAuth0Auth0Enum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    base_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url') }})
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    