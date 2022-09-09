from typing import Tuple

class udim2:
    scaleX: int
    offsetX: int
    scaleY: int
    offsetY: int
    def __init__(self, sx: int, ox: int, sy: int, oy: int):
        self.scaleX = int(sx);
        self.offsetX = int(ox);
        self.scaleY = int(sy);
        self.offsetY = int(oy);

    def toScale(self) -> Tuple[int, int]:
        return (self.scaleX, self.scaleY);

    def toOffset(self) -> Tuple[int, int]:
        return (self.offsetX, self.offsetY);

    @staticmethod
    def fromScale(sx: int, sy: int):
        return udim2(sx, 0, sy, 0);

    @staticmethod
    def fromOffset(ox: int, oy: int):
        return udim2(0, ox, 0, oy);