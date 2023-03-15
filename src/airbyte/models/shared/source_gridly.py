from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceGridlyGridlyEnum(str, Enum):
    GRIDLY = "gridly"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGridly:
    r"""SourceGridly
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGridlyGridlyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    grid_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grid_id') }})
    