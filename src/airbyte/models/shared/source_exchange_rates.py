from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceExchangeRatesExchangeRatesEnum(str, Enum):
    EXCHANGE_RATES = "exchange-rates"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceExchangeRates:
    r"""SourceExchangeRates
    The values required to configure the source.
    """
    
    access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key') }})
    airbyte_source_name: SourceExchangeRatesExchangeRatesEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    base: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base'), 'exclude': lambda f: f is None }})
    ignore_weekends: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ignore_weekends'), 'exclude': lambda f: f is None }})
    