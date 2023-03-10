from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationMongodbMongodbEnum(str, Enum):
    MONGODB = "mongodb"

class DestinationMongodbAuthTypeLoginPasswordAuthorizationEnum(str, Enum):
    LOGIN_PASSWORD = "login/password"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbAuthTypeLoginPassword:
    r"""DestinationMongodbAuthTypeLoginPassword
    Login/Password.
    """
    
    authorization: DestinationMongodbAuthTypeLoginPasswordAuthorizationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    
class DestinationMongodbAuthTypeNoneAuthorizationEnum(str, Enum):
    NONE = "none"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbAuthTypeNone:
    r"""DestinationMongodbAuthTypeNone
    None.
    """
    
    authorization: DestinationMongodbAuthTypeNoneAuthorizationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    
class DestinationMongodbInstanceTypeMongoDBAtlasInstanceEnum(str, Enum):
    ATLAS = "atlas"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbInstanceTypeMongoDBAtlas:
    r"""DestinationMongodbInstanceTypeMongoDBAtlas
    MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.
    """
    
    cluster_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster_url') }})
    instance: DestinationMongodbInstanceTypeMongoDBAtlasInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    
class DestinationMongodbInstanceTypeReplicaSetInstanceEnum(str, Enum):
    REPLICA = "replica"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbInstanceTypeReplicaSet:
    r"""DestinationMongodbInstanceTypeReplicaSet
    MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.
    """
    
    instance: DestinationMongodbInstanceTypeReplicaSetInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    server_addresses: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_addresses') }})
    replica_set: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replica_set'), 'exclude': lambda f: f is None }})
    
class DestinationMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum(str, Enum):
    STANDALONE = "standalone"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbInstanceTypeStandaloneMongoDbInstance:
    r"""DestinationMongodbInstanceTypeStandaloneMongoDbInstance
    MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.
    """
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    instance: DestinationMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    
class DestinationMongodbTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    SSH_PASSWORD_AUTH = "SSH_PASSWORD_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbTunnelMethodPasswordAuthentication:
    r"""DestinationMongodbTunnelMethodPasswordAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: DestinationMongodbTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    
class DestinationMongodbTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    SSH_KEY_AUTH = "SSH_KEY_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbTunnelMethodSSHKeyAuthentication:
    r"""DestinationMongodbTunnelMethodSSHKeyAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: DestinationMongodbTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    
class DestinationMongodbTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    NO_TUNNEL = "NO_TUNNEL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbTunnelMethodNoTunnel:
    r"""DestinationMongodbTunnelMethodNoTunnel
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_method: DestinationMongodbTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodb:
    r"""DestinationMongodb
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationMongodbMongodbEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    auth_type: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    instance_type: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_type'), 'exclude': lambda f: f is None }})
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    