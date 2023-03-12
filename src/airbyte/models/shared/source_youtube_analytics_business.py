from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any

class SourceYoutubeAnalyticsBusinessYoutubeAnalyticsBusinessEnum(str, Enum):
    YOUTUBE_ANALYTICS_BUSINESS = "youtube-analytics-business"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceYoutubeAnalyticsBusiness:
    r"""SourceYoutubeAnalyticsBusiness
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceYoutubeAnalyticsBusinessYoutubeAnalyticsBusinessEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    