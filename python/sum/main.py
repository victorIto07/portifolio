import pygame
from random import randint
from aaline import aaline
from ball import Ball
from math import sqrt

from translate import translate

pygame.init()

WID, HEI = 900, 900

WIN = pygame.display.set_mode((WID, HEI))
balls = []

for i in range(150):
    balls.append(Ball(randint(0, WID), randint(0, HEI)))


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(90)
        WIN.fill('#000000')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for ball in balls:
            if ball.x < 0 or ball.x > WID:
                ball.x_vel *= -1
            if ball.y < 0 or ball.y > HEI:
                ball.y_vel *= -1
            ball.update()
            for other in balls:
                if other != ball:
                    x_dif = ball.x - other.x if ball.x > other.x else other.x - ball.x
                    y_dif = ball.y - other.y if ball.y > other.y else other.y - ball.y
                    dif = (x_dif**2)+(y_dif**2)
                    if x_dif <= 150 and y_dif <= 150:
                        a = translate(sqrt(dif), 10, 150, 255, 0)
                        a = 255 if a > 255 else (0 if a < 0 else a)
                        aaline(WIN, (4, 217, 255, a),
                               (ball.x, ball.y), (other.x, other.y))
            ball.draw(WIN)
        pygame.display.update()
    pygame.quit()


main()
