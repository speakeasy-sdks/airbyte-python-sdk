from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceZoomZoomEnum(str, Enum):
    ZOOM = "zoom"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZoom:
    r"""SourceZoom
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceZoomZoomEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    jwt_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jwt_token') }})
    