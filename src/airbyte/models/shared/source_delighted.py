from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields

class SourceDelightedDelightedEnum(str, Enum):
    DELIGHTED = "delighted"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDelighted:
    r"""SourceDelighted
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceDelightedDelightedEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    since: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('since'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    