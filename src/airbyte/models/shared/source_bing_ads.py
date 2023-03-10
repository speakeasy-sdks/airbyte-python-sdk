from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceBingAdsBingAdsEnum(str, Enum):
    BING_ADS = "bing-ads"

class SourceBingAdsAuthMethodEnum(str, Enum):
    OAUTH2_0 = "oauth2.0"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBingAds:
    r"""SourceBingAds
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceBingAdsBingAdsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    developer_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('developer_token') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    reports_start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reports_start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    auth_method: Optional[SourceBingAdsAuthMethodEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    tenant_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tenant_id'), 'exclude': lambda f: f is None }})
    