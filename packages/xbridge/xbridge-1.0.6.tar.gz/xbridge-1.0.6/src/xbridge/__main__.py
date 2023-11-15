
import asyncio
import configparser
import os
import sys
import uuid
from typing import List
import qrcode

from PeerService import PeerService
from FileReceiver import (FileReceiver, PrFileReceiver)
from FileReciverService import FileReceiverService
from config import Config
from connection import WSConnection
from file_stream import FileReaderStream
from find import DeviceInfo, Discovery, DiscoveryListener
from interface import IInterface
from handshake import HandShakeV1

# logging.basicConfig(level=logging.DEBUG)
# FILES_FLAG = '--with-files'
# logger.setLevel(logging.DEBUG)


async def start_service(name: str, config: Config):
    class MyPeerService(PeerService):
        async def getService(self, name: str) -> IInterface:
            print("try get service of: ", name)
            if self.config.handshake:
                if self.channel.cipher is None:
                    raise ValueError('Please handshake first!!!')
            if name == FileReceiver.__name__:
                return FileReceiverService(self.channel)
            raise ValueError("service not found!")
    
    config.handshake = HandShakeV1()
    peer = MyPeerService(config)
    conn = WSConnection()
    # conn = TCPConnection()
    async with conn.start(peer, name) as (ip, port):
        # show qrcode
        qr = qrcode.QRCode()
        qr.border = 1
        qr.add_data("%s://%s:%d" % (conn.protocol, ip, port))
        qr.print_ascii(invert=True)
        await asyncio.Future()


async def ask_send_files(service_name, files: List[str]):
    config = Config(handshake=HandShakeV1())
    # config = Config()
    conn = WSConnection()
    # conn = TCPConnection()
    async with conn.connect(service_name, config) as peer:
        obj = await peer.getService(FileReceiver.__name__)
        fileReceiver = PrFileReceiver(obj)
        streams = [FileReaderStream(f) for f in files]
        accepts = await fileReceiver.askSend(streams)
        for s, ok in zip(streams, accepts):
            if ok:
                await peer.channel.sendStream(s)


    
def discovery_service():
    class MyDiscoveryListener(DiscoveryListener):
        def onAddService(self, info: DeviceInfo):
            print('[+] %s (%s://%s:%d)' % (info.name, info.protocal, info.ip, info.port))
        
        def onUpdateService(self, info: DeviceInfo):
            print('[u] %s (%s://%s:%d)'% (info.name, info.protocal, info.ip, info.port))
        
        def onRemoveService(self, name):
            print('[-] %s' % name)
            
    listener = MyDiscoveryListener()
    discovery = Discovery(listener)
    discovery.sendFindAll()
    discovery.run()


def cmd(args: List[str]):
    argslen = len(args)
    # print("arg len = %d, args:" % argslen, args)
    # no params
    if argslen == 0 or args[0] == '-h' or args[0] == '--help':
        # version = pkg_resources.require("xbridge")[0].version
        config = configparser.ConfigParser()  
        config.read('pyproject.toml')  
        version = config['tool.poetry']['version'].strip('"')

        print("xbridge v%s" % version)

        print('\nStart service:')
        print('\txbridge [-c <config>] <server>')
        print('\nClient:')
        print('  Discover services nearby:')
        print('\txbridge -d')
        print('  Get Service info:')
        print('\txbridge <server> info')
        print('  Normoal Request:')
        print('\txbridge [-c <config>] <server> request <action> [<params...> [ --with-files <files...> ]]')
        print('  Send/Get/List file:')
        print('\txbridge [-c <config>] <server> send/get/ls [<files...>]')
        print('  Continue Session:')
        print('\txbridge [-c <config>] <server> session <id> <msgtype> [ <params...> [ --with-files <files...> ]')
        return
    
    # just discover

    if args[0] == '-d' or args[0] == 'discover':
        # bonjour.discover_service()
        discovery_service()
        return

    # got config

    if args[0] == '-c':
        config_dir = args[1]
        args = args[2:]
    else:
        config_dir = os.path.join(os.environ['HOME'], '.xbridge')

    if not os.path.exists(config_dir):
        os.makedirs(config_dir, 0o755)
    elif not os.path.isdir(config_dir):
        raise Exception("Config dir %s is not a dir!" % config_dir)
    config = Config(config_dir)
    

    # got service name

    service_name = args[0]
    args = args[1:]

    subcmd = args[0]
    print("subcmd: ", subcmd)

    #
    # server
    #

    if subcmd == 'start':
        # start service
        try:
            asyncio.run(start_service(service_name, config))
        finally:
            print("server end")
        return

    #
    # client
    #

    # got session id
    if args[0] == 'resume':
        session_id = args[1]
        args = args[2:]
    else:
        session_id = str(uuid.uuid1())

    subcmd = args[0]

    # handle request

    # service_url = xbridge.client.get_service_url(service_name)
    
    if subcmd == 'info':
        # info
        args = ['request', 'info']

    if subcmd == 'actions':
        args = ['request', 'get_actions']
        
    if subcmd == 'trust':
        # trust
        newArgs = ['request', 'trust']
        newArgs.extend(args[1:])
        args = newArgs
        # print("args:", args)

    elif subcmd == 'send':
        files = args[1:]
        try:
            asyncio.run(ask_send_files(service_name, files))
        finally:
            print("send finished")
        return
    
    elif subcmd == 'get':
        # get <files...>
        newArgs = ['request', AvailableActions.GetFiles]
        newArgs.extend(args[1:])
        args = newArgs
    elif subcmd == 'ls':
        # ls <files...>
        newArgs = ['request', AvailableActions.ListFiles]
        newArgs.extend(args[1:])
        args = newArgs

    # basic invoke request
    # <msg_type> [<action>] [<params...>] [--with-files <files...>]  
    # print(args)
    msg_type = args[0]
    action = ''
    if msg_type == 'request':
        params_index = 2
        try:
            action = args[1]
        except:
            pass
    else:
        params_index = 1

    try:
        dash_index = args.index(FILES_FLAG)
        params = args[params_index:dash_index]
        files = args[dash_index+1:]
    except:
        params = args[params_index:]
        files = []
        
    # print("action:", action)
    msg = NormalMsg(MsgType(msg_type), session_id, '', action, params, files)
    print('req:', msg.toPrettyString())
    # client.request(service_name, msg, handle_reply)

     
def main():
    try:
        args = sys.argv[1:]
        cmd(args)
    except KeyboardInterrupt:
        print("User Exit")

if __name__ == '__main__':
    main()
