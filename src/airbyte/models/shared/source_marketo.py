from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceMarketoMarketoEnum(str, Enum):
    MARKETO = "marketo"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMarketo:
    r"""SourceMarketo
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceMarketoMarketoEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    domain_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_url') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    