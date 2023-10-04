import pygame
from random import random


def translate(lv, l1, l2, r1, r2):
    if lv > l2:
        lv = l2
    elif lv < l1:
        lv = l1
    l_off = l2-l1
    r_off = r2-r1
    pl = (lv-l1)/l_off
    pr = r_off * pl
    rv = pr + r1
    return rv


class Colors:
    red = (255, 50, 50)
    green = (50, 255, 50)
    blue = (50, 50, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)


class Raycast:

    width, height = 900, 900
    CLOCK = pygame.time.Clock()
    colors = Colors()
    grid = []
    light_radius = 50

    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((self.width, self.height))
        self.ball = [random()*self.width, random() *
                     self.height, random()*5, random()*5]
        self.create_grid()

    def create_grid(self):
        self.grid.clear()
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            self.grid.append(row)

    def run(self):
        self.running = True
        while self.running:
            # self.CLOCK.tick(60)
            self.get_events()
            self.update()
            self.draw()
            pygame.display.update()
        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.update_ball()
        self.update_pixels()

    def update_ball(self):
        if self.ball[0] > self.width or self.ball[0] < 0:
            self.ball[2] *= -1
        if self.ball[1] > self.height or self.ball[1] < 0:
            self.ball[3] *= -1
        self.ball[0] += self.ball[2]
        self.ball[1] += self.ball[3]

    def update_pixels(self):
        pos = [int(self.ball[0]), int(self.ball[1])]
        max_w = pos[0]+self.light_radius+1
        if max_w >= self.width:
            max_w = self.width - 1
        max_h = pos[1]+self.light_radius+1
        if max_h >= self.height:
            max_h = self.height - 1
        for y in range(pos[1]-self.light_radius, max_h):
            for x in range(pos[0]-self.light_radius, max_w):
                d = (((pos[0]-x)**2)+((pos[1]-y)**2))**.5
                c = translate(d, 1, self.light_radius, 200, 0)
                self.grid[y][x] = c

    def draw(self):
        self.draw_background()
        self.draw_pixels()

    def draw_background(self):
        self.WIN.fill(self.colors.black)

    def draw_pixels(self):
        pos = [int(self.ball[0]), int(self.ball[1])]
        pixels = pygame.PixelArray(self.WIN)
        max_w = pos[0]+self.light_radius+1
        if max_w >= self.width:
            max_w = self.width - 1
        max_h = pos[1]+self.light_radius+1
        if max_h >= self.height:
            max_h = self.height - 1
        for y in range(pos[1]-self.light_radius, max_h):
            for x in range(pos[0]-self.light_radius, max_w):
                c = self.grid[y][x]
                pixels[x, y] = (c, c, c)

        pixels.close()


Raycast().run()
