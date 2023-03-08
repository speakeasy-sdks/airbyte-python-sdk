from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceGoogleAnalyticsDataAPIGoogleAnalyticsDataAPIEnum(str, Enum):
    GOOGLE_ANALYTICS_DATA_API = "google-analytics-data-api"

class SourceGoogleAnalyticsDataAPICredentialsServiceAccountKeyAuthenticationAuthTypeEnum(str, Enum):
    SERVICE = "Service"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAnalyticsDataAPICredentialsServiceAccountKeyAuthentication:
    r"""SourceGoogleAnalyticsDataAPICredentialsServiceAccountKeyAuthentication
    Credentials for the service
    """
    
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    auth_type: Optional[SourceGoogleAnalyticsDataAPICredentialsServiceAccountKeyAuthenticationAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    
class SourceGoogleAnalyticsDataAPICredentialsAuthenticateViaGoogleOauthAuthTypeEnum(str, Enum):
    CLIENT = "Client"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAnalyticsDataAPICredentialsAuthenticateViaGoogleOauth:
    r"""SourceGoogleAnalyticsDataAPICredentialsAuthenticateViaGoogleOauth
    Credentials for the service
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    auth_type: Optional[SourceGoogleAnalyticsDataAPICredentialsAuthenticateViaGoogleOauthAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAnalyticsDataAPI:
    r"""SourceGoogleAnalyticsDataAPI
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGoogleAnalyticsDataAPIGoogleAnalyticsDataAPIEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    date_ranges_start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_ranges_start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    property_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('property_id') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    custom_reports: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports'), 'exclude': lambda f: f is None }})
    window_in_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_in_days'), 'exclude': lambda f: f is None }})
    