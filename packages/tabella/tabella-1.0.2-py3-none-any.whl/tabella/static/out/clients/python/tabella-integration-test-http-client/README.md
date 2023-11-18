# Tabella Integration Test HTTP Client

Tabella Integration Test Python HTTP client.

## Example Usage

```python
import asyncio

from tabella_integration_test_client.client import TabellaIntegrationTestClient


async def main() -> None:
    # Get an instance of the client.
    client = TabellaIntegrationTestClient(headers={})
    # Use client for method calls...


if __name__ == "__main__":
    asyncio.run(main())
```

## Build Installable Tarball Locally

```shell
python3 setupy.py sdist --formats=gztar
```
