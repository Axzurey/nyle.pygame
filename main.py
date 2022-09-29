from classes.color4 import color4
from classes.udim2 import udim2
from client.renderer import renderer, gameLoop
import pygame

from gui.guiObject import guiObject

mainRenderer = renderer(pygame.Vector2(1000, 700), 0, color4(1, 1, 1))

gameLoop.setRenderer(mainRenderer)

frame = guiObject()

frame.backgroundColor = color4.fromRGBA(0, 255, 255, 200)

frame.size = udim2(260, 0, 100, 0)

frame.position = udim2(0, .2, 0, .3)

mainRenderer.setParent(frame, mainRenderer)

mainRenderer.start()

