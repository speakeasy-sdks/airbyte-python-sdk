<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
   
req = operations.ResetConnectionRequest(
    path_params=operations.ResetConnectionPathParams(
        connection_id="unde",
    ),
)
    
res = s.connections.reset_connection(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->