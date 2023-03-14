from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceOracleOracleEnum(str, Enum):
    ORACLE = "oracle"

class SourceOracleConnectionDataSystemIDSIDConnectionTypeEnum(str, Enum):
    SID = "sid"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleConnectionDataSystemIDSID:
    r"""SourceOracleConnectionDataSystemIDSID
    Use SID (Oracle System Identifier)
    """
    
    sid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sid') }})
    connection_type: Optional[SourceOracleConnectionDataSystemIDSIDConnectionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_type'), 'exclude': lambda f: f is None }})
    
class SourceOracleConnectionDataServiceNameConnectionTypeEnum(str, Enum):
    SERVICE_NAME = "service_name"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleConnectionDataServiceName:
    r"""SourceOracleConnectionDataServiceName
    Use service name
    """
    
    service_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_name') }})
    connection_type: Optional[SourceOracleConnectionDataServiceNameConnectionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_type'), 'exclude': lambda f: f is None }})
    
class SourceOracleEncryptionTLSEncryptedVerifyCertificateEncryptionMethodEnum(str, Enum):
    ENCRYPTED_VERIFY_CERTIFICATE = "encrypted_verify_certificate"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleEncryptionTLSEncryptedVerifyCertificate:
    r"""SourceOracleEncryptionTLSEncryptedVerifyCertificate
    Verify and use the certificate provided by the server.
    """
    
    encryption_method: SourceOracleEncryptionTLSEncryptedVerifyCertificateEncryptionMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_method') }})
    ssl_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_certificate') }})
    
class SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionAlgorithmEnum(str, Enum):
    AES256 = "AES256"
    RC4_56 = "RC4_56"
    THREE_DES168 = "3DES168"

class SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionMethodEnum(str, Enum):
    CLIENT_NNE = "client_nne"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleEncryptionNativeNetworkEncryptionNNE:
    r"""SourceOracleEncryptionNativeNetworkEncryptionNNE
    The native network encryption gives you the ability to encrypt database connections, without the configuration overhead of TCP/IP and SSL/TLS and without the need to open and listen on different ports.
    """
    
    encryption_method: SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_method') }})
    encryption_algorithm: Optional[SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionAlgorithmEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_algorithm'), 'exclude': lambda f: f is None }})
    
class SourceOracleTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    SSH_PASSWORD_AUTH = "SSH_PASSWORD_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleTunnelMethodPasswordAuthentication:
    r"""SourceOracleTunnelMethodPasswordAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: SourceOracleTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    
class SourceOracleTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    SSH_KEY_AUTH = "SSH_KEY_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleTunnelMethodSSHKeyAuthentication:
    r"""SourceOracleTunnelMethodSSHKeyAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: SourceOracleTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    
class SourceOracleTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    NO_TUNNEL = "NO_TUNNEL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleTunnelMethodNoTunnel:
    r"""SourceOracleTunnelMethodNoTunnel
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_method: SourceOracleTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracle:
    r"""SourceOracle
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceOracleOracleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    encryption: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    connection_data: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_data'), 'exclude': lambda f: f is None }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    schemas: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    