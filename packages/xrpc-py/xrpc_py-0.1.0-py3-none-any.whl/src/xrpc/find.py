

from abc import abstractmethod
import asyncio
from asyncio import Queue
from dataclasses import dataclass
from enum import Enum
import struct
from threading import Thread
import traceback
from typing import Any, Dict, List, Optional

import socket

import xfmt  
  
# mcast_group = ('224.1.1.1', 5007)
mcast_group = ('224.0.0.251', 5355)
# mcast_group = ('224.0.0.168', 53318)

class DiscoveryType(Enum):
    Annouce = "ANNOUCE"
    Find = "FIND"
    FindAll = "FINDALL"
    Reply = "REPLY"
    Remove = "REMOVE"

@dataclass
class DeviceInfo:
    name: str
    protocal: str
    ip: str
    port: int

class DiscoveryListener:
    @abstractmethod
    def onRemoveService(self, name):
        pass

    @abstractmethod
    def onAddService(self, info: DeviceInfo):
        pass

    @abstractmethod
    def onUpdateService(self, info: DeviceInfo):
        pass

class Discovery(Thread):

    thisDevice: DeviceInfo = None
    isRunning = False
    devices: Dict[str, DeviceInfo] = {}
    find_queue: Queue

    listener: DiscoveryListener

    def __init__(self, listener = None) -> None:
        super().__init__()
        self.listener = listener
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        mreq = struct.pack("4sL", socket.inet_aton(mcast_group[0]), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, "SO_REUSEPORT"):
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            
        self.sock.bind(('0.0.0.0', mcast_group[1]))

    def __del__(self):
    #    print('Discovery.__del__')
       self.stop()

    # def start(self) -> None:
    #     super().start()
    #     self.sendFindAll()
       
    def stop(self):
        self.isRunning = False
        # print("running", self.isRunning)
        self.unregister()

    def isMe(self, name: str) -> bool:
        if self.thisDevice:
            return self.thisDevice.name == name
        return False

    async def find(self, name: str) -> Optional[DeviceInfo]:
        d = self.devices.get(name)
        if d:
            return d
        # send 
        self.sendFind(name)
        await asyncio.sleep(1)
        return self.devices.get(name)


    def register(self, name, protocal, ip, port) -> str:
        print("register...")
        while True:
            d = self.devices.get(name)
            if d is None:
                # can't find same name
                break
            name = name + '_1'

        self.thisDevice = DeviceInfo(name, protocal, ip, port)
        # send
        msg = xfmt.List([DiscoveryType.Annouce.value, name, protocal, ip, port]) 
        self.send(msg)

        return name
    
    def unregister(self):
        if self.thisDevice:
            self.send(xfmt.List([DiscoveryType.Remove.value, self.thisDevice.name]))
            self.thisDevice = None

    def send(self, msg: xfmt.Item):
        # print("send item", msg)
        self.sock.sendto(msg.toBytes(), mcast_group)
        # self.sock.send(msg.toBytes())

    def sendReply(self, info: DeviceInfo):
        reply = xfmt.List([DiscoveryType.Reply.value, info.name, info.protocal, info.ip, info.port])
        self.send(reply)

    def sendFind(self, name: str):
        self.send(xfmt.List([DiscoveryType.Find.value, name]))

    def sendFindAll(self):
        self.send(xfmt.List([DiscoveryType.FindAll.value]))

    def run(self):
        # print("discovery watcher is running")
        self.isRunning = True
        self.sock.settimeout(1)
        while self.isRunning:
            try:
                data = self.sock.recv(1024)
            except Exception:
                continue
            # print('Discovery got:', data)
            try:
                item, used = xfmt.Item.fromBytes(data)
                if not isinstance(item, xfmt.List):
                    # print('got mcast not list, skip')
                    continue

                # print('Discovery got item:', item)
                
                req = item.localValue
                dtype = DiscoveryType(req[0])

                if dtype == DiscoveryType.Annouce:
    
                    name = req[1]
                    if self.isMe(name):
                        continue

                    protocal = req[2]
                    ip = req[3]
                    port = req[4]
                    d = self.devices.get(name)
                    if not d:
                        d = DeviceInfo(name, protocal, ip, port)
                        self.devices[name] = d
                        if self.listener:
                            self.listener.onAddService(d)
                    else:
                        d.protocal = protocal
                        d.ip = ip
                        d.port = port
                        if self.listener:
                            self.listener.onUpdateService(d)

                    # always reply my
                    if self.thisDevice:
                        self.sendReply(self.thisDevice)

                elif dtype == DiscoveryType.Remove:
                    name = req[1]
                    if self.isMe(name):
                        continue
                    d = self.devices.get(name)
                    if d:
                        self.devices.pop(name)
                        if self.listener:
                            self.listener.onRemoveService(name)

                elif dtype == DiscoveryType.Find:
                    # reply my if matched
                    if self.isMe(req[1]):
                        self.sendReply(self.thisDevice)

                elif dtype == DiscoveryType.FindAll:
                    # always reply my
                    if self.thisDevice:
                        self.sendReply(self.thisDevice)

                elif dtype ==  DiscoveryType.Reply:
                    # got reply
                    name = req[1]
                    if self.isMe(name):
                        continue
                    protocal = req[2]
                    ip = req[3]
                    port = req[4]
                    d = self.devices.get(name)
                    if not d:
                        # new got info
                        d = DeviceInfo(name, protocal, ip, port)
                        self.devices[name] = d
                        if self.listener:
                            self.listener.onAddService(d)
                    else:
                        # update info
                        d.protocal = protocal
                        d.ip = ip
                        d.port = port
                        if self.listener:
                            self.listener.onUpdateService(d)

            except Exception as e:
                traceback.print_exc()
        
        # print("discovery watcher is stopped")





