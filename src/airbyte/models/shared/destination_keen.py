from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationKeenKeenEnum(str, Enum):
    KEEN = "keen"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationKeen:
    r"""DestinationKeen
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationKeenKeenEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    infer_timestamp: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('infer_timestamp'), 'exclude': lambda f: f is None }})
    