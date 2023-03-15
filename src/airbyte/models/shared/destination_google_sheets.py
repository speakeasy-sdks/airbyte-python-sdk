from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class DestinationGoogleSheetsGoogleSheetsEnum(str, Enum):
    GOOGLE_SHEETS = "google-sheets"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGoogleSheetsAuthenticationViaGoogleOAuth:
    r"""DestinationGoogleSheetsAuthenticationViaGoogleOAuth
    Google API Credentials for connecting to Google Sheets and Google Drive APIs
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGoogleSheets:
    r"""DestinationGoogleSheets
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationGoogleSheetsGoogleSheetsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    credentials: DestinationGoogleSheetsAuthenticationViaGoogleOAuth = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    spreadsheet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spreadsheet_id') }})
    