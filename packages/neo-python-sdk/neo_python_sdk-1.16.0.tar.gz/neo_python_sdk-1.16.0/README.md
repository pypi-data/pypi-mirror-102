# Neo SDK: Python 3 🐍

> Neo SDK for Python with some additional libraries to support the development of Neo Sentinels (NSX).

## Terminology

- **Task**: A task (or Sentinel Task) is a job processed or created by so called Sentinels.
- **Sentinel**: Fancy name for a worker consuming / producing tasks. They are usually not that evil.
- **Particle**: All tasks / messages / responses flowing through the Neo internals are generalized as „particles“. Particles can be the payload for tasks, the response to the Neo client or just some metadata. Particles have to be objects.

## Installation

```bash
pip install neo_python_sdk
```

## Configuration

The Neo SDK can be configured through environment variables (ENVs in short). The following ENVs are supported:

- `NPQ_DISABLE_AUTOCONNECT`: Set to `true` in order to prevent the SDK from autoconnecting.
- `NPQ_NAME`: A identifiable name for your Sentinel.
- `NPQ_CA`: The CA to authenticate the NPQ against, when using TLS. See (https://docs.nats.io/developing-with-nats/security/tls)
- `NPQ_CERT`: The client cert to use signed by the `NPQ_CA`
- `NPQ_CERT_KEY`: The key belonging to `NPQ_CERT`

## Usage

To use it you have to import it in Python with the following import:

```python
import neo_python_sdk as Neo
```

## Quick start

### Consuming tasks

```python
import neo_python_sdk as Neo
import asyncio

# processing tasks requires a queue name
# the request object will be passed to the provided processor (a function)
# the "processor" should use async / await
async def start_neo_tasks(loop):
    neo = await Neo.init(loop)
    async def process_request(payload):
        res = f"Hi there, {payload["user"]}"
        return res

    await neo.process("nsx.dev.example.sayHello", process_request)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_neo_tasks(loop))
    loop.run_forever()
```

### Creating tasks

```Python
import neo_python_sdk as Neo
import asyncio

async def execute_task(loop):
    neo = await Neo.init(loop)
    response = await neo.create("nsx.dev.example.sayHello", {"user": "John"})
    print(f"Server responded: {response}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(execute_task(loop))
```
