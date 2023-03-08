<!-- Start SDK Example Usage -->
```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte()
s.config_security(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    )
)
   
req = operations.CreateConnectionRequest(
    request=shared.ConnectionCreate(
        destination_id="unde",
        name="deserunt",
        source_id="porro",
    ),
)
    
res = s.connections.create_connection(req)

if res.connection_id is not None:
    # handle response
```
<!-- End SDK Example Usage -->