from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceGoogleDirectoryGoogleDirectoryEnum(str, Enum):
    GOOGLE_DIRECTORY = "google-directory"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleDirectory:
    r"""SourceGoogleDirectory
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGoogleDirectoryGoogleDirectoryEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    