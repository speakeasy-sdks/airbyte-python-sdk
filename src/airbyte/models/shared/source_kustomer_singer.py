from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceKustomerSingerKustomerSingerEnum(str, Enum):
    KUSTOMER_SINGER = "kustomer-singer"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceKustomerSinger:
    r"""SourceKustomerSinger
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceKustomerSingerKustomerSingerEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    