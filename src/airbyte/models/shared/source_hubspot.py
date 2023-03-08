from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any

class SourceHubspotHubspotEnum(str, Enum):
    HUBSPOT = "hubspot"

class SourceHubspotCredentialsPrivateAppCredentialsEnum(str, Enum):
    PRIVATE_APP_CREDENTIALS = "Private App Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspotCredentialsPrivateApp:
    r"""SourceHubspotCredentialsPrivateApp
    Choose how to authenticate to HubSpot.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    credentials_title: SourceHubspotCredentialsPrivateAppCredentialsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    
class SourceHubspotCredentialsOAuthCredentialsEnum(str, Enum):
    O_AUTH_CREDENTIALS = "OAuth Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspotCredentialsOAuth:
    r"""SourceHubspotCredentialsOAuth
    Choose how to authenticate to HubSpot.
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    credentials_title: SourceHubspotCredentialsOAuthCredentialsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspot:
    r"""SourceHubspot
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceHubspotHubspotEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    