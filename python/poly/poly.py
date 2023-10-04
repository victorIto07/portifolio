import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('rain')
FONT = pygame.font.SysFont("comicsans", 16)

colors = [(0, 0, 0),
          (255, 255, 255),
          (209, 17, 65),
          (0, 177, 89),
          (0, 174, 219),
          (243, 119, 53),
          (255, 196, 37)
          ]

def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors[0])
    forms = []
    points = []
    draw = False
    while run:
        clock.tick(75)
        pygame.display.update()
        WIN.fill(colors[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    forms = []
                    WIN.fill(colors[0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw = not draw
                if draw == False:
                    forms.append(points)
                    points = []
            if draw and event.type == pygame.MOUSEMOTION:
                points.append(event.pos)
                if len(forms) > 0:
                    forms.remove(forms[-1])
                forms.append(points)
        for poly in forms:
            if len(poly) > 1:
                pygame.draw.polygon(WIN, colors[1], poly, 1)

main()