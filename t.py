import pygame
import numpy
import cv2

pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

def create_neon(surf): # type: ignore
    surf_alpha = surf.convert_alpha() # type: ignore
    rgb = pygame.surfarray.array3d(surf_alpha) # type: ignore
    alpha = pygame.surfarray.array_alpha(surf_alpha).reshape((*rgb.shape[:2], 1)) # type: ignore
    image = numpy.concatenate((rgb, alpha), 2) # type: ignore
    cv2.GaussianBlur(image, ksize=(9, 9), sigmaX=10, sigmaY=10, dst=image) # type: ignore
    cv2.blur(image, ksize=(5, 5), dst=image) # type: ignore
    bloom_surf = pygame.image.frombuffer(image.flatten(), image.shape[1::-1], 'RGBA') # type: ignore
    return bloom_surf

image = pygame.Surface((1280, 720), pygame.SRCALPHA)
pygame.draw.rect(image, (255, 128, 128), (50, 10, 80, 80))
neon_image = create_neon(image)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.fill((127, 127, 127))
    window.blit(neon_image, (0, 0), special_flags = pygame.BLEND_PREMULTIPLIED)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()