from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationRocksetRocksetEnum(str, Enum):
    ROCKSET = "rockset"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRockset:
    r"""DestinationRockset
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationRocksetRocksetEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    workspace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace') }})
    api_server: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_server'), 'exclude': lambda f: f is None }})
    