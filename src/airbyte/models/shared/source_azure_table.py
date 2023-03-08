from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceAzureTableAzureTableEnum(str, Enum):
    AZURE_TABLE = "azure-table"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAzureTable:
    r"""SourceAzureTable
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceAzureTableAzureTableEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    storage_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_access_key') }})
    storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_account_name') }})
    storage_endpoint_suffix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_endpoint_suffix'), 'exclude': lambda f: f is None }})
    