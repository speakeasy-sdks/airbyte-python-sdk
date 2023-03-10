from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceStripeStripeEnum(str, Enum):
    STRIPE = "stripe"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceStripe:
    r"""SourceStripe
    The values required to configure the source.
    """
    
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    airbyte_source_name: SourceStripeStripeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    lookback_window_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_days'), 'exclude': lambda f: f is None }})
    slice_range: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slice_range'), 'exclude': lambda f: f is None }})
    