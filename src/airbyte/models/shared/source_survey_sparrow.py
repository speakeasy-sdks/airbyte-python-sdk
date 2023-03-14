from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceSurveySparrowSurveySparrowEnum(str, Enum):
    SURVEY_SPARROW = "survey-sparrow"

class SourceSurveySparrowRegionGlobalAccountURLBaseEnum(str, Enum):
    HTTPS_API_SURVEYSPARROW_COM_V3 = "https://api.surveysparrow.com/v3"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveySparrowRegionGlobalAccount:
    r"""SourceSurveySparrowRegionGlobalAccount
    Is your account location is EU based? If yes, the base url to retrieve data will be different.
    """
    
    url_base: Optional[SourceSurveySparrowRegionGlobalAccountURLBaseEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_base'), 'exclude': lambda f: f is None }})
    
class SourceSurveySparrowRegionEUBasedAccountURLBaseEnum(str, Enum):
    HTTPS_EU_API_SURVEYSPARROW_COM_V3 = "https://eu-api.surveysparrow.com/v3"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveySparrowRegionEUBasedAccount:
    r"""SourceSurveySparrowRegionEUBasedAccount
    Is your account location is EU based? If yes, the base url to retrieve data will be different.
    """
    
    url_base: Optional[SourceSurveySparrowRegionEUBasedAccountURLBaseEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_base'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveySparrow:
    r"""SourceSurveySparrow
    The values required to configure the source.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    airbyte_source_name: SourceSurveySparrowSurveySparrowEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    region: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    survey_id: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_id'), 'exclude': lambda f: f is None }})
    