from pygame import *
import sys

init()

screen = display.set_mode((1000, 600))
display.set_caption('Hello world')
clock = time.Clock()

fonte = font.Font('texto.ttf', 10)

sixseven = image.load('67zin.png')
boss_vida_max = 100
boss_vida = 100



def boss_tomar_dano(dano):
    global boss_vida # esse global serve para avisar pro codigo q e pra ele usar a vida do boss q esta fora dessa funçao
    boss_vida -= dano
    if boss_vida < 0:
        boss_vida = 0

while True:
    for evento in event.get():
        if evento.type == QUIT:
            quit()
            sys.exit()

        
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE:
                boss_tomar_dano(1)

    clock.tick(60)
    dt = clock.get_time()
    

    screen.fill((0, 0, 0))
    draw.rect(screen, (102, 51, 0), (780, 20, 200, 70), border_radius=20)

    sixseven = transform.scale(sixseven, (100, 50))

    barra_largura_atual = boss_vida * 1.5

    draw.rect(screen, (0, 0, 0), (790, 45, 150, 20), border_radius=20)

    if barra_largura_atual > 0:
        draw.rect(screen, (204, 0, 0), (790, 45, barra_largura_atual, 20), border_radius=20)


    screen.blit(sixseven, (940, 32), (33, 0, 200, 200))

    display.update()