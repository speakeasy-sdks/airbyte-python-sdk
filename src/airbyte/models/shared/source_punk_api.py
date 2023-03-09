from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourcePunkAPIPunkAPIEnum(str, Enum):
    PUNK_API = "punk-api"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePunkAPI:
    r"""SourcePunkAPI
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePunkAPIPunkAPIEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    brewed_after: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brewed_after') }})
    brewed_before: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brewed_before') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    