from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceMongodbMongodbEnum(str, Enum):
    MONGODB = "mongodb"

class SourceMongodbInstanceTypeMongoDBAtlasInstanceEnum(str, Enum):
    ATLAS = "atlas"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbInstanceTypeMongoDBAtlas:
    r"""SourceMongodbInstanceTypeMongoDBAtlas
    The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.
    """
    
    cluster_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster_url') }})
    instance: SourceMongodbInstanceTypeMongoDBAtlasInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    
class SourceMongodbInstanceTypeReplicaSetInstanceEnum(str, Enum):
    REPLICA = "replica"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbInstanceTypeReplicaSet:
    r"""SourceMongodbInstanceTypeReplicaSet
    The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.
    """
    
    instance: SourceMongodbInstanceTypeReplicaSetInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    server_addresses: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_addresses') }})
    replica_set: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replica_set'), 'exclude': lambda f: f is None }})
    
class SourceMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum(str, Enum):
    STANDALONE = "standalone"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbInstanceTypeStandaloneMongoDbInstance:
    r"""SourceMongodbInstanceTypeStandaloneMongoDbInstance
    The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.
    """
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    instance: SourceMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodb:
    r"""SourceMongodb
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceMongodbMongodbEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    auth_source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_source'), 'exclude': lambda f: f is None }})
    instance_type: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_type'), 'exclude': lambda f: f is None }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    