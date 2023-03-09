from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceNetsuiteNetsuiteEnum(str, Enum):
    NETSUITE = "netsuite"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNetsuite:
    r"""SourceNetsuite
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceNetsuiteNetsuiteEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    consumer_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumer_key') }})
    consumer_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumer_secret') }})
    realm: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('realm') }})
    start_datetime: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_datetime') }})
    token_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_key') }})
    token_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_secret') }})
    object_types: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_types'), 'exclude': lambda f: f is None }})
    window_in_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_in_days'), 'exclude': lambda f: f is None }})
    