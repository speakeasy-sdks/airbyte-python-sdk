from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceApifyDatasetApifyDatasetEnum(str, Enum):
    APIFY_DATASET = "apify-dataset"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceApifyDataset:
    r"""SourceApifyDataset
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceApifyDatasetApifyDatasetEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetId') }})
    clean: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clean'), 'exclude': lambda f: f is None }})
    