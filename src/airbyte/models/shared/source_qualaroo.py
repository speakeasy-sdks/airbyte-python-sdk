from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceQualarooQualarooEnum(str, Enum):
    QUALAROO = "qualaroo"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceQualaroo:
    r"""SourceQualaroo
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceQualarooQualarooEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    survey_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_ids'), 'exclude': lambda f: f is None }})
    