from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceTiktokMarketingTiktokMarketingEnum(str, Enum):
    TIKTOK_MARKETING = "tiktok-marketing"

class SourceTiktokMarketingCredentialsSandboxAccessTokenAuthTypeEnum(str, Enum):
    SANDBOX_ACCESS_TOKEN = "sandbox_access_token"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTiktokMarketingCredentialsSandboxAccessToken:
    r"""SourceTiktokMarketingCredentialsSandboxAccessToken
    Authentication method
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    advertiser_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advertiser_id') }})
    auth_type: Optional[SourceTiktokMarketingCredentialsSandboxAccessTokenAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    
class SourceTiktokMarketingCredentialsOAuth20AuthTypeEnum(str, Enum):
    OAUTH2_0 = "oauth2.0"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTiktokMarketingCredentialsOAuth20:
    r"""SourceTiktokMarketingCredentialsOAuth20
    Authentication method
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    app_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_id') }})
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    advertiser_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advertiser_id'), 'exclude': lambda f: f is None }})
    auth_type: Optional[SourceTiktokMarketingCredentialsOAuth20AuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    
class SourceTiktokMarketingReportAggregationGranularityEnum(str, Enum):
    LIFETIME = "LIFETIME"
    DAY = "DAY"
    HOUR = "HOUR"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTiktokMarketing:
    r"""SourceTiktokMarketing
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceTiktokMarketingTiktokMarketingEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    report_granularity: Optional[SourceTiktokMarketingReportAggregationGranularityEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('report_granularity'), 'exclude': lambda f: f is None }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    