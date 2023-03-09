from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceGoogleSearchConsoleGoogleSearchConsoleEnum(str, Enum):
    GOOGLE_SEARCH_CONSOLE = "google-search-console"

class SourceGoogleSearchConsoleAuthorizationServiceAccountKeyAuthenticationAuthTypeEnum(str, Enum):
    SERVICE = "Service"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSearchConsoleAuthorizationServiceAccountKeyAuthentication:
    auth_type: SourceGoogleSearchConsoleAuthorizationServiceAccountKeyAuthenticationAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    service_account_info: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_info') }})
    
class SourceGoogleSearchConsoleAuthorizationOAuthAuthTypeEnum(str, Enum):
    CLIENT = "Client"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSearchConsoleAuthorizationOAuth:
    auth_type: SourceGoogleSearchConsoleAuthorizationOAuthAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSearchConsole:
    r"""SourceGoogleSearchConsole
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGoogleSearchConsoleGoogleSearchConsoleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    authorization: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    site_urls: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_urls') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    custom_reports: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports'), 'exclude': lambda f: f is None }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    