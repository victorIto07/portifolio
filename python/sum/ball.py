import py_compile
from random import randint, random
import pygame


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_vel = random() * 3 if random()>.5 else random() * -3
        self.y_vel = random() * 3 if random()>.5 else random() * -3
        self.w = randint(2, 5)

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self, WIN):
        pygame.draw.circle(WIN, '#ffffff', (self.x, self.y), self.w)
