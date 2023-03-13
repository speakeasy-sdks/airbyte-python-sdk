from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationPostgresPostgresEnum(str, Enum):
    POSTGRES = "postgres"

class DestinationPostgresSslModeVerifyFullModeEnum(str, Enum):
    VERIFY_FULL = "verify-full"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeVerifyFull:
    r"""DestinationPostgresSslModeVerifyFull
    Verify-full SSL mode.
    """
    
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    client_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate') }})
    client_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key') }})
    mode: DestinationPostgresSslModeVerifyFullModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    
class DestinationPostgresSslModeVerifyCaModeEnum(str, Enum):
    VERIFY_CA = "verify-ca"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeVerifyCa:
    r"""DestinationPostgresSslModeVerifyCa
    Verify-ca SSL mode.
    """
    
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    mode: DestinationPostgresSslModeVerifyCaModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    
class DestinationPostgresSslModeRequireModeEnum(str, Enum):
    REQUIRE = "require"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeRequire:
    r"""DestinationPostgresSslModeRequire
    Require SSL mode.
    """
    
    mode: DestinationPostgresSslModeRequireModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    
class DestinationPostgresSslModePreferModeEnum(str, Enum):
    PREFER = "prefer"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModePrefer:
    r"""DestinationPostgresSslModePrefer
    Prefer SSL mode.
    """
    
    mode: DestinationPostgresSslModePreferModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    
class DestinationPostgresSslModeAllowModeEnum(str, Enum):
    ALLOW = "allow"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeAllow:
    r"""DestinationPostgresSslModeAllow
    Allow SSL mode.
    """
    
    mode: DestinationPostgresSslModeAllowModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    
class DestinationPostgresSslModeDisableModeEnum(str, Enum):
    DISABLE = "disable"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeDisable:
    r"""DestinationPostgresSslModeDisable
    Disable SSL.
    """
    
    mode: DestinationPostgresSslModeDisableModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    
class DestinationPostgresTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    SSH_PASSWORD_AUTH = "SSH_PASSWORD_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresTunnelMethodPasswordAuthentication:
    r"""DestinationPostgresTunnelMethodPasswordAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: DestinationPostgresTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    
class DestinationPostgresTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    SSH_KEY_AUTH = "SSH_KEY_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresTunnelMethodSSHKeyAuthentication:
    r"""DestinationPostgresTunnelMethodSSHKeyAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: DestinationPostgresTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    
class DestinationPostgresTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    NO_TUNNEL = "NO_TUNNEL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresTunnelMethodNoTunnel:
    r"""DestinationPostgresTunnelMethodNoTunnel
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_method: DestinationPostgresTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgres:
    r"""DestinationPostgres
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationPostgresPostgresEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    ssl_mode: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode'), 'exclude': lambda f: f is None }})
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    