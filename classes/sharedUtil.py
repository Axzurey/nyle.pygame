import threading
import pygame
import cv2
import numpy
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

    return thr

def create_neon(surf: pygame.Surface):
    surf_alpha = surf.convert_alpha()
    rgb = pygame.surfarray.array3d(surf_alpha) # type: ignore
    alpha = pygame.surfarray.array_alpha(surf_alpha).reshape((*rgb.shape[:2], 1)) # type: ignore
    image = numpy.concatenate((rgb, alpha), 2) # type: ignore
    cv2.GaussianBlur(image, ksize=(9, 9), sigmaX=10, sigmaY=10, dst=image) # type: ignore
    cv2.blur(image, ksize=(5, 5), dst=image) # type: ignore
    bloom_surf = pygame.image.frombuffer(image.flatten(), image.shape[1::-1], 'RGBA') # type: ignore
    return bloom_surf