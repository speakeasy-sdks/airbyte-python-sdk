from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceDixaDixaEnum(str, Enum):
    DIXA = "dixa"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDixa:
    r"""SourceDixa
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceDixaDixaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    