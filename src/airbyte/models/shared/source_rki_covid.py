from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceRkiCovidRkiCovidEnum(str, Enum):
    RKI_COVID = "rki-covid"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRkiCovid:
    r"""SourceRkiCovid
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceRkiCovidRkiCovidEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    