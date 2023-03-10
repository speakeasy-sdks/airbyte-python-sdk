from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceIntercomIntercomEnum(str, Enum):
    INTERCOM = "intercom"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceIntercom:
    r"""SourceIntercom
    The values required to configure the source.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    airbyte_source_name: SourceIntercomIntercomEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    