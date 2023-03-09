from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSenseforceSenseforceEnum(str, Enum):
    SENSEFORCE = "senseforce"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSenseforce:
    r"""SourceSenseforce
    The values required to configure the source.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    airbyte_source_name: SourceSenseforceSenseforceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    backend_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('backend_url') }})
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_id') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    slice_range: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slice_range'), 'exclude': lambda f: f is None }})
    