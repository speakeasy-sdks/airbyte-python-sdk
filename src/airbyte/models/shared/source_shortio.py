from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceShortioShortioEnum(str, Enum):
    SHORTIO = "shortio"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceShortio:
    r"""SourceShortio
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceShortioShortioEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    domain_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_id') }})
    secret_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_key') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    