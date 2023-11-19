import struct
from io import FileIO
from pathlib import Path
from typing import Any, Callable, Optional, TypeVar

from .enums import ByteOrder, Format, OlString

T = TypeVar("T")


class BinaryReader(FileIO):
    DEFAULT_BYTEORDER = ByteOrder.STANDARD

    def __init__(
        self,
        path: str | Path,
        order: ByteOrder = DEFAULT_BYTEORDER
    ):
        super().__init__(path, mode="rb")
        self.path = Path(path)
        self.order = order

    @staticmethod
    def unpacker(fmt: Format) -> Callable[[Callable[..., T]], Callable[..., T]]:
        def decorator(_: Callable):
            def wrapper(self: "BinaryReader", order: Optional[ByteOrder] = None):
                return self.unpack(fmt, order)[0]
            return wrapper
        return decorator

    @unpacker(Format.I8)
    def i8(self) -> int:
        """`signed byte` `1 byte`"""
        ...

    @unpacker(Format.I16)
    def i16(self) -> int:
        """`signed short` `word` `2 bytes`"""
        ...

    @unpacker(Format.I32)
    def i32(self) -> int:
        """`signed integer` `double word` `4 bytes`"""
        ...

    @unpacker(Format.I64)
    def i64(self) -> int:
        """`signed long` `quad word` `8 bytes`"""
        ...

    @unpacker(Format.U8)
    def u8(self) -> int:
        """`unsigned byte` `1 byte`"""
        ...

    @unpacker(Format.U16)
    def u16(self) -> int:
        """`unsigned short` `word` `2 bytes`"""
        ...

    @unpacker(Format.U32)
    def u32(self) -> int:
        """`unsigned integer` `double word` `4 bytes`"""
        ...

    @unpacker(Format.U64)
    def u64(self) -> int:
        """`unsigned long` `quad word` `8 bytes`"""
        ...

    @unpacker(Format.F16)
    def f16(self) -> float:
        """`float` `half-precision` `2 bytes`"""
        ...

    @unpacker(Format.F32)
    def f32(self) -> float:
        """`float` `single-precision` `4 bytes`"""
        ...

    @unpacker(Format.F64)
    def f64(self) -> float:
        """`float` `double-precision` `8 bytes`"""
        ...

    def mcsastring(self) -> bytes:
        """mcsa file string"""

        size = self.u16(ByteOrder.LITTLE)
        return bytes(
            self.i8()
            for _ in range(size)
        )

    def olstring(self, size: int = OlString.SIZE) -> bytes:
        """ol file string"""

        return bytes(
            char ^ OlString.XOR
            for char in self.read(size)
            if char != OlString.NULL
        )

    def unpack(self, fmt: Format, order: Optional[ByteOrder] = None) -> Any:
        order = order or self.order
        size = struct.calcsize(str(fmt))
        data = self.read(size)
        return struct.unpack(f"{order}{fmt}", data)
