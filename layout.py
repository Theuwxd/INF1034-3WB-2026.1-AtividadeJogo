import pygame
import sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Hello world')
clock = pygame.time.Clock()

#fonte do texto
fonte = pygame.font.Font('texto.ttf', 10)

# imagem de coraçao do lado da vida
heart = pygame.image.load('coracao.png')


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (102, 51, 0), (20, 20, 200, 70), border_radius=20)
    screen.blit(heart, (25, 40))

    #Coloquei as vidas separadas, pq pensei em quando a gnt perder uma vida tem como diminuir tirando uma delas
    #mas isso foi ideia inical, qualquer coisa a gnt muda
    pygame.draw.rect(screen, (204, 0, 0), (54, 45, 50, 20), border_radius=20)
    pygame.draw.rect(screen, (204, 0, 0), (54, 45, 100, 20), border_radius=20)
    pygame.draw.rect(screen, (204, 0, 0), (54, 45, 150, 20), border_radius=20)

    #colocar os textos 
    texto1 = fonte.render('A - esquerda', True, (255, 255, 255))
    texto2 = fonte.render('D - direita', True, (255, 255, 255))
    texto3 = fonte.render('w - cima', True, (255, 255, 255))
    texto4 = fonte.render('S - baixo', True, (255, 255, 255))
    #botei o espaco para dash mas n sei qual vms usar, ent da pra trocar 
    texto5 = fonte.render('SPACE - dash', True, (255, 255, 255))


    screen.blit(texto1, (25, 420))
    screen.blit(texto2, (25, 440))
    screen.blit(texto3, (25, 460))
    screen.blit(texto4, (25, 480))
    screen.blit(texto5, (25, 500))






    pygame.display.update()
