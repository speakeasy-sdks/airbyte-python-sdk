from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceLaunchdarklyLaunchdarklyEnum(str, Enum):
    LAUNCHDARKLY = "launchdarkly"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLaunchdarkly:
    r"""SourceLaunchdarkly
    The values required to configure the source.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    airbyte_source_name: SourceLaunchdarklyLaunchdarklyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    