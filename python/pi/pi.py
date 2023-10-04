import pygame
import math
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('VIZUALIZAÇÃO PI')
ICON = pygame.image.load('C:\projects\py\pi\pi.png')
pygame.display.set_icon(ICON)
FONT = pygame.font.SysFont("comicsans", 16)

points_in = points_out = 0

WHITE = (255, 255, 255)
BLUE = (140, 189, 255)
BLACK = (0, 0, 0)
RED = (228, 69, 90)
GREY = (20, 20, 20)
PURPLE = (154,140,199)


class Point:

    def __init__(self, x, y, inside):
        self.x = x
        self.y = y
        self.inside = inside

    def draw(self):
        if self.inside:
            color = WHITE
        else:
            color = BLUE
        pygame.draw.circle(WIN, color, (self.x, self.y), 1)


def render_points(n):
    points = []
    points_in = points_out = 0
    for _ in range(n):
        x, y = randint(0, 800), randint(0, 800)
        p = Point(x, y, (math.sqrt(x**2+y**2) <= 800))
        if math.sqrt(p.x**2+p.y**2) <= 800:
            p.inside = True
            points_in += 1
        else:
            p.inside = False
            points_out += 1
        points.append(p)
    return points, points_in, points_out


def line():
    points = []
    for x in range(WIDTH, 0, -1):
        y = math.sqrt(WIDTH**2 - x**2)
        points.append((x, y))
    return points


def Main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(BLACK)

    while run:
        clock.tick(75)
        pygame.draw.lines(WIN, WHITE, False, line())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    points, points_in, points_out = render_points(20000)
                    dentro = FONT.render(f'Inside: {points_in}', 1, WHITE)
                    fora = FONT.render(f'Outside: {points_out}', 1, BLUE)
                    pi = FONT.render(f'PI: 3.1415', 1, RED)
                    pi_aprox = FONT.render(
                        f'PI_APROX: {round(4*points_in/(points_in+points_out), 4)}', 1, RED)
                    if (round(4*points_in/(points_in+points_out), 4) <= 3.1415):
                        percent = round(4*points_in/(points_in+points_out)/3.1415*100, 2)
                    else:
                        percent = round(100-((4*points_in/(points_in+points_out)/3.1415*100)-100), 2)
                    pi_percent = FONT.render(
                        f'{percent}% Right', 1, PURPLE)
                    WIN.fill(BLACK)
                    for point in points:
                        point.draw()
                    pygame.draw.rect(
                        WIN, GREY, (0, 0, pi_aprox.get_width()*2+pi_percent.get_width()+20, dentro.get_height()*2+25))
                    WIN.blit(dentro, (10, dentro.get_height()/2))
                    WIN.blit(fora, (10, fora.get_height()+5))
                    WIN.blit(pi, (dentro.get_width()+25, dentro.get_height()/2))
                    WIN.blit(pi_aprox, (dentro.get_width() +
                             25, fora.get_height()+5))
                    WIN.blit(pi_percent, (dentro.get_width() +35 + pi_aprox.get_width(), fora.get_height()-fora.get_height()/2+5))

        pygame.display.update()

    pygame.quit()


Main()
