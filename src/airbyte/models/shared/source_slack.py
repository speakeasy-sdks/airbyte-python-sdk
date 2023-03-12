from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceSlackSlackEnum(str, Enum):
    SLACK = "slack"

class SourceSlackCredentialsAPITokenOptionTitleEnum(str, Enum):
    API_TOKEN_CREDENTIALS = "API Token Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSlackCredentialsAPIToken:
    r"""SourceSlackCredentialsAPIToken
    Choose how to authenticate into Slack
    """
    
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    option_title: SourceSlackCredentialsAPITokenOptionTitleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title') }})
    
class SourceSlackCredentialsSignInViaSlackOAuthOptionTitleEnum(str, Enum):
    DEFAULT_O_AUTH2_0_AUTHORIZATION = "Default OAuth2.0 authorization"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSlackCredentialsSignInViaSlackOAuth:
    r"""SourceSlackCredentialsSignInViaSlackOAuth
    Choose how to authenticate into Slack
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    option_title: SourceSlackCredentialsSignInViaSlackOAuthOptionTitleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSlack:
    r"""SourceSlack
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSlackSlackEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    join_channels: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_channels') }})
    lookback_window: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    channel_filter: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel_filter'), 'exclude': lambda f: f is None }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    