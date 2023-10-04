from pygame import *
from Colors import Colors

colors = Colors()


class Body:
    def __init__(self, x, y,  tamanho,largura):
        self.x = x
        self.y = y
        self.altura = tamanho
        self.largura = largura

    def update(self,pai):
        self.x += pai.x_vel
        self.y += pai.y_vel

    def draw(self, WIN):
        rect = Rect(self.x, self.y, self.largura, self.altura)
        draw.rect(WIN, colors.blue, rect, int(self.largura/2)+1)
