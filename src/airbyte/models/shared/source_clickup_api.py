from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceClickupAPIClickupAPIEnum(str, Enum):
    CLICKUP_API = "clickup-api"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceClickupAPI:
    r"""SourceClickupAPI
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceClickupAPIClickupAPIEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    folder_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_id'), 'exclude': lambda f: f is None }})
    list_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_id'), 'exclude': lambda f: f is None }})
    space_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('space_id'), 'exclude': lambda f: f is None }})
    team_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team_id'), 'exclude': lambda f: f is None }})
    