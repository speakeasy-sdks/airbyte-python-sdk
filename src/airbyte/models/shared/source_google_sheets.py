from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceGoogleSheetsGoogleSheetsEnum(str, Enum):
    GOOGLE_SHEETS = "google-sheets"

class SourceGoogleSheetsCredentialsServiceAccountKeyAuthenticationAuthTypeEnum(str, Enum):
    SERVICE = "Service"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSheetsCredentialsServiceAccountKeyAuthentication:
    r"""SourceGoogleSheetsCredentialsServiceAccountKeyAuthentication
    Credentials for connecting to the Google Sheets API
    """
    
    auth_type: SourceGoogleSheetsCredentialsServiceAccountKeyAuthenticationAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    service_account_info: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_info') }})
    
class SourceGoogleSheetsCredentialsAuthenticateViaGoogleOAuthAuthTypeEnum(str, Enum):
    CLIENT = "Client"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSheetsCredentialsAuthenticateViaGoogleOAuth:
    r"""SourceGoogleSheetsCredentialsAuthenticateViaGoogleOAuth
    Credentials for connecting to the Google Sheets API
    """
    
    auth_type: SourceGoogleSheetsCredentialsAuthenticateViaGoogleOAuthAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSheets:
    r"""SourceGoogleSheets
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGoogleSheetsGoogleSheetsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    spreadsheet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spreadsheet_id') }})
    row_batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('row_batch_size'), 'exclude': lambda f: f is None }})
    