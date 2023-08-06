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
import upbit

print(upbit.get_markets())
```

### Exchange
```python
import upbit

client = upbit.Client('your_access_key', 'your_secret_key')
print(client.get_accounts())
```

### WebSocket
```python
import upbit

class WS(upbit.WebSocket):
    async def on_connect(self):
        print('connect')
        await self.send_field()
        
    async def on_disconnect(self):
        print('disconnect')
        
    async def on_data(self, data: dict):
        print(data)

WS().run()
```