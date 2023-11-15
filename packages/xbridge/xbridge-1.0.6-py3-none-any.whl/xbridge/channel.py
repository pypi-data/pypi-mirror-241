# 通道
# 用于收发数据(需要时加密/解密)
# 一次连接对用一个实例
# 
import asyncio
from abc import abstractmethod
from asyncio import Queue, StreamReader, StreamWriter, Task
import traceback
from typing import Any, Dict, List
import xfmt
from cipher import Cipher
from websockets.exceptions import ConnectionClosed
from log import logger

class Channel:

    ip_list: List[str]
    port: int

    cipher: Cipher = None
    next_cipher: Cipher = None

    running: bool

    read_task: Task
    read_queue: Queue

    # write_task: Task
    # write_queue: Queue

    # stream list that is receiving
    pending_streams: List[xfmt.Stream] = []

    # call list that is waiting for return
    pending_calls: List[xfmt.Call] = []

    # registered service objects
    # objects: List[int]
    services: Dict[str, 'IInterface'] = {}

    def __init__(self) -> None:
        # self.pending_calls = []
        # self.pending_streams = []

        self.loop = asyncio.get_event_loop()
        # self.ip_list = ip_list
        # self.port = port
        print("Channel init start")
        self.read_queue = Queue(maxsize=3)
        # self.write_queue = Queue(maxsize=3)
        # self.startx()
        print("Channel init done")
         
        print("start channel task")
        self.running = True
        # loop = asyncio.get_event_loop()
        self.read_task = self.loop.create_task(self.read_task_loop())
        # self.write_task = self.loop.create_task(self.write_task_loop())


    # def __del__(self):
    #     print("channel del...")
        

    # waiting for all task finished
    async def waitStop(self): 
        # print("waiting for write task stop...")
        # await self.write_task
        print("waiting for read task stop...")
        await self.read_task
        print("❎ all channel task stopped")


    # write item to channel (tobytes + encrypt)
    async def write_item(self, item: xfmt.Item):
        # item: XItem = await self.write_queue.get()
        if item is None:
            return
        # logger.debug("🚗 will send item %s" % item)
        try:
            data = item.toBytes()
        except Exception as e:
            print("🔥 serialize xitem failed! ", str(e))
            traceback.print_exc()
            # continue
        # # print("got data")
        if self.cipher:
            data = self.cipher.encrypt(data)
        # logger.debug("🚀 will send data[%d] %s" % (len(data), data))
        await self.send(data)
    
    # print('write task end')


    # read from channel to pipe
    async def read_task_loop(self):
        try:
            print('start channel read task...')
            while self.running:
                # print("waiting for recv...")
                # try:
                data = await self.recv(1024)
                # except ConnectionClosed:
                #     print("connection closed")
                #     return
                
                if self.next_cipher:
                    self.cipher = self.next_cipher
                    self.next_cipher = None

                # print("ok")
                logger.debug("🌝 read data[%d]" % len(data))
                if self.cipher:
                    data = self.cipher.decrypt(data)
                
                # got data
                # parser to xfmt type
                try:
                    item, used = xfmt.Item.fromBytes(data)
                except Exception as e:
                    print('🔥 parse xitem failed!', str(e))
                    traceback.print_exc()
                    continue
                # if item is None:
                #     raise ValueError("got invalid item!")
                
                logger.debug("🌞 got item: %s" % item)

                if isinstance(item, xfmt.Ret) or isinstance(item, xfmt.Err):
                    for pending_call in self.pending_calls:
                        if item.id == pending_call.id:
                            # found matched call
                            await pending_call.queue.put(item)
                            break

                elif isinstance(item, xfmt.StreamData):
                    s: xfmt.StreamData = item
                    for pending_stream in self.pending_streams:
                        # print('got stream data %d' % s.id)
                        if s.id == pending_stream.id:
                            # found matched stream
                            # await pending_stream.queue.put(s.value)
                            data = s.value
                            # print('got stream data', data)
                            if data is None:
                                self.pending_streams.remove(pending_stream)
                                # print("now stream list:", self.pending_streams)
                            await pending_stream.writeChunk(data)
                            break

                elif isinstance(item, xfmt.Call):
                    # print('got Call')
                    call: xfmt.Call = item
                    # handle call
                    if call.obj == 0:
                        # call Peer
                        service = self.services[""]
                    else:
                        for name, s in self.services.items():
                            if id(s) == call.obj:   
                                # found matched obj
                                service = s
                                break
                    try:
                        if not service:
                            raise ValueError("service not found")
                        
                        retValue = await service.call(call.func, call.params)
                        # func = getattr(service, call.func)
                        # print("parmas:", call.params)
                        # # print("local parmas:", call.params.localValue)
                        # print("#####")
                        # retValue = await func(*(call.params))
                        from interface import SrInterface
                        if isinstance(retValue, SrInterface):
                            self.registerService(type(retValue).__name__, retValue)
                            retValue = id(retValue)
                        ret = xfmt.Ret(call.id, retValue)
                        await self.write_item(ret)
                    except Exception as e:
                        traceback.print_exc()
                        err = xfmt.Err(call.id, str(e))
                        await self.write_item(err)

            
            print('read task end')
        except ConnectionClosed as e:
            print("🌙 Connection Closed")
        except Exception as e:
            traceback.print_exc()
            # print("read task: Exception occurred:", str(e))
        finally:
            # 清理
            # 1. cancel all pending call
            for call in self.pending_calls:
                await call.queue.put(None)
            # 2. save stream state
            # TODO
                
            print('❎ chanel read task END')
            await self.write_item(None) # trigger write task stop


    # send data to connection endpoint  
    @abstractmethod 
    async def send(self, data: bytes):
        raise TypeError("abstract")
        pass

    # receive data from connection endpoint
    @abstractmethod 
    async def recv(self, len: int) -> bytes:
        raise TypeError("abstract")

    # close connection endpoint
    @abstractmethod
    async def close(self):
        raise TypeError("abstract")

    def registerService(self, name: str, service: 'IInterface'):
        service.bindChannel(self)
        self.services[name] = service
        # print('channel pending calls', self.pending_calls)
        # print('channel pending streams', self.pending_streams)

    async def callFunc(self, call: xfmt.Call) -> xfmt.Item:
        self.pending_calls.append(call)
        print("call func %s ..." % call.func)
        await self.write_item(call)
        ret = await call.queue.get()
        self.pending_calls.remove(call)
        if ret is None:
            raise ValueError("Call %s is cancelled!" % call.func)
        if isinstance(ret, xfmt.Err):
            raise ValueError(ret.msg)
        return ret.value
    
    async def callFuncNumber(self, call: xfmt.Call) -> xfmt.Number:
        item = await self.callFunc(call)
        if not isinstance(item, xfmt.Number):
            raise ValueError("expect ret number")
        return item
    
    async def callFuncU16(self, call: xfmt.Call) -> xfmt.U16:
        item = await self.callFunc(call)
        if not isinstance(item, xfmt.U16):
            raise ValueError("expect ret u16")
        return item
    
    async def callFuncU8(self, call: xfmt.Call) -> xfmt.U8:
        item = await self.callFunc(call)
        if not isinstance(item, xfmt.U8):
            raise ValueError("expect ret u8")
        return item
    
    async def callFuncDict(self, call: xfmt.Call) -> xfmt.Dict:
        item = await self.callFunc(call)
        if not isinstance(item, xfmt.Dict):
            raise ValueError("expect ret dict")
        return item
    
    async def callFuncList(self, call: xfmt.Call) -> xfmt.List:
        item = await self.callFunc(call)
        if not isinstance(item, xfmt.List):
            raise ValueError("expect ret list")
        return item
    
    async def sendStream(self, stream: xfmt.Stream):
        async for data in stream.readChunks():
            # print("got part", len(data))
            await self.write_item(xfmt.StreamData(stream.id, data))
            # await self.send(xfmt.StreamData(stream.id, data).toBytes())
            # await self.write_item(xfmt.StreamData(stream.id, data))
            # await asyncio.sleep(0)
        await self.write_item(xfmt.StreamData(stream.id, None))
        

    def registerStream(self, stream: xfmt.Stream):
        # print("will receive stream... ", stream)
        self.pending_streams.append(stream)
        # print("now stream list:", self.pending_streams)
        

class WebsocketChannel(Channel):

    ws: Any

    def __init__(self, ws) -> None:
        super().__init__()
        self.ws = ws

    async def send(self, data: bytes):
        # print("ws will send: ", len(data))
        await self.ws.send(data)
        # print("ws send: ", len(data))


    async def recv(self, size: int) -> bytes:
        # print("ws: try receiv...")
        data = await self.ws.recv()
        # print("ws: received: ", len(data))
        return data

    async def close(self):
        await self.ws.close()
    

class TCPChannel(Channel):

    reader: StreamReader
    writer: StreamWriter

    def __init__(self, reader, writer) -> None:
        super().__init__()
        self.reader = reader
        self.writer = writer

    async def send(self, data: bytes):
        self.writer.write(data)
        await self.writer.drain()

    async def recv(self, size: int) -> bytes:
        data = await self.reader.read(size)
        return data

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()