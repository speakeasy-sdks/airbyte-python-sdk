from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceFacebookPagesFacebookPagesEnum(str, Enum):
    FACEBOOK_PAGES = "facebook-pages"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFacebookPages:
    r"""SourceFacebookPages
    The values required to configure the source.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    airbyte_source_name: SourceFacebookPagesFacebookPagesEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    page_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_id') }})
    