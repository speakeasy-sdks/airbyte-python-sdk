from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourcePolygonStockAPIPolygonStockAPIEnum(str, Enum):
    POLYGON_STOCK_API = "polygon-stock-api"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePolygonStockAPI:
    r"""SourcePolygonStockAPI
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePolygonStockAPIPolygonStockAPIEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKey') }})
    end_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    multiplier: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('multiplier') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    stocks_ticker: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stocksTicker') }})
    timespan: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timespan') }})
    adjusted: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjusted'), 'exclude': lambda f: f is None }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})
    