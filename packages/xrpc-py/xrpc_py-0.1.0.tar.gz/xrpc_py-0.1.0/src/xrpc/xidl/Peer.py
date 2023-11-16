class HelloMsg:
    preferLocales: str = None
    #// 支持的locale列表
    pubkey: bytes = None
    #// 公钥
    random: bytes = None
    #// 随机数16B + 时间戳
    sign: bytes = None

class HelloReplyMsg:
    locale: str = None
    #// 将会使用的locale
    pubkey: str = None
    #// 公钥
    random: str = None
    #// 随机数 16B + 时间戳
    sign: str = None
    #// 随机数的签名, 为了证明公钥是自己的
    aesKey: bytes = None
    #// 用对方公钥加密的AES key
    aesIV: bytes = None

class Stream:
    id: int = None
    size: int = None
    offset: int = None

class Peer:
    #*
    #* 选择兼容的协议版本
    #*
    #* versions: caller supported version List
    #* return: version that will use
    #*
    def pickVersion(self, versions: list[int]) -> int:
        pass
    #* 握手
    #*
    #* version: protocal version
    def handShake(self, version: int, info: HelloMsg) -> HelloReplyMsg:
        pass
    #*
    #* 恢复流
    def restoreStream(self, id: int, offset: int) -> bool:
        pass

