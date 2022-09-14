import threading
from typing import Any


def clamp(x: float, minV: float, maxV: float):
    return x < minV and minV or x > maxV and maxV or x;

def clampAll(minV: float, maxV: float, *nums: float):
    return (clamp(val, minV, maxV) for val in nums)

def rawGet(obj: object, prop: str): return object.__getattribute__(obj, prop);

def rawSet(obj: object, prop: str, value: Any): return object.__setattr__(obj, prop, value);

def createThread(func: Any):

    thr = threading.Thread(target=func, daemon=True);
    thr.start()

    return thr;