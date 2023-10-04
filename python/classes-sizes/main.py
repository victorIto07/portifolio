import pygame

from Colors import Colors
from Person import Person

WIDTH,HEIGHT = 960,1000

JANELA = pygame.display.set_mode((WIDTH, HEIGHT))
colors = Colors()

pessoa = Person(WIDTH/2,HEIGHT/2,1,0,170)
pessoa2 = Person(WIDTH/2-120,HEIGHT/3, -1, .5, 90)
pessoa3 = Person(WIDTH/2-120,HEIGHT/2+200, 1.5, -.5, 120)

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        JANELA.fill(colors.white)
        pessoa.draw(JANELA)
        pessoa2.draw(JANELA)
        pessoa3.draw(JANELA)
        pygame.display.update()
    pygame.quit()
main()