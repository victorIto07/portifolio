from pygame import *
from colors import Colors
from mapp import v_map
class Cell:
    def __init__(self, pos,i,j, v, config):
        self.i = i
        self.j = j
        self.pos = pos
        self.v = v
        self.w = config["width"]/config["gridCols"]
        self.h = config["height"]/config["gridRows"]
        self.surf = Surface((self.w,self.h))
        self.surf.fill(Colors.red)
        self.rect = self.surf.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.alpha_set = False

    def set_alpha(self, v):
        self.surf.set_alpha(v)
        self.v = v
        self.alpha_set = True

    def draw(self,WIN:Surface):
        WIN.blit(self.surf, self.rect)