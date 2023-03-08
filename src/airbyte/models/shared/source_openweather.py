from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceOpenweatherOpenweatherEnum(str, Enum):
    OPENWEATHER = "openweather"

class SourceOpenweatherLanguageEnum(str, Enum):
    AF = "af"
    AL = "al"
    AR = "ar"
    AZ = "az"
    BG = "bg"
    CA = "ca"
    CZ = "cz"
    DA = "da"
    DE = "de"
    EL = "el"
    EN = "en"
    EU = "eu"
    FA = "fa"
    FI = "fi"
    FR = "fr"
    GL = "gl"
    HE = "he"
    HI = "hi"
    HR = "hr"
    HU = "hu"
    ID = "id"
    IT = "it"
    JA = "ja"
    KR = "kr"
    LA = "la"
    LT = "lt"
    MK = "mk"
    NO = "no"
    NL = "nl"
    PL = "pl"
    PT = "pt"
    PT_BR = "pt_br"
    RO = "ro"
    RU = "ru"
    SV = "sv"
    SE = "se"
    SK = "sk"
    SL = "sl"
    SP = "sp"
    ES = "es"
    SR = "sr"
    TH = "th"
    TR = "tr"
    UA = "ua"
    UK = "uk"
    VI = "vi"
    ZH_CN = "zh_cn"
    ZH_TW = "zh_tw"
    ZU = "zu"

class SourceOpenweatherUnitsEnum(str, Enum):
    STANDARD = "standard"
    METRIC = "metric"
    IMPERIAL = "imperial"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOpenweather:
    r"""SourceOpenweather
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceOpenweatherOpenweatherEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    appid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appid') }})
    lat: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lat') }})
    lon: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lon') }})
    lang: Optional[SourceOpenweatherLanguageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lang'), 'exclude': lambda f: f is None }})
    units: Optional[SourceOpenweatherUnitsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('units'), 'exclude': lambda f: f is None }})
    