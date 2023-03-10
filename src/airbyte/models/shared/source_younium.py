from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceYouniumYouniumEnum(str, Enum):
    YOUNIUM = "younium"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceYounium:
    r"""SourceYounium
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceYouniumYouniumEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    legal_entity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legal_entity') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    playground: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playground'), 'exclude': lambda f: f is None }})
    