from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceSapFieldglassSapFieldglassEnum(str, Enum):
    SAP_FIELDGLASS = "sap-fieldglass"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSapFieldglass:
    r"""SourceSapFieldglass
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSapFieldglassSapFieldglassEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    