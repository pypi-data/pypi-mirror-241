
import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, AsyncIterator, Coroutine, Dict, List, Tuple

import xfmt

from interface import IInterface, PrInterface, SrInterface



@dataclass
class HelloMsg(xfmt.Item):
    preferLocales: List[str] = None
    #// 支持的locale列表
    pubkey: bytes = None
    #// 公钥
    random: bytes = None
    #// 随机数16B + 时间戳
    sign: bytes = None

    def toBytes(self) -> bytes:
        return xfmt.Dict(vars(self)).toBytes()
    
    def getLocalValue(self) -> Any:
        return self
    
    @staticmethod
    def fromXDict(xdict: xfmt.Dict):
        preferLocales = xdict.value['preferLocales'].localValue
        pubkey = xdict.value['pubkey'].localValue
        sign = xdict.value['sign'].localValue
        random = xdict.value['random'].localValue
        return HelloMsg(preferLocales, pubkey, random, sign)
    
    @staticmethod
    def fromBytes(data: bytes) -> Tuple['HelloMsg', int]:
        xdict, used = xfmt.Dict.fromBytes(data)   
        return HelloMsg.fromXDict(xdict), used


@dataclass
class HelloReplyMsg(xfmt.Item):
    locale: str = None
    #// 将会使用的locale
    pubkey: bytes = None
    #// 公钥
    random: bytes = None
    #// 随机数 16B + 时间戳
    sign: bytes = None
    #// 随机数的签名, 为了证明公钥是自己的
    aesKey: bytes = None
    #// 用对方公钥加密的AES key
    aesIV: bytes = None

    def toBytes(self) -> bytes:
        # dict = vars(self)
        # dict['__class__'] = self.__class__.__name__
        return xfmt.Dict(vars(self)).toBytes()
    
    @staticmethod
    def fromXDict(xdict: xfmt.Dict) -> 'HelloReplyMsg':
        locale = xdict.value['locale'].localValue
        pubkey = xdict.value['pubkey'].localValue
        random = xdict.value['random'].localValue
        sign = xdict.value['sign'].localValue
        aesKey = xdict.value['aesKey'].localValue
        aesIV = xdict.value['aesIV'].localValue
        return HelloReplyMsg(locale, pubkey, random, sign, aesKey, aesIV )

    @staticmethod
    def fromBytes(data: bytes) -> Tuple['HelloReplyMsg', int]:      
        xdict, used = xfmt.Dict.fromBytes(data)  
        return HelloReplyMsg.fromXDict(xdict), used


class Peer:

    @abstractmethod
    async def checkVersion(self, versions: List[int]) -> int:
        pass

    @abstractmethod
    async def handShake(self, version: int, info: xfmt.Item) -> xfmt.Item:
        pass

    @abstractmethod
    async def restoreStream(self, id: int, offset: int) -> bool:
        pass

    @abstractmethod
    async def close(self) -> bool:
        """Notify that connection will close"""
        pass

    @abstractmethod
    async def getService(self, name: str) -> IInterface:
        """ Get remote service by name 
        """
        pass


class PrPeer(PrInterface, Peer):

    async def checkVersion(self, versions: List[int]) -> int:
        call = xfmt.Call.of(self.obj_id, self.checkVersion.__name__, [versions])
        ret = await self.channel.callFuncNumber(call)
        return ret.localValue

    async def handShake(self, version: int, info: xfmt.Item) -> xfmt.Item:
        call = xfmt.Call.of(self.obj_id, self.handShake.__name__, [version, info])
        return await self.channel.callFunc(call)
    
    async def restoreStream(self, id: xfmt.Number, offset: xfmt.Number) -> bool:
        call = xfmt.Call.of(self.obj_id, self.restoreStream.__name__, [id, offset])
        ret = await self.channel.callFuncU8(call)
        return ret.value != 0
    
    async def close(self) -> bool:
        call = xfmt.Call.of(self.obj_id, self.close.__name__, [])
        ret = await self.channel.callFuncU8(call)
        return ret.value != 0
    
    async def getService(self, name: str) -> IInterface:
        call = xfmt.Call.of(self.obj_id, self.getService.__name__, [name])
        ret = await self.channel.callFuncNumber(call)
        return PrInterface(self.channel, ret.localValue)


class SrPeer(SrInterface, Peer):
   
    async def _checkVersion(self, versions: xfmt.List) -> xfmt.Number:
        ret = await self.checkVersion(versions.localValue)
        return xfmt.Number.of(ret)

    async def _handShake(self, version: xfmt.Number, info: xfmt.Item) -> xfmt.Item:
        return await self.handShake(version.localValue, info)

    async def _restoreStream(self, id: xfmt.Number, offset: xfmt.Number) -> xfmt.U8:
        ret = await self.restoreStream(id.localValue, offset.localValue)
        return xfmt.U8(1 if ret else 0)

    async def _close(self) -> bool:
        ret = await self.close()
        return xfmt.U8(1 if ret else 0)
    
    async def _getService(self, name: xfmt.Str) -> IInterface:
        return await self.getService(name.localValue)

