
# Auto generate from FileReceiver.xidl

from abc import abstractmethod
import os
from typing import List


import xfmt
from interface import PrInterface, SrInterface


class FileReceiver():
    @abstractmethod
    async def askSend(self, files: List[xfmt.Stream]) -> List[bool]:
        """
        Ask to send files.

        files : A list of file streams to be sent
        return: A list of boolean values indicating accept the file or not
        """
        pass


class PrFileReceiver(PrInterface, FileReceiver):
    def __init__(self, interface: PrInterface) -> None:
        super().__init__(interface.channel, interface.obj_id)

    async def askSend(self, files: List[xfmt.Stream]) -> List[bool]:
        call = xfmt.Call.of(self.obj_id, self.askSend.__name__, [files])
        ret = await self.channel.callFuncList(call)
        return [False if v == 0 else True for v in ret.localValue]


class SrFileReceiver(SrInterface, FileReceiver):
    async def _askSend(self, files: xfmt.List) -> xfmt.List:
        ret = await self.askSend(files.localValue)
        return xfmt.List(ret)
