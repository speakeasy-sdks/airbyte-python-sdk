from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceSquareSquareEnum(str, Enum):
    SQUARE = "square"

class SourceSquareCredentialsAPIKeyCredentialsTitleEnum(str, Enum):
    API_KEY = "API Key"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquareCredentialsAPIKey:
    r"""SourceSquareCredentialsAPIKey
    Choose how to authenticate to Square.
    """
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    credentials_title: Optional[SourceSquareCredentialsAPIKeyCredentialsTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title'), 'exclude': lambda f: f is None }})
    
class SourceSquareCredentialsOauthAuthenticationCredentialsTitleEnum(str, Enum):
    O_AUTH_CREDENTIALS = "OAuth Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquareCredentialsOauthAuthentication:
    r"""SourceSquareCredentialsOauthAuthentication
    Choose how to authenticate to Square.
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    credentials_title: Optional[SourceSquareCredentialsOauthAuthenticationCredentialsTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquare:
    r"""SourceSquare
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSquareSquareEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    is_sandbox: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    include_deleted_objects: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_deleted_objects'), 'exclude': lambda f: f is None }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    