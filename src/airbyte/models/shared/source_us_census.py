from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceUsCensusUsCensusEnum(str, Enum):
    US_CENSUS = "us-census"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceUsCensus:
    r"""SourceUsCensus
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceUsCensusUsCensusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    query_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_path') }})
    query_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_params'), 'exclude': lambda f: f is None }})
    