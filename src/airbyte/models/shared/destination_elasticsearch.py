from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationElasticsearchElasticsearchEnum(str, Enum):
    ELASTICSEARCH = "elasticsearch"

class DestinationElasticsearchAuthenticationMethodUsernamePasswordMethodEnum(str, Enum):
    BASIC = "basic"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationElasticsearchAuthenticationMethodUsernamePassword:
    r"""DestinationElasticsearchAuthenticationMethodUsernamePassword
    Basic auth header with a username and password
    """
    
    method: DestinationElasticsearchAuthenticationMethodUsernamePasswordMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    
class DestinationElasticsearchAuthenticationMethodAPIKeySecretMethodEnum(str, Enum):
    SECRET = "secret"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationElasticsearchAuthenticationMethodAPIKeySecret:
    r"""DestinationElasticsearchAuthenticationMethodAPIKeySecret
    Use a api key and secret combination to authenticate
    """
    
    api_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKeyId') }})
    api_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKeySecret') }})
    method: DestinationElasticsearchAuthenticationMethodAPIKeySecretMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationElasticsearch:
    r"""DestinationElasticsearch
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationElasticsearchElasticsearchEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    endpoint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint') }})
    authentication_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authenticationMethod'), 'exclude': lambda f: f is None }})
    ca_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate'), 'exclude': lambda f: f is None }})
    upsert: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upsert'), 'exclude': lambda f: f is None }})
    