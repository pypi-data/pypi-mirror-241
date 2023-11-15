
import os

# from handshake import HandShakeProtocal

class UserInfo:
    pass


class Config:
    preferLocales = ['zh']
    handshake: 'HandShakeProtocal' # handshake for encryption
    dir: str

    def __init__(self, dir: str = None, handshake: 'HandShakeProtocal' = None) -> None:
        # load config from dir
        # ...
        self.handshake = handshake
        print('dir', dir)
        if dir:
            self.dir = dir
        else:
            # default_dir = 
            # global default_dir
            self.dir = os.path.join(os.environ['HOME'], '.xbridge')

    def getRSA():
        pass

    def getInfo() -> UserInfo:
        pass
    
