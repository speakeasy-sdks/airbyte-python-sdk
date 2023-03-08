from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceGithubGithubEnum(str, Enum):
    GITHUB = "github"

class SourceGithubCredentialsPersonalAccessTokenOptionTitleEnum(str, Enum):
    PAT_CREDENTIALS = "PAT Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGithubCredentialsPersonalAccessToken:
    r"""SourceGithubCredentialsPersonalAccessToken
    Choose how to authenticate to GitHub
    """
    
    personal_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_access_token') }})
    option_title: Optional[SourceGithubCredentialsPersonalAccessTokenOptionTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    
class SourceGithubCredentialsOAuthOptionTitleEnum(str, Enum):
    O_AUTH_CREDENTIALS = "OAuth Credentials"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGithubCredentialsOAuth:
    r"""SourceGithubCredentialsOAuth
    Choose how to authenticate to GitHub
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    option_title: Optional[SourceGithubCredentialsOAuthOptionTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGithub:
    r"""SourceGithub
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGithubGithubEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    repository: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('repository') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    page_size_for_large_streams: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size_for_large_streams'), 'exclude': lambda f: f is None }})
    