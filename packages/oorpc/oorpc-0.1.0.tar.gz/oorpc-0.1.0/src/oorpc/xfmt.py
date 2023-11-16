

import struct
from abc import ABC, abstractmethod
from asyncio import Queue
from dataclasses import dataclass
from enum import Enum
from typing import AsyncGenerator, Generator, Optional, Tuple, Union
import typing

class XType(Enum):
    End = b'\x00'

    I8 = b'a'
    U8 = b'A'
    I16 = b'h'
    U16 = b'H'
    I32 = b'i'
    U32 = b'I'
    I64 = b'q'
    U64 = b'Q'

    Bytes = b'B'
    Str = b'S'
    List = b'L'
    Dict = b'D'

    Call = b'C'
    Ret = b'R'
    Err = b'E'
    Stream = b'T'
    StreamData = b't'

    @staticmethod
    def isNumber(byte: int):
        if byte in [XType.U8.intValue,
                    XType.I8.intValue,
                    XType.U16.intValue,
                    XType.I16.intValue,
                    XType.U32.intValue,
                    XType.I32.intValue,
                    XType.U64.intValue,
                    XType.I64.intValue,
                    ]:
            return True
        # return (byte & 0xF0) == 0x10
        return False
    
    @property
    def intValue(self):
        return self.value[0]

class Item:

    def __init__(self) -> None:
        raise TypeError("can't init XItem")

    @abstractmethod
    def getLocalValue(self) -> typing.Any:
        raise ValueError("not implement")
        pass

    @property
    def localValue(self) -> typing.Any:
        # print("localValue of ", self)
        return self.getLocalValue()

    @abstractmethod
    def toBytes(self) -> bytes:
        raise ValueError("XItem.toBytes not implement")
        
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['Item', int]:
        # print("data[0]=%x" % data[0])
        if data[0] == XType.End.intValue:
            return End.fromBytes(data)
        if XType.isNumber(data[0]):
            return Number.fromBytes(data)
        if data[0] == XType.Str.intValue:
            return Str.fromBytes(data)
        if data[0] == XType.Bytes.intValue:
            return Bytes.fromBytes(data)
        if data[0] == XType.List.intValue:
            return List.fromBytes(data)
        if data[0] == XType.Dict.intValue:
            return Dict.fromBytes(data)
        if data[0] == XType.Call.intValue:
            return Call.fromBytes(data)
        if data[0] == XType.Ret.intValue:
            return Ret.fromBytes(data)
        if data[0] == XType.Err.intValue:
            return Err.fromBytes(data)
        if data[0] == XType.Stream.intValue:
            return Stream.fromBytes(data)
        if data[0] == XType.StreamData.intValue:
            return StreamData.fromBytes(data)
        
        # print("invalid xitem data 0x%X" % data[0])
        print('data', data)
        raise TypeError('invalid item type 0x%02X(\'%c\')' % (data[0], data[0]))

    @staticmethod
    def of(value: typing.Any) -> 'Item':
        # print('try get XItem of ', value)
        if isinstance(value, Item):
            return value
        if isinstance(value, bool):
            return U8(1 if value else 0)
        if isinstance(value, int):
            return Number.of(value)
        if isinstance(value, str):
            return Str(value)
        if isinstance(value, bytes):
            return Bytes(value)
        if isinstance(value, list):
            return List(value)
        if isinstance(value, dict):
            return Dict(value)
        if value is None:
            return End()
        raise TypeError("%s can't convert to XItem" % type(value))

class End(Item):
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'End'
    
    def toBytes(self) -> bytes:
        return XType.End.value
    
    def getLocalValue(self) -> typing.Any:
        return None
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['End', int]:
        return End(), 1

