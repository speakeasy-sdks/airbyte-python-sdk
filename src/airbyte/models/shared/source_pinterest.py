from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourcePinterestPinterestEnum(str, Enum):
    PINTEREST = "pinterest"

class SourcePinterestCredentialsAccessTokenAuthMethodEnum(str, Enum):
    ACCESS_TOKEN = "access_token"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePinterestCredentialsAccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    auth_method: SourcePinterestCredentialsAccessTokenAuthMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    
class SourcePinterestCredentialsOAuth20AuthMethodEnum(str, Enum):
    OAUTH2_0 = "oauth2.0"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePinterestCredentialsOAuth20:
    auth_method: SourcePinterestCredentialsOAuth20AuthMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    
class SourcePinterestStatusEnum(str, Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    ARCHIVED = "ARCHIVED"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePinterest:
    r"""SourcePinterest
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePinterestPinterestEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    status: Optional[list[SourcePinterestStatusEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    