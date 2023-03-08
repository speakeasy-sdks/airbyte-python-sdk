from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourcePocketPocketEnum(str, Enum):
    POCKET = "pocket"

class SourcePocketContentTypeEnum(str, Enum):
    ARTICLE = "article"
    VIDEO = "video"
    IMAGE = "image"

class SourcePocketDetailTypeEnum(str, Enum):
    SIMPLE = "simple"
    COMPLETE = "complete"

class SourcePocketSortByEnum(str, Enum):
    NEWEST = "newest"
    OLDEST = "oldest"
    TITLE = "title"
    SITE = "site"

class SourcePocketStateEnum(str, Enum):
    UNREAD = "unread"
    ARCHIVE = "archive"
    ALL = "all"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePocket:
    r"""SourcePocket
    The values required to configure the source.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    airbyte_source_name: SourcePocketPocketEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    consumer_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumer_key') }})
    content_type: Optional[SourcePocketContentTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content_type'), 'exclude': lambda f: f is None }})
    detail_type: Optional[SourcePocketDetailTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail_type'), 'exclude': lambda f: f is None }})
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    favorite: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('favorite'), 'exclude': lambda f: f is None }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search'), 'exclude': lambda f: f is None }})
    since: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('since'), 'exclude': lambda f: f is None }})
    sort: Optional[SourcePocketSortByEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})
    state: Optional[SourcePocketStateEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    