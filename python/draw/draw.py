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
    lines = []
    points = []
    draw = False
    WIN.fill(colors[0])
    while run:
        clock.tick(150)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw = not draw
                if draw == False:
                    lines.append(points)
                    points = []
            if draw == True and event.type == pygame.MOUSEMOTION:
                points.append(event.pos)
                if len(lines) > 0:
                    lines.remove(lines[-1])
                lines.append(points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    WIN.fill(colors[0])
                    lines = []
                if event.key == pygame.K_LEFT:
                    if len(lines) > 0:
                        lines.remove(lines[-1])
            for line in lines:
                for i in range(len(line)-1):
                    if i > 0:
                        pygame.draw.line(WIN, colors[1], line[i], line[i+1], 3)
                        
main()