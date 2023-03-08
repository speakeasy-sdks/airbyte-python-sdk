from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceOrbitOrbitEnum(str, Enum):
    ORBIT = "orbit"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOrbit:
    r"""SourceOrbit
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceOrbitOrbitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    workspace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace') }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    