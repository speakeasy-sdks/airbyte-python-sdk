from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceSmailySmailyEnum(str, Enum):
    SMAILY = "smaily"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSmaily:
    r"""SourceSmaily
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSmailySmailyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_password') }})
    api_subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_subdomain') }})
    api_username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_username') }})
    