from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceRetentlyRetentlyEnum(str, Enum):
    RETENTLY = "retently"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRetently:
    r"""SourceRetently
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceRetentlyRetentlyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    