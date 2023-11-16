

import os
from typing import Any, AsyncGenerator, Coroutine, Generator, List, Optional

import log
from progress_bar import TranferBar
from xfmt import Bytes, Stream


class FileReaderStream(Stream):

    def __init__(self, file_path: str) -> None:
        super().__init__(os.path.basename(file_path), os.path.getsize(file_path))
        self.bar = TranferBar('Sending', max=self.size)
        self.filepath = file_path
        
    def __del__(self):
        self.bar.finish_lazy()  

    async def readChunks(self) -> Generator[bytes, None, None]:

        with open(self.filepath, 'rb') as file:
            while True:
                part = file.read(512*1024)
                part_len = len(part)
                if part_len <= 0:
                    break
                yield part
                self.bar.next_lazy(part_len)

        self.bar.finish_lazy()  

    
    
class FileWriterStream(Stream):

    def __init__(self, s: Stream, file_path: str) -> None:
        # print("new FileWriterStream")
        super().__init__(s.name, s.size, s.id)
        self.bar = TranferBar('Receiving', max=self.size)
        # self.filepath = file_path
        self.file = open(file_path, 'wb')

    def __del__(self):
        self.bar.finish_lazy()
        self.file.close()

    async def writeChunk(self, data: Optional[bytes]):
        if data is None:
            self.bar.finish_lazy()
            return
        data_len = len(data)
        self.bar.next_lazy(data_len)
        self.file.write(data)
    