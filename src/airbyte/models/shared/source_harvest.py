from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceHarvestHarvestEnum(str, Enum):
    HARVEST = "harvest"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHarvest:
    r"""SourceHarvest
    The values required to configure the source.
    """
    
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    airbyte_source_name: SourceHarvestHarvestEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    replication_start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_start_date') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    replication_end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_end_date'), 'exclude': lambda f: f is None }})
    