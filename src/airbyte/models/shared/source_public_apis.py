from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourcePublicApisPublicApisEnum(str, Enum):
    PUBLIC_APIS = "public-apis"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePublicApis:
    r"""SourcePublicApis
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePublicApisPublicApisEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    