from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionCreate:
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    