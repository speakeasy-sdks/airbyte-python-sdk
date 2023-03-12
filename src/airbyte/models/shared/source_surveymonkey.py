from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSurveymonkeySurveymonkeyEnum(str, Enum):
    SURVEYMONKEY = "surveymonkey"

class SourceSurveymonkeySurveyMonkeyAuthorizationMethodAuthMethodEnum(str, Enum):
    OAUTH2_0 = "oauth2.0"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveymonkeySurveyMonkeyAuthorizationMethod:
    r"""SourceSurveymonkeySurveyMonkeyAuthorizationMethod
    The authorization method to use to retrieve data from SurveyMonkey
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    auth_method: SourceSurveymonkeySurveyMonkeyAuthorizationMethodAuthMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    
class SourceSurveymonkeyOriginDatacenterOfTheSurveyMonkeyAccountEnum(str, Enum):
    USA = "USA"
    EUROPE = "Europe"
    CANADA = "Canada"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveymonkey:
    r"""SourceSurveymonkey
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSurveymonkeySurveymonkeyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    credentials: Optional[SourceSurveymonkeySurveyMonkeyAuthorizationMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    origin: Optional[SourceSurveymonkeyOriginDatacenterOfTheSurveyMonkeyAccountEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origin'), 'exclude': lambda f: f is None }})
    survey_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_ids'), 'exclude': lambda f: f is None }})
    