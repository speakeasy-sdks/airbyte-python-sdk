from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceBigcommerceBigcommerceEnum(str, Enum):
    BIGCOMMERCE = "bigcommerce"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBigcommerce:
    r"""SourceBigcommerce
    The values required to configure the source.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    airbyte_source_name: SourceBigcommerceBigcommerceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    store_hash: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('store_hash') }})
    