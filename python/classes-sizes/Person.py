from pygame import *
from Body import Body
from Head import Head
from Colors import Colors

colors = Colors()


class Person:

    def __init__(self, x, y, x_vel, y_vel, tamanho):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.tamanho = tamanho
        self.define_corpo()

    def define_corpo(self):
        raio_cabeca = int(self.tamanho*.25)
        tamanho_corpo = self.tamanho*.4*3
        largura_corpo = self.tamanho*.5

        self.cabeca = Head(self.x, self.y, raio_cabeca)
        self.corpo = Body(self.x-self.cabeca.r, self.y +
                          self.cabeca.r, tamanho_corpo, largura_corpo)

    def update(self):
        self.corpo.update(self)
        self.cabeca.update(self)

    def draw(self, WIN):
        self.update()
        self.corpo.draw(WIN)
        self.cabeca.draw(WIN)
