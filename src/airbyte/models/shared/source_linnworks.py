from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields

class SourceLinnworksLinnworksEnum(str, Enum):
    LINNWORKS = "linnworks"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLinnworks:
    r"""SourceLinnworks
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceLinnworksLinnworksEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    application_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_id') }})
    application_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_secret') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    