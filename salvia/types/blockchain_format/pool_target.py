from dataclasses import dataclass

from salvia.types.blockchain_format.sized_bytes import bytes32
from salvia.util.ints import uint32
from salvia.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class PoolTarget(Streamable):
    puzzle_hash: bytes32
    max_height: uint32  # A max height of 0 means it is valid forever
