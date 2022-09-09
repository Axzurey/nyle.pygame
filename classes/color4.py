import math

from classes.sharedUtil import clampAll

class color4:
    r: float
    g: float
    b: float
    a: float

    def __str__(self):
        return '%d, %d, %d, %d(rgba)'.format(self.r, self.g, self.b, self.a)

    def __init__(self, r: float = 0, g: float = 0, b: float = 0, a: float = 1):
        (r, g, b, a) = clampAll((r, g, b, a), 0, 1);
        self.r = r;
        self.g = g;
        self.b = b;
        self.a = a;

    @staticmethod
    def fromRGB(r: float, g: float, b: float):
        return r