class Number(Item):

    value: int

    def __init__(self, value: int) -> None:
        self.value = value

    def getLocalValue(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return 'Number(%d)' % self.value

    @staticmethod
    def of(value: int) -> 'Number':
        if value > 0:
            if value < 256:
                return U8(value)
            if value < 65535:
                return U16(value)
            return U64(value)
        else:
            if value >= -128:
                return I8(value)
            if value >= -32768:
                return I16(value)
            return I64(value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['Number', int]:
        if data[0] == XType.U8.intValue:
            return U8.fromBytes(data)
        if data[0] == XType.I8.intValue:
            return I8.fromBytes(data)
        if data[0] == XType.U16.intValue:
            return U16.fromBytes(data)
        if data[0] == XType.I16.intValue:
            return I16.fromBytes(data)
        if data[0] == XType.U32.intValue:
            return U32.fromBytes(data)
        if data[0] == XType.I32.intValue:
            return I32.fromBytes(data)
        if data[0] == XType.U64.intValue:
            return U64.fromBytes(data)
        if data[0] == XType.I64.intValue:
            return I64.fromBytes(data)
        print('data', data)
        raise TypeError("invalid number type 0x%02X(\'%c\')" % (data[0], data[0]))


class U8(Number):

    def __repr__(self) -> str:
        return 'U8(%d)' % self.value
    
    def toBytes(self) -> bytes:
        # print("self value: %d" % self.value)
        return XType.U8.value + struct.pack('>B', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['U8', int]:
        if len(data) < 2:
            raise TypeError("data not enough")
        v = struct.unpack('>B', data[1:2])[0]
        return U8(v), 2

class I8(Number):

    def __repr__(self) -> str:
        return 'I8(%d)' % self.value

    def toBytes(self) -> bytes:
        return XType.I8.value + struct.pack('>b', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['I8', int]:
        if len(data) < 2:
            raise TypeError("data not enough")
        v = struct.unpack('>b', data[1:2])[0]
        return I8(v), 2
    

class U16(Number):

    def __repr__(self) -> str:
        return 'U16(%d)' % self.value
    
    def toBytes(self) -> bytes:
        return XType.U16.value + struct.pack('>H', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['U16', int]:
        if len(data) < 3:
            raise TypeError("data not enough")
        v = struct.unpack('>H', data[1:3])[0]
        return U16(v), 3
      
class I16(Number):

    def __repr__(self) -> str:
        return 'I16(%d)' % self.value
    
    def toBytes(self) -> bytes:
        return XType.I16.value + struct.pack('>h', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['I16', int]:
        if len(data) < 3:
            raise TypeError("data not enough")
        v = struct.unpack('>h', data[1:3])[0]
        return I16(v), 3


class U32(Number):

    def __repr__(self) -> str:
        return 'U32(%d)' % self.value
    
    def toBytes(self) -> bytes:
        return XType.U32.value + struct.pack('>I', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['U32', int]:
        if len(data) < 5:
            raise TypeError("data not enough")
        v = struct.unpack('>I', data[1:5])[0]
        return U32(v), 5
      
class I32(Number):

    def __repr__(self) -> str:
        return 'I32(%d)' % self.value
    
    def toBytes(self) -> bytes:
        return XType.I32.value + struct.pack('>h', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['I32', int]:
        if len(data) < 5:
            raise TypeError("data not enough")
        v = struct.unpack('>h', data[1:5])[0]
        return I32(v), 5

class U64(Number):

    def __repr__(self) -> str:
        return 'U64(%d)' % self.value
    
    def toBytes(self) -> bytes:
        return XType.U64.value + struct.pack('>Q', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['U64', int]:
        if len(data) < 9:
            raise TypeError("data not enough")
        v = struct.unpack('>Q', data[1:9])[0]
        return U64(v), 9
      
class I64(Number):

    def __repr__(self) -> str:
        return 'I64(%d)' % self.value
    
    def toBytes(self) -> bytes:
        return XType.I64.value + struct.pack('>q', self.value)
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['I64', int]:
        if len(data) < 9:
            raise TypeError("data not enough")
        v = struct.unpack('>q', data[1:9])[0]
        return I64(v), 9
    
    
  
class Bytes(Item):
    value: bytes

    def __init__(self, value) -> None:
        self.value = value

    def getLocalValue(self) -> bytes:
        return self.value
    
    def __repr__(self) -> str:
        return 'Bytes(%s)' % self.value
    
    def toBytes(self) -> bytes:
        return XType.Bytes.value + Number.of(len(self.value)).toBytes() + self.value

    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['Bytes', int]:
        off = 1
        number_item, used = Number.fromBytes(data[off:])
        off += used
        data_len = len(data)
        if data_len - off < number_item.value:
            raise TypeError('data not enough')  
        value = data[off:off + number_item.value]
        return Bytes(value), off + number_item.value


class Str(Item):
    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    def getLocalValue(self) -> str:
        return self.value

    def toBytes(self) -> bytes:
        return XType.Str.value + self.value.encode() + XType.End.value

    def __repr__(self) -> str:
        return 'Str("%s")' % self.value
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['Str', int]:
        # print('Str: from bytes', data)
        try:
            index = data.index(b'\x00')
        except ValueError as e:
            # print("invalid str", str(e))
            raise TypeError("data not enough")
        # print("last index", index)
        value = data[1:index].decode()
        # print("got str: ", value)
        return Str(value), index+1


# @dataclass
class List(Item):

    value: typing.List[Item]

    def __init__(self, items: typing.List[typing.Any]) -> None:
        self.value = [Item.of(item) for item in items]  

    def __repr__(self) -> str:
        return 'List%s' % str(self.value)
    
    def getLocalValue(self) -> typing.Any:
        return [item.localValue for item in self.value]
    
    def toBytes(self) -> bytes:
        items = [item.toBytes() for item in self.value]
        # items = map(lambda item: item.toBytes() , self.value)
        return XType.List.value + b''.join(items) + XType.End.value
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['List', int]:
        # print('List.fromBytes: ', data)
        value: typing.List[Item] = []
        off = 1
        while data[off] != 0:
            # print("try parse item: ", data[off:])
            item, used = Item.fromBytes(data[off:])
            # print("got item", item)
            value.append(item)
            # print("got List item: ", item)
            off += used
        
        return List(value), off+1



@dataclass
class Dict(Item):

    value: typing.Dict[str, Item]

    def __init__(self, items: typing.Dict[str, typing.Any]) -> None:
        # print("try create xdict of", items)
        self.value = {key: Item.of(value) for key, value in items.items()}  
        # print("init ok, ", self)

    def __repr__(self) -> str:
        return 'Dict%s' % self.value

    def getLocalValue(self) -> typing.Dict[str, typing.Any]:
        return { k: v.localValue for k, v in self.value.items()}

    def toBytes(self) -> bytes:
        # items = map(lambda k, v: Str(k).toBytes() + v.toBytes(), self.value.items())
        items = [Str(key).toBytes() + value.toBytes() for key, value in self.value.items()]
        return XType.Dict.value + b''.join(items) + XType.End.value
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['Dict', int]:
        # print("Dict.fromBytes...", data)
        # try:
        #     end_off = data.index(b'\x00')
        # except ValueError:
        #     # data not enough
        #     raise TypeError('invalid type')

        value: typing.Dict[str, Item] = {}
        off = 1
        name: str = None
        while data[off] != 0:
            item, used = Item.fromBytes(data[off:])
            # if item is None:
            #     raise TypeError('invalid type')
            # print('dict got', item)
            if name is None:
                # guard that item must be str
                name = item.value
            else:
                value[name] = item
                name = None
            off += used

        # print("ok, dict is", value)
        
        d =  Dict(value)
        # print("got dict: ", d)
        return d, off



global_call_id = 0
def next_call_id() -> int:
    global global_call_id
    global_call_id += 1
    if global_call_id > 255:
        global_call_id = 0
    return global_call_id



# @dataclass
class Call(Item):
    id: int # call id
    obj: int
    func: str
    params: List

    queue: Queue # FIXME: only for caller

    def __init__(self, id: int, obj: int, func: str, params: typing.Union[typing.List[typing.Any], List]):
        # print('init call', params)
        self.id = id
        self.obj = obj
        self.func = func

        if isinstance(params, List):
            self.params = params
        else:
            self.params = List(params)

        # print("params: ", self.params)
            
        # print("init queue")
        
        self.queue = Queue(maxsize=1)
        # print("queue init ok")

    
    def getLocalValue(self) -> typing.Any:
        return self.params.localValue

    def __repr__(self) -> str:
        return 'Call{#%d, obj%d.%s(%s)}' % (self.id, self.obj, self.func, self.params)

    @staticmethod
    def of(obj: int, func: str, params: typing.List[typing.Any]):
        return Call(next_call_id(), obj, func, params)

    def toBytes(self) -> bytes:
        return  XType.Call.value + Number.of(self.id).toBytes() + Number.of(self.obj).toBytes() + Str(self.func).toBytes() + self.params.toBytes()

    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple[typing.Optional['Call'], int]:
        # print("Call.fromBytes")
        off = 1
        call_id, used = Number.fromBytes(data[off:])
        off += used
        # print("call id: ", call_id)

        obj_id, used = Number.fromBytes(data[off:])
        off+= used
        # print("obj id", obj_id)

        func_name, used = Str.fromBytes(data[off:])
        off += used
        # print('func name', func_name)

        params, used = List.fromBytes(data[off:])
        off += used
        # print('params', params)

        # print("ok, create call")
        call = Call(call_id.value, obj_id.value, func_name.value, params)
        # print("parsed call", call)
        return call, off

# @dataclass
class Ret(Item):

    id: int # call id
    value: Item

    def __init__(self, id, value: Union[Item, typing.Any]) -> None:
        self.id = id
        self.value = Item.of(value)

    def __repr__(self) -> str:
        return 'Ret(#%d, %s)' % (self.id, self.value)

    def toBytes(self) -> bytes:
        return XType.Ret.value + Number.of(self.id).toBytes() + self.value.toBytes()

    
    def getLocalValue(self) -> typing.Any:
        return self.value.localValue
    
    @staticmethod
    def fromBytes(data: bytes) -> typing.Tuple['Ret', int]:

        off = 1
        call_id, used = Number.fromBytes(data[off:])
        off += used

        item, used = Item.fromBytes(data[off:])
        off += used

        return Ret(call_id.value, item), off


global_stream_id = 0
def next_stream_id() -> int:
    global global_stream_id
    global_stream_id += 1
    if global_stream_id > 255:
        global_stream_id = 0
    return global_stream_id


@dataclass
class StreamData(Item):
    id: int
    value: Optional[bytes]
    
    # stream_data + id + data
    def toBytes(self) -> bytes:
        return XType.StreamData.value + Number.of(self.id).toBytes() + (Bytes(self.value).toBytes() if self.value else XType.End.value)
    
    def __repr__(self) -> str:
        return 'StreamData(#%d, %dBytes)' % (self.id, len(self.value) if self.value else 0)
    
    def getLocalValue(self) -> typing.Any:
        return self
    
    def isEnd(self):
        return self.value is None
    
    @staticmethod
    def fromBytes(data: bytes) -> Tuple['StreamData', int]:
        off = 1
        id, used = Number.fromBytes(data[off:])
        off += used

        item, used =  Item.fromBytes(data[off:])
        off += used

        return StreamData(id.localValue, item.localValue), off



class Stream(Item):
    id: int
    name: str
    size: int # byte size
    offset: int # current position
    # direct_out: bool

    queue: Queue

    def __init__(self, name, size, id = 0) -> None:
        self.id = next_stream_id() if id == 0 else id
        self.name = name
        self.size = size
        # self.direct_out = direct_out
        self.offset = 0

        self.queue = Queue(maxsize=1)

    # def isSender(self):
    #     return self.direct_out
    
    # stream_info + id + list[name, size]
    def toBytes(self) -> bytes:
        return XType.Stream.value + Number.of(self.id).toBytes() + List([self.name, self.size]).toBytes()
    
    def __repr__(self) -> str:
        return 'StreamInfo(#%d, %s, %dBytes)' % (self.id, self.name, self.size)
    
    def getLocalValue(self) -> typing.Any:
        return self
    
    @staticmethod
    def fromBytes(data: bytes) -> Tuple['Stream', int]:
        off = 1
        id, used = Number.fromBytes(data[off:])
        off += used

        xlist, used = List.fromBytes(data[off:])
        off += used

        xlist = xlist.localValue
        # print('xlist in stream info: ', xlist)
        name = xlist[0]
        size = xlist[1]

        return  Stream(name, size, id.localValue), off

    @abstractmethod
    async def readChunks(self) -> Generator[bytes, None, None]:
        pass

    @abstractmethod
    async def writeChunk(self, data: Optional[bytes]) -> None:
        pass

@dataclass
class Err(Item):
    id: int
    msg: str

    def toBytes(self) -> bytes:
        return XType.Err.value + Number.of(self.id).toBytes() + Str(self.msg).toBytes()
    
    @staticmethod
    def fromBytes(data: bytes) -> Tuple[Item, int]:
        off = 1
        err_id, used = Number.fromBytes(data[off:]) 
        off += used

        msg, used = Str.fromBytes(data[off:])
        off += used

        return Err(err_id.localValue, msg.localValue), off

    def getLocalValue(self) -> typing.Any:
        return self

    