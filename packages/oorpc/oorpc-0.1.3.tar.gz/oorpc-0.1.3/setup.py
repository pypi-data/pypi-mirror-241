# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['oorpc', 'oorpc.xidl']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'netifaces>=0.11.0,<0.12.0',
 'progress>=1.6,<2.0',
 'pycryptodome>=3.14.1,<4.0.0',
 'qrcode>=7.3.1,<8.0.0',
 'rsa>=4.8,<5.0',
 'websockets>=10.3,<11.0',
 'zeroconf>=0.38.5,<0.39.0']

entry_points = \
{'console_scripts': ['oorpc-gen = oorpc.__main__:main']}

setup_kwargs = {
    'name': 'oorpc',
    'version': '0.1.3',
    'description': 'An Object-oriented Binary RPC Framework',
    'long_description': '\n# oorpc\n\nAn Object-oriented Binary RPC Framework\n\n## Library Usage\n### 0. Example \nPlease refer `example`\n1. start server\n```sh\npoetry install\npoetry run python example/server.py\n```\n2. run client to test\n```sh\npoetry run python example/client.py\n```\n\n接下来是详细步骤.\n### 1. Define service interface (.xidl)\n```java\n// greeter.xidl\nclass NameCard {\n    Str name\n    Num age\n    Str intro\n}\n\nclass Greeter {\n    NameCard exchangeNameCard(NameCard card)\n    void sendFile(self, Stream file)\n}\n\n```\n\n### 2. Generate code from xidl\n```sh\nxrpc-gen python greeter.xidl\n```\nwill got file `greeter.py`\n```sh\n# greeter.py\n    class Greeter 接口定义\n    class PrGreeter 代理\n    class SrGreeter 服务\n```\n\n### 3. 实现服务\n1. 继承并实现`SrGreeter`\n```py\nclass GreeterService(SrGreeter):\n    async def exchangeNameCard(self, card: NameCard) -> NameCard:\n        print(\'Got name card:\')\n        print(\'\\tname:\', card.name)\n        print(\'\\tage:\', card.age)\n        print(\'\\tintro:\', card.intro)\n        return NameCard(\'GG\', 100, \'I am the Greeter Service\')\n    \n    async def sendFile(self, file: xfmt.Stream) -> None:\n        save_dir = \'__temp/\'\n        if not os.path.exists(save_dir):\n            os.mkdir(save_dir)\n        s = FileWriterStream(file, save_dir + file.name)\n        self.channel.registerStream(s)\n```\n\n2. 继承并实现默认服务`PeerService`的查找服务接口\n\n```py\nclass MyPeerService(PeerService):\n    async def getService(self, name: str) -> IInterface:\n        if name == Greeter.__name__:\n            return GreeterService(self.channel)\n        raise ValueError("service not found!")\n```\n\n\n### 4. 启动服务\n```py\nasync def start_server():\n    config = Config()\n    peer = MyPeerService(config)\n    conn = WSConnection() # use websocket\n    async with conn.start(peer, \'greeter\') as (ip, port):\n        print("Server: %s://%s:%d" % (conn.protocol, ip, port))\n        await asyncio.Future() # wait forever\nasyncio.run(start_server())\n```\n> 示例发布了一个名为`greeter`的websocket服务, 该服务可在局域网内自动发现\n\n### 5. 调用服务接口\n```py\n\nasync def test_client():     \n    config = Config()\n    conn = WSConnection() # use websocket\n    async with conn.connect(\'greeter\', config) as peer:\n        # find service\n        obj = await peer.getService(Greeter.__name__)\n        greeter = PrGreeter(obj)\n\n        # normal rpc call\n        card = await greeter.exchangeNameCard(NameCard(\'Client\', 50, \'I am the test client!\'))\n        print(\'Got reply:\')\n        print(\'\\tname:\', card.name)\n        print(\'\\tage:\', card.age)\n        print(\'\\tintro:\', card.intro)\n        \n        # Send file\n        file = \'example/client.py\'\n        print("Ready to send file", file)\n        file = FileReaderStream(file)\n        await greeter.sendFile(file) # call sendFile\n        await peer.channel.sendStream(file) # send file stream\n\nasyncio.run(test_client())\n\n```\n> 查找并连接名为`greeter`的websocket 服务\n### 6. 加密握手协议\nconfig中传入handshake即可配置握手协议. 协议实现`HandShakeProtocal`\n```py\nconfig = Config(handshake=HandShakeV1())\n```\n> 握手和加密方式可自定义\n\n### 7. 使用其他的连接协议\n目前支持使用websocket(`WSConnection`)和tcp连接协议(`TCPConnection`), 如果想要自定义协议, 请实现`Connection`类\n```py\nconn = MyCustomConnection() # use custom connection protocal\n```\n\n### 8. 局域网发现\n默认打开局域网发现功能, 如果想要关闭, 则在启动服务时传入参数`discoverable=False`\n```py\nasync with conn.start(peer, name, discoverable=False) as (ip, port):\n    ...\n```',
    'author': 'yudingp',
    'author_email': 'yudingp@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
