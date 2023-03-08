from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceGnewsGnewsEnum(str, Enum):
    GNEWS = "gnews"

class SourceGnewsCountryEnum(str, Enum):
    AU = "au"
    BR = "br"
    CA = "ca"
    CN = "cn"
    EG = "eg"
    FR = "fr"
    DE = "de"
    GR = "gr"
    HK = "hk"
    IN = "in"
    IE = "ie"
    IL = "il"
    IT = "it"
    JP = "jp"
    NL = "nl"
    NO = "no"
    PK = "pk"
    PE = "pe"
    PH = "ph"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SG = "sg"
    ES = "es"
    SE = "se"
    CH = "ch"
    TW = "tw"
    UA = "ua"
    GB = "gb"
    US = "us"

class SourceGnewsInEnum(str, Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    CONTENT = "content"

class SourceGnewsLanguageEnum(str, Enum):
    AR = "ar"
    ZH = "zh"
    NL = "nl"
    EN = "en"
    FR = "fr"
    DE = "de"
    EL = "el"
    HE = "he"
    HI = "hi"
    IT = "it"
    JA = "ja"
    ML = "ml"
    MR = "mr"
    NO = "no"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    ES = "es"
    SV = "sv"
    TA = "ta"
    TE = "te"
    UK = "uk"

class SourceGnewsNullableEnum(str, Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    CONTENT = "content"

class SourceGnewsSortByEnum(str, Enum):
    PUBLISHED_AT = "publishedAt"
    RELEVANCE = "relevance"

class SourceGnewsTopHeadlinesTopicEnum(str, Enum):
    BREAKING_NEWS = "breaking-news"
    WORLD = "world"
    NATION = "nation"
    BUSINESS = "business"
    TECHNOLOGY = "technology"
    ENTERTAINMENT = "entertainment"
    SPORTS = "sports"
    SCIENCE = "science"
    HEALTH = "health"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGnews:
    r"""SourceGnews
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGnewsGnewsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    country: Optional[SourceGnewsCountryEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    in_: Optional[list[SourceGnewsInEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in'), 'exclude': lambda f: f is None }})
    language: Optional[SourceGnewsLanguageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})
    nullable: Optional[list[SourceGnewsNullableEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nullable'), 'exclude': lambda f: f is None }})
    sortby: Optional[SourceGnewsSortByEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortby'), 'exclude': lambda f: f is None }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    top_headlines_query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_headlines_query'), 'exclude': lambda f: f is None }})
    top_headlines_topic: Optional[SourceGnewsTopHeadlinesTopicEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_headlines_topic'), 'exclude': lambda f: f is None }})
    