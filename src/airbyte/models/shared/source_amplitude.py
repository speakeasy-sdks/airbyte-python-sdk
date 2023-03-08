from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceAmplitudeAmplitudeEnum(str, Enum):
    AMPLITUDE = "amplitude"

class SourceAmplitudeDataRegionEnum(str, Enum):
    STANDARD_SERVER = "Standard Server"
    EU_RESIDENCY_SERVER = "EU Residency Server"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAmplitude:
    r"""SourceAmplitude
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceAmplitudeAmplitudeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    secret_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_key') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    data_region: Optional[SourceAmplitudeDataRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_region'), 'exclude': lambda f: f is None }})
    