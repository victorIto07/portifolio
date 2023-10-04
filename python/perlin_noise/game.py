import sys
sys.setrecursionlimit(100000)

from random import randint
from pygame import *
from cell import Cell
from colors import Colors

from configs import Configs

class Game:
    config:Configs.props
    run:bool = True
    grid = []

    def __init__(self,config):
        self.config = config
        self.WIN = display.set_mode((self.config["width"], self.config["height"]))
    
    def start(self):
        self.init_grid()
        while self.run:
            self.read_events()

        quit()

    def read_events(self):
        for e in event.get():
            if e.type == QUIT:
                self.run = False
            if e.type == KEYDOWN:
                if e.key == K_DOWN:
                    self.init_grid()

    def init_grid(self):
        self.grid.clear()
        self.cell_w,self.cell_h = self.config["width"]/self.config["gridCols"],self.config["height"]/self.config["gridRows"]
        for i in range(self.config["gridRows"]+1):
            self.grid.append([])
            for j in range(self.config["gridCols"]+1):
                self.grid[i].append(Cell((j*self.cell_w, i*self.cell_h),i,j,0, self.config))
        self.perlin_noise()
        self.WIN.fill(Colors.white)
        self.draw_cells()
        self.draw_grid()
        display.update()

    def perlin_noise(self):
        i = (self.config["gridRows"]//2)
        j = (self.config["gridCols"]//2)
        c = self.grid[i][j]
        c.set_alpha(randint(0,255))
        self.set_neighbors_alpha(c)

    def set_neighbors_alpha(self, cell):
        if cell.i > 0 and cell.j > 0:
            nw = self.grid[cell.i-1][cell.j-1]
            if not nw.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                nw.set_alpha(a)
                self.set_neighbors_alpha(nw)
        if cell.i > 0:
            n = self.grid[cell.i-1][cell.j]
            if not n.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                n.set_alpha(a)
                self.set_neighbors_alpha(n)
        if cell.i > 0 and cell.j < self.config["gridCols"]:
            ne = self.grid[cell.i-1][cell.j+1]
            if not ne.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                ne.set_alpha(a)
                self.set_neighbors_alpha(ne)
        if cell.j > 0:
            w = self.grid[cell.i][cell.j-1]
            if not w.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                w.set_alpha(a)
                self.set_neighbors_alpha(w)
        if cell.j < self.config["gridCols"]:
            e = self.grid[cell.i][cell.j+1]
            if not e.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                e.set_alpha(a)
                self.set_neighbors_alpha(e)
        if cell.i < self.config["gridRows"] and cell.j > 0:
            sw = self.grid[cell.i+1][cell.j-1]
            if not sw.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                sw.set_alpha(a)
                self.set_neighbors_alpha(sw)
        if cell.i < self.config["gridRows"]:
            s = self.grid[cell.i+1][cell.j]
            if not s.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                s.set_alpha(a)
                self.set_neighbors_alpha(s)
        if cell.i < self.config["gridRows"] and cell.j < self.config["gridCols"]:
            se = self.grid[cell.i+1][cell.j+1]
            if not se.alpha_set:
                a = randint(cell.v-20, cell.v+20)
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0
                se.set_alpha(a)
                self.set_neighbors_alpha(se)
        
    def draw_cells(self):
        for i in range(self.config["gridRows"]+1):
            for j in range(self.config["gridCols"]+1):
                self.grid[i][j].draw(self.WIN)

    def draw_grid(self):
        for i in range(1,self.config["gridRows"]):
            for j in range(1,self.config["gridCols"]):
                draw.line(self.WIN, Colors.black,(self.cell_w*j, 0), (self.cell_w*j, self.config["height"]))
                draw.line(self.WIN, Colors.black,(0, self.cell_h*i), (self.config["width"], self.cell_h*i))