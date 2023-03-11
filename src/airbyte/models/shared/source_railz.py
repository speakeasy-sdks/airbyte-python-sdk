from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceRailzRailzEnum(str, Enum):
    RAILZ = "railz"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRailz:
    r"""SourceRailz
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceRailzRailzEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    secret_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_key') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    