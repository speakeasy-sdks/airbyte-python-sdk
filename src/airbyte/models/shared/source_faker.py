from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceFakerFakerEnum(str, Enum):
    FAKER = "faker"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaker:
    r"""SourceFaker
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceFakerFakerEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    parallelism: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parallelism'), 'exclude': lambda f: f is None }})
    records_per_slice: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('records_per_slice'), 'exclude': lambda f: f is None }})
    records_per_sync: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('records_per_sync'), 'exclude': lambda f: f is None }})
    seed: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    