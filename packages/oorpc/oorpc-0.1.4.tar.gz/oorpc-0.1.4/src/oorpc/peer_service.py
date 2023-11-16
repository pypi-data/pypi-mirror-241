


import asyncio
from typing import List

from . import xfmt
from .common import ProtocalInfo
from .config import Config
from .peer import SrPeer


class PeerService(SrPeer):

    def __init__(self, config: Config, ch=None) -> None:
        super().__init__(ch)
        self.config = config
        
    async def checkVersion(self, versions: List[int]) -> int:
        chooseVersion = 0 # not support
        versions.sort()
        for v in versions:
            if v in ProtocalInfo.supportVersions:
                chooseVersion = v
        return chooseVersion
    
    async def handShake(self, version: int, info: xfmt.Item) -> xfmt.Item:
        if not self.config.handshake:
            raise ValueError('handshake not support')
        if version not in ProtocalInfo.supportVersions:
            raise ValueError("protocal version %d is not supported. only supports %s", version, ProtocalInfo.supportVersions)
        cipher, reply = await self.config.handshake.answer(self.config, info)
        self.channel.next_cipher = cipher
        return reply
        
    async def restoreStream(self, id: int, offset: int) -> bool:
        return True
    
    async def close(self) -> bool:
        print("🌈 waiting for receive all pending data")
        while len(self.channel.pending_streams) > 0:
            await asyncio.sleep(0.2)
        # await asyncio.sleep(1)
        return True