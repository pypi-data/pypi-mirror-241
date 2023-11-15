# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xbridge', 'xbridge.old', 'xbridge.xidl']

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
{'console_scripts': ['xbridge = xbridge.__main__:main']}

setup_kwargs = {
    'name': 'xbridge',
    'version': '1.0.6',
    'description': 'An Object-oriented Binary RPC Framework',
    'long_description': '\n# xbridge\n\nAn Object-oriented Binary RPC Framework\n\n## Library Usage\n\n### 1. define service interface (.xidl)\n```java\n// Greeter.xidl\nclass HelloReq {\n    Str name\n}\n\nclass HelloReply {\n    Str msg\n}\n\nclass Greeter {\n    HelloReply sayHello(HelloReq req)\n    sendFile(self, Stream)\n}\n\n```\n\n### 2. generate code from xidl\n```sh\nxbridge gen python Greeter.xidl\n```\nwill got file `Greeter.py`\n```sh\n# Greeter.py\n    class Greeter 接口定义\n    class PrGreeter 代理\n    class SrGreeter 服务\n```\n\n### 3. 实现服务\n1. 继承并实现`SrGreeter`\n```py\nclass GreeterService(SrGreeter):\n    def sayHello(req: HelloReq) -> HelloReply:\n        print(\'hello %s\' % req.name)\n        return HelloReply(\'Hello, \', req.name)\n\n    def sendFile(file: Stream) -> None:\n        save_dir = \'__temp/\'\n        if not os.path.exists(save_dir):\n            os.mkdir(save_dir)\n        s = FileWriterStream(file, save_dir + file.name)\n        self.channel.registerStream(s) # will receive the stream\n```\n\n2. 继承并实现默认服务`SrPeer`的查找服务接口\n\n```py\nclass MyPeerService(SrPeer):\n    def getService(name: str) -> IInterface:\n        if name == Greeter.__name__:\n            return GreeterService(self.channel)\n        raise ValueError("service not found!")\n```\n\n\n### 4. 启动服务\n```py\nconfig = Config()\npeer = MyPeerService(config)\nconn = WSConnection() # use websocket\nasync with conn.start(peer, \'greeter\') as (ip, port):\n    # server started, show qrcode\n    qr = qrcode.QRCode()\n    qr.border = 1\n    qr.add_data("%s://%s:%d" % (conn.protocol, ip, port))\n    qr.print_ascii(invert=True)\n    await asyncio.Future() # wait forever\n\n```\n> 示例发布了一个名为`greeter`的websocket服务, 该服务可在局域网内自动发现\n\n### 5. 调用服务接口\n```py\nconfig = Config()\nconn = WSConnection() # use websocket\nasync with conn.connect(\'greeter\', config) as peer:\n    # find service\n    obj = await peer.getService(Greeter.__name__)\n    greeter = PrGreeter(obj)\n\n    # normal rpc call\n    ret = await greeter.sayHello(HelloMsg(\'Daniel\'))\n    print(ret.msg) # Hello, Daniel\n    \n    # Send file\n    file = FileReaderStream(\'file.txt\')\n    await greeter.sendFile(file) # call sendFile\n    await peer.channel.sendStream(file) # send file stream\n\n```\n> 查找并连接名为`greeter`的websocket 服务\n### 6. 加密握手协议\nconfig中传入handshake即可配置握手协议. 协议实现`HandShakeProtocal`\n```py\nconfig = Config(handshake=HandShakeV1())\n```\n> 握手和加密方式可自定义\n\n### 7. 使用其他的连接协议\n目前支持使用websocket(`WSConnection`)和tcp连接协议(`TCPConnection`), 如果想要自定义协议, 请实现`Connection`类\n```py\nconn = MyCustomConnection() # use custom connection protocal\n```\n\n### 8. 局域网发现\n默认打开局域网发现功能, 如果想要关闭, 则在启动服务时传入参数`discoverable=False`\n```py\nasync with conn.start(peer, name, discoverable=False) as (ip, port):\n    ...\n```\n\n## Command line Usage\n\n### Install\nsuggest using `pipx` to install command\n```sh\npipx install xbridge\n```\n\n### 帮助\n```sh\nxbridge [-h|--help]\n```\n\n### 搜索服务\n```sh\nxbridge -d\n```\n\n### 启动服务\n```sh\nxbridge [-c <config_dir>] <name> start\n```\n> `<config_dir>`是本地配置目录, 包含密钥和未结束的sessions. 默认路径`$HOME/.xbridge`\n> `<name>`是建议的服务名, 实际服务名以启动后为准\n\n### 发起请求\n\n#### 一般命令格式\n```sh\nxbridge [-c <config_dir>] <name> request [<action> <params...> [ --with-files <files...> ]]\n```\n> `<name>`可以是服务名, 也可以是`[protocal://]ip:port`格式字符串\n\n\n#### 快捷子命令\n\n- 查看服务支持的所有请求\n\n```sh\nxbridge <server> info\n# 等价于:\nxbridge <server> request info\n```\n\n- 发送文件:\n```sh\nxbridge <server> send <files...>\n# 等价于:\nxbridge <server> request send_files <files...> --with-files <files...>\n```\n- 获取文件\n```sh\nxbridge <server> get <files...>\n# 等价于:\nxbridge <server> request get_files <files...>\n```\n- 列出文件\n\n```sh\nxbridge <server> ls [<files...>]\n# 等价于:\nxbridge <server> request list_files [<files...>]\n```\n\n### 断点继续\n```sh\nxbridge [-c <config_dir>] <server> resume <session> <msg_type> [ <params...> [ --with-files <files...> ]]\n```\n> `<msg_type>`: reply/done/get_file\n> \n\n### Configuration\n\nconfiguration dir is by default located in `$HOME/.xbridge/`.\nYou can specify the dir by `-c <config_dir>`\n\n#### RSA keys\nrsa key用来表明自己的身份.\n`prikey.pem` 私钥\n`pubkey.pem` 公钥\n\n> 密钥会在首次使用时自动生成\n#### Permissions\n\n```json\n// permissions.json\n[\n    {\n        "client_hash": "xxxx",\n        "allow_connect": true,\n        "always_allow_actions": {\n            "send_files": true,\n            "get_files": false,\n            "list_files": true,\n        }\n    }\n]\n\n```\n\n#### Sessions\n该目录用户存放所有未结束的sessions\n\n',
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
