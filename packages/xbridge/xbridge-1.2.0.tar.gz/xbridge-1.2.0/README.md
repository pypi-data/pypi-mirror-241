
# xbridge

An xrpc based tool for securely transmitting in a local network


## Command line Usage

### Install
suggest using `pipx` to install command
```sh
pipx install xbridge
```

### 帮助
```sh
xbridge [-h|--help]
```

### 搜索服务
```sh
xbridge -d
```

### 启动服务
```sh
xbridge [-c <config_dir>] <name> start
```
> `<config_dir>`是本地配置目录, 包含密钥和未结束的sessions. 默认路径`$HOME/.xbridge`
> `<name>`是建议的服务名, 实际服务名以启动后为准

### 发起请求

#### 一般命令格式
```sh
xbridge [-c <config_dir>] <name> request [<action> <params...> [ --with-files <files...> ]]
```
> `<name>`可以是服务名, 也可以是`[protocal://]ip:port`格式字符串


#### 快捷子命令

- 查看服务支持的所有请求

```sh
xbridge <server> info
# 等价于:
xbridge <server> request info
```

- 发送文件:
```sh
xbridge <server> send <files...>
# 等价于:
xbridge <server> request send_files <files...> --with-files <files...>
```
- 获取文件
```sh
xbridge <server> get <files...>
# 等价于:
xbridge <server> request get_files <files...>
```
- 列出文件

```sh
xbridge <server> ls [<files...>]
# 等价于:
xbridge <server> request list_files [<files...>]
```

### 断点继续
```sh
xbridge [-c <config_dir>] <server> resume <session> <msg_type> [ <params...> [ --with-files <files...> ]]
```
> `<msg_type>`: reply/done/get_file
> 

### Configuration

configuration dir is by default located in `$HOME/.xbridge/`.
You can specify the dir by `-c <config_dir>`

#### RSA keys
rsa key用来表明自己的身份.
`prikey.pem` 私钥
`pubkey.pem` 公钥

> 密钥会在首次使用时自动生成
#### Permissions

```json
// permissions.json
[
    {
        "client_hash": "xxxx",
        "allow_connect": true,
        "always_allow_actions": {
            "send_files": true,
            "get_files": false,
            "list_files": true,
        }
    }
]

```

#### Sessions
该目录用户存放所有未结束的sessions

