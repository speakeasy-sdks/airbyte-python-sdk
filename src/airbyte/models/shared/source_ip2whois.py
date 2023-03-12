from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceIp2whoisIp2whoisEnum(str, Enum):
    IP2WHOIS = "ip2whois"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceIp2whois:
    r"""SourceIp2whois
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceIp2whoisIp2whoisEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    