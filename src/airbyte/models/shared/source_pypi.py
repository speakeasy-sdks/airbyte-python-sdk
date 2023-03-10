from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourcePypiPypiEnum(str, Enum):
    PYPI = "pypi"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePypi:
    r"""SourcePypi
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePypiPypiEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    project_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_name') }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    