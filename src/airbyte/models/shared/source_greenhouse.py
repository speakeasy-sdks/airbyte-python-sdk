from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceGreenhouseGreenhouseEnum(str, Enum):
    GREENHOUSE = "greenhouse"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGreenhouse:
    r"""SourceGreenhouse
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGreenhouseGreenhouseEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    