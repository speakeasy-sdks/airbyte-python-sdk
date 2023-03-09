from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceConfigcatConfigcatEnum(str, Enum):
    CONFIGCAT = "configcat"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceConfigcat:
    r"""SourceConfigcat
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceConfigcatConfigcatEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    