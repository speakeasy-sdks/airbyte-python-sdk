from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationMssqlMssqlEnum(str, Enum):
    MSSQL = "mssql"

class DestinationMssqlSslMethodEncryptedVerifyCertificateSslMethodEnum(str, Enum):
    ENCRYPTED_VERIFY_CERTIFICATE = "encrypted_verify_certificate"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlSslMethodEncryptedVerifyCertificate:
    r"""DestinationMssqlSslMethodEncryptedVerifyCertificate
    Verify and use the certificate provided by the server.
    """
    
    ssl_method: DestinationMssqlSslMethodEncryptedVerifyCertificateSslMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    host_name_in_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostNameInCertificate'), 'exclude': lambda f: f is None }})
    
class DestinationMssqlSslMethodEncryptedTrustServerCertificateSslMethodEnum(str, Enum):
    ENCRYPTED_TRUST_SERVER_CERTIFICATE = "encrypted_trust_server_certificate"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlSslMethodEncryptedTrustServerCertificate:
    r"""DestinationMssqlSslMethodEncryptedTrustServerCertificate
    Use the certificate provided by the server without verification. (For testing purposes only!)
    """
    
    ssl_method: DestinationMssqlSslMethodEncryptedTrustServerCertificateSslMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    
class DestinationMssqlTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    SSH_PASSWORD_AUTH = "SSH_PASSWORD_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlTunnelMethodPasswordAuthentication:
    r"""DestinationMssqlTunnelMethodPasswordAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: DestinationMssqlTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    
class DestinationMssqlTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    SSH_KEY_AUTH = "SSH_KEY_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlTunnelMethodSSHKeyAuthentication:
    r"""DestinationMssqlTunnelMethodSSHKeyAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: DestinationMssqlTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    
class DestinationMssqlTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    NO_TUNNEL = "NO_TUNNEL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlTunnelMethodNoTunnel:
    r"""DestinationMssqlTunnelMethodNoTunnel
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_method: DestinationMssqlTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssql:
    r"""DestinationMssql
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationMssqlMssqlEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    ssl_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method'), 'exclude': lambda f: f is None }})
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    