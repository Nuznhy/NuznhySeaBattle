CELL_SHIP_UNIT = 'D'
CELL_SHIP_DAMAGED = 'x'
CELL_SHIP_DESTROYED = '#'
CELL_SPACE_EMPTY = '.'
CELL_SPACE_HIT = '*'
CELL_SPACE_BUFFER = '^'

OFFSETS = (-1, 0, 1)


class AxisDirection(Enum):
    X = 0
    Y = 1


class HitStatus(Enum):
    UNKNOWN = 0
    MISS = 1
    MISS_REPEATED = 2
    DAMAGED = 3
    DESTROYED = 4