import pygame

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.c = '#ff0000'
    
    def draw(self, WIN):
        pygame.draw.circle(WIN, self.c, (self.x,self.y), 3)