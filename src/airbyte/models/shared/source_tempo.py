from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceTempoTempoEnum(str, Enum):
    TEMPO = "tempo"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTempo:
    r"""SourceTempo
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceTempoTempoEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    