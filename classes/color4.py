from typing import Dict, Literal, Tuple, Union

from classes.sharedUtil import clampAll

class color4:
    r: float
    g: float
    b: float
    a: float

    def __str__(self):
        return '%d, %d, %d, %d(rgba)'.format(self.r, self.g, self.b, self.a)

    def __init__(self, r: float = 0, g: float = 0, b: float = 0, a: float = 1):
        (r, g, b, a) = clampAll(0, 1, r, g, b, a);
        self.r = r;
        self.g = g;
        self.b = b;
        self.a = a;

    @staticmethod
    def fromRGB(r: float, g: float, b: float):
        (r, g, b) = clampAll(0, 255, r, g, b);

        return color4(r / 255, g / 255, b / 255)

    def toRGBATuple(self) -> Tuple[int, int, int, int]:
        return (int(self.r * 255), int(self.g) * 255, int(self.b * 255), int(self.a * 255))

    def toRGBTuple(self) -> Tuple[int, int, int]:
        return (int(self.r * 255), int(self.g * 255), int(self.b * 255))
    def toRGBList(self) -> list[float]:
        return [self.r * 255, self.g * 255, self.b * 255]
    def toRGBDict(self) -> Dict[Union[Literal['r'], Literal['g'], Literal['b']], float]:
        return {
            'r': self.r * 255,
            'g': self.g * 255,
            'b': self.b * 255
        }

color4().toRGBList()