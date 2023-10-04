from random import random
import pygame

from colors import Colors

class Point:
    colors = Colors()
    def __init__(self,x,y,randomColor=True):
        self.c = self.colors.random() if randomColor else self.colors.red
        self.x = x
        self.x_vel = random() * 3 if random()>.5 else random() * -3
        self.y = y
        self.y_vel = random() * 3 if random()>.5 else random() * -3

    def update(self,dt):
        self.x += self.x_vel*dt
        self.y += self.y_vel*dt

    def draw(self,WIN):
        pygame.draw.circle(WIN, self.c,(self.x,self.y),1)