


import os
from typing import List
import xfmt
from FileReceiver import SrFileReceiver
from file_stream import FileWriterStream


class FileReceiverService(SrFileReceiver):
    async def askSend(self, files: List[xfmt.Stream]) -> List[bool]:
        save_dir = '__temp/'
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for f in files:
            s = FileWriterStream(f, save_dir + f.name)
            self.channel.registerStream(s)
        return [True for s in files]
