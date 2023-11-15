

        

from abc import ABC
import xfmt
from channel import Channel


class IInterface(ABC):
    obj_id: int = -1
    channel: Channel = None
    def bindChannel(self, ch: Channel):
        self.channel = ch

class PrInterface(IInterface):
    def __init__(self, ch, obj_id: int) -> None:
        self.channel = ch
        self.obj_id = obj_id

class SrInterface(IInterface):

    def __init__(self, ch = None) -> None:
        self.obj_id = id(self)
        self.channel = ch

    async def call(self, func_name: str, params: xfmt.List):
        func = getattr(self, '_' + func_name)
        return await func(*(params.value))
