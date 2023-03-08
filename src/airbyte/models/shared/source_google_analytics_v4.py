from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceGoogleAnalyticsV4GoogleAnalyticsV4Enum(str, Enum):
    GOOGLE_ANALYTICS_V4 = "google-analytics-v4"

class SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthenticationAuthTypeEnum(str, Enum):
    SERVICE = "Service"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthentication:
    r"""SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthentication
    Credentials for the service
    """
    
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    auth_type: Optional[SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthenticationAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    
class SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauthAuthTypeEnum(str, Enum):
    CLIENT = "Client"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauth:
    r"""SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauth
    Credentials for the service
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    auth_type: Optional[SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauthAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAnalyticsV4:
    r"""SourceGoogleAnalyticsV4
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGoogleAnalyticsV4GoogleAnalyticsV4Enum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    view_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_id') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    custom_reports: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports'), 'exclude': lambda f: f is None }})
    window_in_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_in_days'), 'exclude': lambda f: f is None }})
    