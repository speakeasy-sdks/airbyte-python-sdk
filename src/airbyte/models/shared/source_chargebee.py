from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceChargebeeChargebeeEnum(str, Enum):
    CHARGEBEE = "chargebee"

class SourceChargebeeProductCatalogEnum(str, Enum):
    ONE_0 = "1.0"
    TWO_0 = "2.0"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceChargebee:
    r"""SourceChargebee
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceChargebeeChargebeeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    product_catalog: SourceChargebeeProductCatalogEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product_catalog') }})
    site: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site') }})
    site_api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_api_key') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    