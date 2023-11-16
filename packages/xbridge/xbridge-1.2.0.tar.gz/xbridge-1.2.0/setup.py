# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xbridge']

package_data = \
{'': ['*']}

install_requires = \
['oorpc>=0.1.3,<0.2.0']

entry_points = \
{'console_scripts': ['xbridge = xbridge.__main__:main']}

setup_kwargs = {
    'name': 'xbridge',
    'version': '1.2.0',
    'description': 'A Securely Data Transmitting Tool',
    'long_description': '\n# xbridge\n\nAn xrpc based tool for securely transmitting in a local network\n\n\n## Command line Usage\n\n### Install\nsuggest using `pipx` to install command\n```sh\npipx install xbridge\n```\n\n### 帮助\n```sh\nxbridge [-h|--help]\n```\n\n### 搜索服务\n```sh\nxbridge -d\n```\n\n### 启动服务\n```sh\nxbridge [-c <config_dir>] <name> start\n```\n> `<config_dir>`是本地配置目录, 包含密钥和未结束的sessions. 默认路径`$HOME/.xbridge`\n> `<name>`是建议的服务名, 实际服务名以启动后为准\n\n### 发起请求\n\n#### 一般命令格式\n```sh\nxbridge [-c <config_dir>] <name> request [<action> <params...> [ --with-files <files...> ]]\n```\n> `<name>`可以是服务名, 也可以是`[protocal://]ip:port`格式字符串\n\n\n#### 快捷子命令\n\n- 查看服务支持的所有请求\n\n```sh\nxbridge <server> info\n# 等价于:\nxbridge <server> request info\n```\n\n- 发送文件:\n```sh\nxbridge <server> send <files...>\n# 等价于:\nxbridge <server> request send_files <files...> --with-files <files...>\n```\n- 获取文件\n```sh\nxbridge <server> get <files...>\n# 等价于:\nxbridge <server> request get_files <files...>\n```\n- 列出文件\n\n```sh\nxbridge <server> ls [<files...>]\n# 等价于:\nxbridge <server> request list_files [<files...>]\n```\n\n### 断点继续\n```sh\nxbridge [-c <config_dir>] <server> resume <session> <msg_type> [ <params...> [ --with-files <files...> ]]\n```\n> `<msg_type>`: reply/done/get_file\n> \n\n### Configuration\n\nconfiguration dir is by default located in `$HOME/.xbridge/`.\nYou can specify the dir by `-c <config_dir>`\n\n#### RSA keys\nrsa key用来表明自己的身份.\n`prikey.pem` 私钥\n`pubkey.pem` 公钥\n\n> 密钥会在首次使用时自动生成\n#### Permissions\n\n```json\n// permissions.json\n[\n    {\n        "client_hash": "xxxx",\n        "allow_connect": true,\n        "always_allow_actions": {\n            "send_files": true,\n            "get_files": false,\n            "list_files": true,\n        }\n    }\n]\n\n```\n\n#### Sessions\n该目录用户存放所有未结束的sessions\n\n',
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
