from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceWhiskyHunterWhiskyHunterEnum(str, Enum):
    WHISKY_HUNTER = "whisky-hunter"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceWhiskyHunter:
    r"""SourceWhiskyHunter
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceWhiskyHunterWhiskyHunterEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    