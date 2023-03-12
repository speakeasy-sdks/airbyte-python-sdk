from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceMssqlMssqlEnum(str, Enum):
    MSSQL = "mssql"

class SourceMssqlReplicationMethodLogicalReplicationCDCDataToSyncEnum(str, Enum):
    EXISTING_AND_NEW = "Existing and New"
    NEW_CHANGES_ONLY = "New Changes Only"

class SourceMssqlReplicationMethodLogicalReplicationCDCMethodEnum(str, Enum):
    CDC = "CDC"

class SourceMssqlReplicationMethodLogicalReplicationCDCInitialSnapshotIsolationLevelEnum(str, Enum):
    SNAPSHOT = "Snapshot"
    READ_COMMITTED = "Read Committed"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlReplicationMethodLogicalReplicationCDC:
    r"""SourceMssqlReplicationMethodLogicalReplicationCDC
    CDC uses {TBC} to detect inserts, updates, and deletes. This needs to be configured on the source database itself.
    """
    
    method: SourceMssqlReplicationMethodLogicalReplicationCDCMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    data_to_sync: Optional[SourceMssqlReplicationMethodLogicalReplicationCDCDataToSyncEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_to_sync'), 'exclude': lambda f: f is None }})
    initial_waiting_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initial_waiting_seconds'), 'exclude': lambda f: f is None }})
    snapshot_isolation: Optional[SourceMssqlReplicationMethodLogicalReplicationCDCInitialSnapshotIsolationLevelEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('snapshot_isolation'), 'exclude': lambda f: f is None }})
    
class SourceMssqlReplicationMethodStandardMethodEnum(str, Enum):
    STANDARD = "STANDARD"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlReplicationMethodStandard:
    r"""SourceMssqlReplicationMethodStandard
    Standard replication requires no setup on the DB side but will not be able to represent deletions incrementally.
    """
    
    method: SourceMssqlReplicationMethodStandardMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    
class SourceMssqlSslMethodEncryptedVerifyCertificateSslMethodEnum(str, Enum):
    ENCRYPTED_VERIFY_CERTIFICATE = "encrypted_verify_certificate"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlSslMethodEncryptedVerifyCertificate:
    r"""SourceMssqlSslMethodEncryptedVerifyCertificate
    Verify and use the certificate provided by the server.
    """
    
    ssl_method: SourceMssqlSslMethodEncryptedVerifyCertificateSslMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    host_name_in_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostNameInCertificate'), 'exclude': lambda f: f is None }})
    
class SourceMssqlSslMethodEncryptedTrustServerCertificateSslMethodEnum(str, Enum):
    ENCRYPTED_TRUST_SERVER_CERTIFICATE = "encrypted_trust_server_certificate"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlSslMethodEncryptedTrustServerCertificate:
    r"""SourceMssqlSslMethodEncryptedTrustServerCertificate
    Use the certificate provided by the server without verification. (For testing purposes only!)
    """
    
    ssl_method: SourceMssqlSslMethodEncryptedTrustServerCertificateSslMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    
class SourceMssqlTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    SSH_PASSWORD_AUTH = "SSH_PASSWORD_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlTunnelMethodPasswordAuthentication:
    r"""SourceMssqlTunnelMethodPasswordAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: SourceMssqlTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    
class SourceMssqlTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    SSH_KEY_AUTH = "SSH_KEY_AUTH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlTunnelMethodSSHKeyAuthentication:
    r"""SourceMssqlTunnelMethodSSHKeyAuthentication
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    tunnel_method: SourceMssqlTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    
class SourceMssqlTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    NO_TUNNEL = "NO_TUNNEL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlTunnelMethodNoTunnel:
    r"""SourceMssqlTunnelMethodNoTunnel
    Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.
    """
    
    tunnel_method: SourceMssqlTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssql:
    r"""SourceMssql
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceMssqlMssqlEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    replication_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_method'), 'exclude': lambda f: f is None }})
    schemas: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    ssl_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method'), 'exclude': lambda f: f is None }})
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    