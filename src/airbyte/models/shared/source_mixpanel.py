from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceMixpanelMixpanelEnum(str, Enum):
    MIXPANEL = "mixpanel"

class SourceMixpanelCredentialsProjectSecretOptionTitleEnum(str, Enum):
    PROJECT_SECRET = "Project Secret"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMixpanelCredentialsProjectSecret:
    r"""SourceMixpanelCredentialsProjectSecret
    Choose how to authenticate to Mixpanel
    """
    
    api_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_secret') }})
    option_title: Optional[SourceMixpanelCredentialsProjectSecretOptionTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    
class SourceMixpanelCredentialsServiceAccountOptionTitleEnum(str, Enum):
    SERVICE_ACCOUNT = "Service Account"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMixpanelCredentialsServiceAccount:
    r"""SourceMixpanelCredentialsServiceAccount
    Choose how to authenticate to Mixpanel
    """
    
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    option_title: Optional[SourceMixpanelCredentialsServiceAccountOptionTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    
class SourceMixpanelRegionEnum(str, Enum):
    US = "US"
    EU = "EU"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMixpanel:
    r"""SourceMixpanel
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceMixpanelMixpanelEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    attribution_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribution_window'), 'exclude': lambda f: f is None }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    date_window_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_window_size'), 'exclude': lambda f: f is None }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    project_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id'), 'exclude': lambda f: f is None }})
    project_timezone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_timezone'), 'exclude': lambda f: f is None }})
    region: Optional[SourceMixpanelRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    select_properties_by_default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('select_properties_by_default'), 'exclude': lambda f: f is None }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    