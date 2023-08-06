# upbit.py
![PyPi](https://img.shields.io/pypi/v/upbit.py)

Upbit API (업비트 API) 

## Install
```shell
pip install upbit.py
```

## Example
### Quotation
```python
from upbit import Client

client = Client('', '')
print(client.get_markets())
```

### Exchange
```python
from upbit import Client

client = Client('access_key', 'secret_key')
print(client.get_accounts())
```

### WebSocket
```python
from upbit import WebSocket

class WS(WebSocket):
    async def on_connect(self):
        await self.send_field()

    async def on_response(self, response: dict):
        print(response)

WS().run()
```