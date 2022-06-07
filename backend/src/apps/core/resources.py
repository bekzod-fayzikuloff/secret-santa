import enum


class BoxState(str, enum.Enum):
    OPEN = "OP"
    CLOSE = "CL"
    DURING = "DU"
