from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceMicrosoftTeamsMicrosoftTeamsEnum(str, Enum):
    MICROSOFT_TEAMS = "microsoft-teams"

class SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoftAuthTypeEnum(str, Enum):
    TOKEN = "Token"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoft:
    r"""SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoft
    Choose how to authenticate to Microsoft
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    tenant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tenant_id') }})
    auth_type: Optional[SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoftAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    
class SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoftOAuth20AuthTypeEnum(str, Enum):
    CLIENT = "Client"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoftOAuth20:
    r"""SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoftOAuth20
    Choose how to authenticate to Microsoft
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    tenant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tenant_id') }})
    auth_type: Optional[SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoftOAuth20AuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMicrosoftTeams:
    r"""SourceMicrosoftTeams
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceMicrosoftTeamsMicrosoftTeamsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    period: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    