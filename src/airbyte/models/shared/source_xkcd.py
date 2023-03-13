from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceXkcdXkcdEnum(str, Enum):
    XKCD = "xkcd"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceXkcd:
    r"""SourceXkcd
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceXkcdXkcdEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    