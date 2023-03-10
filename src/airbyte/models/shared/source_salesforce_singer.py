from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceSalesforceSingerSalesforceSingerEnum(str, Enum):
    SALESFORCE_SINGER = "salesforce-singer"

class SourceSalesforceSingerAPITypeEnum(str, Enum):
    BULK = "BULK"
    REST = "REST"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSalesforceSinger:
    r"""SourceSalesforceSinger
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSalesforceSingerSalesforceSingerEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_type: SourceSalesforceSingerAPITypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_type') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    is_sandbox: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox'), 'exclude': lambda f: f is None }})
    quota_percent_per_run: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quota_percent_per_run'), 'exclude': lambda f: f is None }})
    quota_percent_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quota_percent_total'), 'exclude': lambda f: f is None }})
    