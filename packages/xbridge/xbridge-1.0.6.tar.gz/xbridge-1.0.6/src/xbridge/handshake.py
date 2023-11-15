

from abc import abstractmethod
from typing import Any, Tuple
from cipher import Cipher
from Peer import HelloMsg, HelloReplyMsg, Peer, PrPeer
from config import Config
from rsa_key import RSAKey
from xbridge import ProtocalInfo
from xfmt import Item

class HandShakeProtocal:
    @abstractmethod
    async def involk(self, config: Config, peer: PrPeer) -> Cipher:
        pass
    @abstractmethod
    async def answer(self, config: Config, info: Item ) -> Tuple[Cipher, Item]:
        pass


class HandShakeV1:

    async def involk(self, config: Config, peer: PrPeer) -> Cipher:
        version = await peer.checkVersion(ProtocalInfo.supportVersions)
        print("remote xbridge version: ", version)

        rsa = RSAKey.load(config.dir)
        random = Cipher.random()
        sign = rsa.sign(random)
        
        hello = HelloMsg(config.preferLocales, rsa.pubkey_bytes, random, sign)
        # print("hello", hello)
        ret = await peer.handShake(version, hello)
        # print('ret', ret)

        reply = HelloReplyMsg.fromXDict(ret)
        # print('got reply', reply)
        iv = rsa.decrypt(reply.aesIV)
        key = rsa.decrypt(reply.aesKey)

        return Cipher(key, iv)

    async def answer(self, config: Config, info: Item ) -> Tuple[Cipher, Item]:
        
        hello = HelloMsg.fromXDict(info)
        # print('handShake info', info)
        # print('handShake info type', type(info))
        # print('handShake info pubkey', type(info.pubkey))
        peerRSA = RSAKey.fromBytes(None, hello.pubkey)

        # 1. get peer id and check permission
        peerid = peerRSA.pubkey_hash
        # if not permission.allowConnect(peerid):
        #     raise ValueError("No permission to connect from %s" % peerid)

        # 2. verify signature in hello msg
        if not peerRSA.verify(hello.random, hello.sign):
            raise ValueError("Failed to verify peer rsa pubkey")

        # 3. create random and sign
        rsa = RSAKey.load(config.dir)
        random = Cipher.random()
        sign =rsa.sign(random)

        # 4. create aes key
        cipher = Cipher.new()
        ekey = peerRSA.encrypt(cipher.key)
        eiv = peerRSA.encrypt(cipher.iv)

        return cipher, HelloReplyMsg(hello.preferLocales[0], rsa.pubkey_bytes, random, sign, ekey, eiv )