import pygame
import sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Hello world')
clock = pygame.time.Clock()

movimento = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    keys = pygame.key.get_pressed()
    movimento = False

    if keys[pygame.K_RIGHT]:
        #colocar a parte das imagens
        movimento = True
    elif keys[pygame.K_LEFT]:
        #colocar a parte das imagens
        movimento = True
    elif keys[pygame.K_UP]:
        #colocar a parte das imagens
        movimento = True
    elif keys[pygame.K_DOWN]:
        #colocar a parte das imagens
        movimento = True










    pygame.display.update()