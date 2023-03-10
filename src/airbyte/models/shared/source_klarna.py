from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceKlarnaKlarnaEnum(str, Enum):
    KLARNA = "klarna"

class SourceKlarnaRegionEnum(str, Enum):
    EU = "eu"
    US = "us"
    OC = "oc"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceKlarna:
    r"""SourceKlarna
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceKlarnaKlarnaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    playground: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playground') }})
    region: SourceKlarnaRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    