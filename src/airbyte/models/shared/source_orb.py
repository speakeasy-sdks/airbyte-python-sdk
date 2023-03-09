from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceOrbOrbEnum(str, Enum):
    ORB = "orb"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOrb:
    r"""SourceOrb
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceOrbOrbEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    lookback_window_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_days'), 'exclude': lambda f: f is None }})
    numeric_event_properties_keys: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numeric_event_properties_keys'), 'exclude': lambda f: f is None }})
    plan_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan_id'), 'exclude': lambda f: f is None }})
    string_event_properties_keys: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('string_event_properties_keys'), 'exclude': lambda f: f is None }})
    subscription_usage_grouping_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription_usage_grouping_key'), 'exclude': lambda f: f is None }})
    