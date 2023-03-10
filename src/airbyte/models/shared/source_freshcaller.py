from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceFreshcallerFreshcallerEnum(str, Enum):
    FRESHCALLER = "freshcaller"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFreshcaller:
    r"""SourceFreshcaller
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceFreshcallerFreshcallerEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    start_date: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    requests_per_minute: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requests_per_minute'), 'exclude': lambda f: f is None }})
    sync_lag_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync_lag_minutes'), 'exclude': lambda f: f is None }})
    