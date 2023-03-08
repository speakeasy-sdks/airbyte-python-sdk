from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceK6CloudK6CloudEnum(str, Enum):
    K6_CLOUD = "k6-cloud"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceK6Cloud:
    r"""SourceK6Cloud
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceK6CloudK6CloudEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    