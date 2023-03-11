from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceCoinmarketcapCoinmarketcapEnum(str, Enum):
    COINMARKETCAP = "coinmarketcap"

class SourceCoinmarketcapDataTypeEnum(str, Enum):
    LATEST = "latest"
    HISTORICAL = "historical"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCoinmarketcap:
    r"""SourceCoinmarketcap
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceCoinmarketcapCoinmarketcapEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    data_type: SourceCoinmarketcapDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_type') }})
    symbols: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbols'), 'exclude': lambda f: f is None }})
    