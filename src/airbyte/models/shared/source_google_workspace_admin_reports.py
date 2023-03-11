from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceGoogleWorkspaceAdminReportsGoogleWorkspaceAdminReportsEnum(str, Enum):
    GOOGLE_WORKSPACE_ADMIN_REPORTS = "google-workspace-admin-reports"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleWorkspaceAdminReports:
    r"""SourceGoogleWorkspaceAdminReports
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceGoogleWorkspaceAdminReportsGoogleWorkspaceAdminReportsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    lookback: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback'), 'exclude': lambda f: f is None }})
    