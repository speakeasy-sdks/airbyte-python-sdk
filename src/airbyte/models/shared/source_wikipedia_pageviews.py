from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceWikipediaPageviewsWikipediaPageviewsEnum(str, Enum):
    WIKIPEDIA_PAGEVIEWS = "wikipedia-pageviews"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceWikipediaPageviews:
    r"""SourceWikipediaPageviews
    The values required to configure the source.
    """
    
    access: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access') }})
    agent: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agent') }})
    airbyte_source_name: SourceWikipediaPageviewsWikipediaPageviewsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    article: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('article') }})
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    end: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end') }})
    project: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project') }})
    start: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start') }})
    