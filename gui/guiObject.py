from classes.color4 import color4
from client.renderer import gameLoop
from gui.guiDefaultProperties import LoadDefaultGuiProperties
from gui.instance import instance
from classes.udim2 import udim2
from pygame import Vector2
import pygame
import classes.mathf as mathf

class guiObject(instance):
    position: udim2
    size: udim2

    absolutePosition: pygame.Vector2
    absoluteSize: pygame.Vector2
    
    rotation: float
    
    color: color4
    
    backgroundColor: color4
    backgroundTransparency: float

    borderWidth: int
    borderColor: color4

    dropShadowRadius: float
    dropShadowColor: color4

    def __init__(self):
        super()

        self.__internal = {
            
        }

        LoadDefaultGuiProperties('guiObject', self);

    def getSizeAndPositionFromUdim2(self, positionUdim: udim2, sizeUdim: udim2):
        if self.parent and isinstance(self.parent, instance):
            pPos = self.parent.absolutePosition
            pSize = self.parent.absoluteSize

            fP = positionUdim.toScale()
            fpO = positionUdim.toOffset()
            fS = sizeUdim.toScale()
            fsO = sizeUdim.toOffset()

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)
            
            return (position, size)
        
        else:
            container = gameLoop.getRenderer().resolution

            pPos = Vector2(0, 0)
            pSize = Vector2(container.x, container.y)

            fP = positionUdim.toScale()
            fpO = positionUdim.toOffset()
            fS = sizeUdim.toScale()
            fsO = sizeUdim.toOffset()

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)

            return (position, size)

    def update(self, dt: float):

        screen = gameLoop.getRenderer().screen

        (bgPosition, bgSize) = self.getSizeAndPositionFromUdim2(self.position, self.size)

        backgroundRect = pygame.Rect(bgPosition.x, bgPosition.y, bgSize.x, bgSize.y)

        backSurf = pygame.Surface(backgroundRect.size)

        backSurf.fill(self.backgroundColor.toRGBTuple())

        borderRect = pygame.Rect(
            bgPosition.x - self.borderWidth, 
            bgPosition.y - self.borderWidth, 
            bgSize.x + self.borderWidth, bgSize.y + self.borderWidth)

        borderSurf = pygame.Surface(borderRect.size)

        borderSurf.fill(self.borderColor.toRGBTuple())

        backSurf.set_alpha(int((1 - self.backgroundTransparency) * 255))

        #blit borderSurf before backSurf, so it is below

        #currently looks like a dropshadow, offset it?

        screen.blit(borderSurf, borderRect.center)

        screen.blit(backSurf, backgroundRect.center)

        for child in self.children:
            child.update(dt)