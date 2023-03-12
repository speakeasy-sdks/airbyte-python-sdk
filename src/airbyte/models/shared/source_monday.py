from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceMondayMondayEnum(str, Enum):
    MONDAY = "monday"

class SourceMondayCredentialsAPITokenAuthTypeEnum(str, Enum):
    API_TOKEN = "api_token"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMondayCredentialsAPIToken:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    auth_type: SourceMondayCredentialsAPITokenAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    
class SourceMondayCredentialsOAuth20AuthTypeEnum(str, Enum):
    OAUTH2_0 = "oauth2.0"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMondayCredentialsOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    auth_type: SourceMondayCredentialsOAuth20AuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    subdomain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMonday:
    r"""SourceMonday
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceMondayMondayEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    