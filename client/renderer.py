from __future__ import annotations

import time
from typing import Union
import pygame
from classes.color4 import color4
from classes.sharedUtil import rawSet

from gui.instance import instance

pygame.init()

class renderer:
    rendererClosing: bool
    lastUpdate: float
    lastEvents: list[pygame.event.Event]

    children: list[instance]

    def __init__(self, resolution: pygame.Vector2, framerate: int, backgroundColor: color4):
        self.rendererClosing = False;
        self.lastUpdate = time.time()
        self.lastEvents = []
        self.children = []


        self.backgroundColor = backgroundColor;

        self.framerate = framerate;

        self.resolution = resolution;

        self.screen = pygame.display.set_mode((resolution.x, resolution.y))

    @staticmethod
    def setParent(inst: instance, to: Union[renderer, instance, None]):
        if to:
            if inst in to.children: return;
            rawSet(inst, 'parent', to);
            to.children.append(inst);
        else:
            if inst.parent:
                inst.parent.children.remove(inst);
                rawSet(inst, 'parent', None);

    def start(self):
        clock = pygame.time.Clock()

        while (not self.rendererClosing):

            now = time.time()

            dt = now - self.lastUpdate;

            self.lastUpdate = now;

            events = pygame.event.get()
            self.lastEvents = events;

            for event in events:
                if event.type == pygame.QUIT:
                    self.rendererClosing = True;

            self.screen.fill(self.backgroundColor.toRGBTuple())

            for child in self.children:
                child.update(dt)

            pygame.display.flip()

            clock.tick(self.framerate);


class __gameLoop:
    def setRenderer(self, renderer: renderer):
        self.renderer = renderer;

    def getRenderer(self) -> renderer:
        return self.renderer


gameLoop = __gameLoop();