from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceAsanaAsanaEnum(str, Enum):
    ASANA = "asana"

class SourceAsanaCredentialsAuthenticateViaAsanaOauthCredentialsTitleEnum(str, Enum):
    O_AUTH_CREDENTIALS = "OAuth Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAsanaCredentialsAuthenticateViaAsanaOauth:
    r"""SourceAsanaCredentialsAuthenticateViaAsanaOauth
    Choose how to authenticate to Github
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    option_title: Optional[SourceAsanaCredentialsAuthenticateViaAsanaOauthCredentialsTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    
class SourceAsanaCredentialsAuthenticateWithPersonalAccessTokenCredentialsTitleEnum(str, Enum):
    PAT_CREDENTIALS = "PAT Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAsanaCredentialsAuthenticateWithPersonalAccessToken:
    r"""SourceAsanaCredentialsAuthenticateWithPersonalAccessToken
    Choose how to authenticate to Github
    """
    
    personal_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_access_token') }})
    option_title: Optional[SourceAsanaCredentialsAuthenticateWithPersonalAccessTokenCredentialsTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAsana:
    r"""SourceAsana
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceAsanaAsanaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    