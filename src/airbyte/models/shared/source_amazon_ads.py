from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceAmazonAdsAmazonAdsEnum(str, Enum):
    AMAZON_ADS = "amazon-ads"

class SourceAmazonAdsAuthTypeEnum(str, Enum):
    OAUTH2_0 = "oauth2.0"

class SourceAmazonAdsRegionEnum(str, Enum):
    NA = "NA"
    EU = "EU"
    FE = "FE"

class SourceAmazonAdsStateFilterEnum(str, Enum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAmazonAds:
    r"""SourceAmazonAds
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceAmazonAdsAmazonAdsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    auth_type: Optional[SourceAmazonAdsAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    look_back_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('look_back_window'), 'exclude': lambda f: f is None }})
    profiles: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profiles'), 'exclude': lambda f: f is None }})
    region: Optional[SourceAmazonAdsRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    state_filter: Optional[list[SourceAmazonAdsStateFilterEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state_filter'), 'exclude': lambda f: f is None }})
    