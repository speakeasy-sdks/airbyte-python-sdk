from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceTvmazeScheduleTvmazeScheduleEnum(str, Enum):
    TVMAZE_SCHEDULE = "tvmaze-schedule"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTvmazeSchedule:
    r"""SourceTvmazeSchedule
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceTvmazeScheduleTvmazeScheduleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    domestic_schedule_country_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domestic_schedule_country_code') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    web_schedule_country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('web_schedule_country_code'), 'exclude': lambda f: f is None }})
    