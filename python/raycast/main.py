from player import Player
from map import Grid

import pygame
pygame.init()


class Raycast:

    FONT = pygame.font.SysFont('arial', 24)
    CLOCK = pygame.time.Clock()
    show_grid = False
    FPS = 60

    width, height = 500, 500

    grid = Grid().map

    def __init__(self):
        self.WIN = pygame.display.set_mode((self.width, self.height))
        self.player = Player(self.width/2, self.height/2, (self.width, self.height))
        self.run()

    def run(self):
        self.running = True
        while self.running:
            self.CLOCK.tick(self.FPS)
            self.read_events()
            self.draw()
            pygame.display.update()
        pygame.quit()

    def read_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.show_grid = not self.show_grid
                if event.key == pygame.K_UP:
                    self.player.depth_view += 1
                if event.key == pygame.K_DOWN:
                    self.player.depth_view -= 1

        k = pygame.key.get_pressed()
        if k[pygame.K_w]:
            self.player.body.y += -2
        if k[pygame.K_d]:
            self.player.body.x += 2
        if k[pygame.K_s]:
            self.player.body.y += 2
        if k[pygame.K_a]:
            self.player.body.x += -2
        if k[pygame.K_LEFT]:
            self.player.angle = (self.player.angle-2) % 360
        if k[pygame.K_RIGHT]:
            self.player.angle = (self.player.angle + 2) % 360
        if k[pygame.K_1]:
            self.player.angle = 0
        if k[pygame.K_2]:
            self.player.angle = 90
        if k[pygame.K_3]:
            self.player.angle = 180
        if k[pygame.K_4]:
            self.player.angle = 270
            

    def draw(self):
        self.draw_background()
        self.draw_grid()
        self.draw_player()
        self.draw_fps()
        self.draw_player_angle()

    def draw_background(self):
        self.WIN.fill('#000000')  # black

    def draw_grid(self):
        cel_height = int(self.height/len(self.grid))
        for j in range(len(self.grid)):
            row = self.grid[j]
            cel_width = int(self.width/len(row))
            for i in range(len(row)):
                c = self.grid[j][i]
                x, y = i * cel_width, j * cel_height
                if c == 1:
                    pygame.draw.rect(self.WIN, '#ff6666',
                                     (x, y, cel_width, cel_height))
                if self.show_grid:
                    pygame.draw.rect(self.WIN, '#ffffff',
                                     (x, y, cel_width, cel_height), 1)

    def draw_fps(self):
        self.WIN.blit(self.FONT.render(
            str(int(self.CLOCK.get_fps())), False, '#55ff55'), (0, 0))
        
    def draw_player_angle(self):
        self.WIN.blit(self.FONT.render(
            str(self.player.angle), False, '#5555ff'), (0, 27))

    def draw_player(self):
        self.player.draw(self.WIN, self.grid)


Raycast()
