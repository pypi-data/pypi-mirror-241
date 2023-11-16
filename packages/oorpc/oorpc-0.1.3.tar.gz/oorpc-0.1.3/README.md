
# oorpc

An Object-oriented Binary RPC Framework

## Library Usage
### 0. Example 
Please refer `example`
1. start server
```sh
poetry install
poetry run python example/server.py
```
2. run client to test
```sh
poetry run python example/client.py
```

接下来是详细步骤.
### 1. Define service interface (.xidl)
```java
// greeter.xidl
class NameCard {
    Str name
    Num age
    Str intro
}

class Greeter {
    NameCard exchangeNameCard(NameCard card)
    void sendFile(self, Stream file)
}

```

### 2. Generate code from xidl
```sh
xrpc-gen python greeter.xidl
```
will got file `greeter.py`
```sh
# greeter.py
    class Greeter 接口定义
    class PrGreeter 代理
    class SrGreeter 服务
```

### 3. 实现服务
1. 继承并实现`SrGreeter`
```py
class GreeterService(SrGreeter):
    async def exchangeNameCard(self, card: NameCard) -> NameCard:
        print('Got name card:')
        print('\tname:', card.name)
        print('\tage:', card.age)
        print('\tintro:', card.intro)
        return NameCard('GG', 100, 'I am the Greeter Service')
    
    async def sendFile(self, file: xfmt.Stream) -> None:
        save_dir = '__temp/'
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        s = FileWriterStream(file, save_dir + file.name)
        self.channel.registerStream(s)
```

2. 继承并实现默认服务`PeerService`的查找服务接口

```py
class MyPeerService(PeerService):
    async def getService(self, name: str) -> IInterface:
        if name == Greeter.__name__:
            return GreeterService(self.channel)
        raise ValueError("service not found!")
```


### 4. 启动服务
```py
async def start_server():
    config = Config()
    peer = MyPeerService(config)
    conn = WSConnection() # use websocket
    async with conn.start(peer, 'greeter') as (ip, port):
        print("Server: %s://%s:%d" % (conn.protocol, ip, port))
        await asyncio.Future() # wait forever
asyncio.run(start_server())
```
> 示例发布了一个名为`greeter`的websocket服务, 该服务可在局域网内自动发现

### 5. 调用服务接口
```py

async def test_client():     
    config = Config()
    conn = WSConnection() # use websocket
    async with conn.connect('greeter', config) as peer:
        # find service
        obj = await peer.getService(Greeter.__name__)
        greeter = PrGreeter(obj)

        # normal rpc call
        card = await greeter.exchangeNameCard(NameCard('Client', 50, 'I am the test client!'))
        print('Got reply:')
        print('\tname:', card.name)
        print('\tage:', card.age)
        print('\tintro:', card.intro)
        
        # Send file
        file = 'example/client.py'
        print("Ready to send file", file)
        file = FileReaderStream(file)
        await greeter.sendFile(file) # call sendFile
        await peer.channel.sendStream(file) # send file stream

asyncio.run(test_client())

```
> 查找并连接名为`greeter`的websocket 服务
### 6. 加密握手协议
config中传入handshake即可配置握手协议. 协议实现`HandShakeProtocal`
```py
config = Config(handshake=HandShakeV1())
```
> 握手和加密方式可自定义

### 7. 使用其他的连接协议
目前支持使用websocket(`WSConnection`)和tcp连接协议(`TCPConnection`), 如果想要自定义协议, 请实现`Connection`类
```py
conn = MyCustomConnection() # use custom connection protocal
```

### 8. 局域网发现
默认打开局域网发现功能, 如果想要关闭, 则在启动服务时传入参数`discoverable=False`
```py
async with conn.start(peer, name, discoverable=False) as (ip, port):
    ...
```