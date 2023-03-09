from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceZenloopZenloopEnum(str, Enum):
    ZENLOOP = "zenloop"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZenloop:
    r"""SourceZenloop
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceZenloopZenloopEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    date_from: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_from'), 'exclude': lambda f: f is None }})
    survey_group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_group_id'), 'exclude': lambda f: f is None }})
    survey_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_id'), 'exclude': lambda f: f is None }})
    