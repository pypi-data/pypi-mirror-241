from typing import Protocol


class PPoint2D(Protocol):
    x: float
    y: float


class PSize2D(Protocol):
    width: float
    height: float


class PRect(Protocol):
    x: float
    y: float
    width: float
    height: float
