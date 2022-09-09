from typing import List, Tuple


def clamp(x: float, minV: float, maxV: float):
    return x < minV and minV or x > maxV and maxV or x;

def clampAll(nums: Tuple[float], minV: float, maxV: float):
    out = ()
    for f in nums:
        out += (clamp(f), minV, maxV)

    return out;