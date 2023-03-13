from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceFaunaFaunaEnum(str, Enum):
    FAUNA = "fauna"

class SourceFaunaCollectionDeletionsEnabledDeletionModeEnum(str, Enum):
    DELETED_FIELD = "deleted_field"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaunaCollectionDeletionsEnabled:
    r"""SourceFaunaCollectionDeletionsEnabled
    <b>This only applies to incremental syncs.</b> <br>
    Enabling deletion mode informs your destination of deleted documents.<br>
    Disabled - Leave this feature disabled, and ignore deleted documents.<br>
    Enabled - Enables this feature. When a document is deleted, the connector exports a record with a \"deleted at\" column containing the time that the document was deleted.
    """
    
    column: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column') }})
    deletion_mode: SourceFaunaCollectionDeletionsEnabledDeletionModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletion_mode') }})
    
class SourceFaunaCollectionDeletionsDisabledDeletionModeEnum(str, Enum):
    IGNORE = "ignore"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaunaCollectionDeletionsDisabled:
    r"""SourceFaunaCollectionDeletionsDisabled
    <b>This only applies to incremental syncs.</b> <br>
    Enabling deletion mode informs your destination of deleted documents.<br>
    Disabled - Leave this feature disabled, and ignore deleted documents.<br>
    Enabled - Enables this feature. When a document is deleted, the connector exports a record with a \"deleted at\" column containing the time that the document was deleted.
    """
    
    deletion_mode: SourceFaunaCollectionDeletionsDisabledDeletionModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletion_mode') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaunaCollection:
    r"""SourceFaunaCollection
    Settings for the Fauna Collection.
    """
    
    deletions: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletions') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFauna:
    r"""SourceFauna
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceFaunaFaunaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    scheme: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme') }})
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    collection: Optional[SourceFaunaCollection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection'), 'exclude': lambda f: f is None }})
    