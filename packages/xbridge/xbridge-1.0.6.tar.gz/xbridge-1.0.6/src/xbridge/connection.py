


import asyncio
import contextlib
import socket
from typing import AsyncIterator, Optional
from channel import Channel, TCPChannel, WebsocketChannel
from cipher import Cipher
from config import Config
from find import Discovery
from Peer import HelloMsg, PrPeer, SrPeer
import websockets
from rsa_key import RSAKey
from xbridge import ProtocalInfo



async def find_service(name: str):
    d = Discovery()
    d.start()
    device = await d.find(name)
    d.stop()
    return device


def get_ip():
    ip = '172.0.0.1'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        return ip
    finally:
        s.close()


class Connection:

    protocol: str = ''
    discovery: Discovery = None

    def __init__(self) -> None:
        pass

    async def start(self, peer: SrPeer, name: str = 'xbridge', port: Optional[int] = None, discoverable = True):
        pass

    async def connect(self, name_or_url: str, config: Config) -> AsyncIterator[PrPeer]:
        pass

    def startDiscovery(self):
        if self.discovery is None:
            self.discovery = Discovery()
            self.discovery.start()
            self.discovery.sendFindAll()

    def stopDiscovery(self):
        if self.discovery:
            self.discovery.stop()
            self.discovery = None

    def onStart(self, name, ip, port):
        if self.discovery:
            new_name = self.discovery.register(name, self.protocol, ip, port)
            print("Server %s run on %s://%s:%d" % (new_name, self.protocol, ip, port))
        else:
            print("Server run on %s://%s:%d" % (self.protocol, ip, port))

    async def handleChannel(self, ch: Channel, peer):
        ch.registerService("", peer)
        await ch.waitStop()

class WSConnection(Connection):

    def __init__(self) -> None:
        super().__init__()
        self.protocol = 'ws'

    @contextlib.asynccontextmanager
    async def start(self, peer: SrPeer, name: str = 'xbridge', port: Optional[int] = None, discoverable = True):
        
        if discoverable:
            self.startDiscovery()

        async def handle_session(ws):
            print("session start...")
            await self.handleChannel(WebsocketChannel(ws), peer)
            print("session exit")

        try:
            ip = get_ip()
            async with websockets.serve(
                handle_session,
                "0.0.0.0", port,
                compression=None,
            ) as server:
                print("ws server started")
                sock_port: int = server.sockets[0].getsockname()[1]
                self.onStart(name, ip, sock_port)
                
                yield ip, sock_port
        finally:
            print("ws server end")
            self.stopDiscovery()
 
 
    @contextlib.asynccontextmanager
    async def connect(self, name_or_uri: str, config: Config) -> AsyncIterator[PrPeer]:
        if name_or_uri.startswith('ws://'):
            url = name_or_uri
        elif len(name_or_uri.split(":")) >= 2:
            url = 'ws://' + name_or_uri
        else:
            device = await find_service(name_or_uri)
            if not device:
                raise ValueError("Server %s not found!" % name_or_uri)
            url = '%s://%s:%d' % (device.protocal, device.ip, device.port)
        print('url', url)

        async with websockets.connect(url, compression=None) as websocket:

            try:
                print("session start...")

                ch = WebsocketChannel(websocket)
                peer = PrPeer(ch, 0)

                # version = await peer.checkVersion(ProtocalInfo.supportVersions)
                # print("remote xbridge version: ", version)

                if config.handshake:
                    cipher = await config.handshake.involk(config, peer)
                    ch.cipher = cipher
                    print('handshake ok')
                else:
                    print("Skip handshake!")
                
                yield peer
                await peer.close()


            finally:
                print("session end!")


class TCPConnection(Connection):

    def __init__(self) -> None:
        super().__init__()
        self.protocol = 'tcp'

    @contextlib.asynccontextmanager
    async def start(self, peer: SrPeer, name: str = 'xbridge', port: Optional[int] = None, discoverable = True):
        if discoverable:
            self.startDiscovery()

        async def handle_session(reader, writer):
            print("session start...")
            ch = TCPChannel(reader, writer)
            await self.handleChannel(ch, peer)
            print("session exit")

        try:
            ip = get_ip()
            server = await asyncio.start_server(
                handle_session,
                "0.0.0.0", port
            )
            print("tcp server started")
            sock_port: int = server.sockets[0].getsockname()[1]
            self.onStart(name, ip, sock_port)
            yield ip, sock_port
        finally:
            print("tcp server end")
            server.close()
            await server.wait_closed()


    @contextlib.asynccontextmanager
    async def connect(self, name_or_url: str, config: Config) -> AsyncIterator[PrPeer]:
        if name_or_url.startswith('tcp://'):
            host, port = name_or_url[6:].split(":")
        elif len(name_or_url.split(":")) >= 2:
            host, port = name_or_url.split(":")
        else:
            device = await find_service(name_or_url)
            if not device:
                raise ValueError("Server %s not found!" % name_or_url)
            host = device.ip
            port = device.port
        print('host', host, 'port', port)   

        reader, writer = await asyncio.open_connection(host, int(port))

        try:
            print("session start...")

            ch = TCPChannel(reader, writer)
            peer = PrPeer(ch, 0)

            if config.handshake:
                cipher = await config.handshake.involk(config, peer)
                ch.cipher = cipher
                print('handshake ok')
            else:
                print("Skip handshake!")

            print('handshake ok')
            
            yield peer
            await peer.close()


        finally:
            print("will close socket")
            writer.close()
            await writer.wait_closed()
            print("session end!")
    