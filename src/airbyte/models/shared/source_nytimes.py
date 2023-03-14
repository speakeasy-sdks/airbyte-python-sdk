from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceNytimesNytimesEnum(str, Enum):
    NYTIMES = "nytimes"

class SourceNytimesShareTypeUsedForMostPopularSharedStreamEnum(str, Enum):
    FACEBOOK = "facebook"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNytimes:
    r"""SourceNytimes
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceNytimesNytimesEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    period: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    share_type: Optional[SourceNytimesShareTypeUsedForMostPopularSharedStreamEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('share_type'), 'exclude': lambda f: f is None }})
    