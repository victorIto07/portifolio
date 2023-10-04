import pygame
from random import randint

pygame.init()
WIDTH, HEIGTH = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGTH))

FONT = pygame.font.SysFont("calibri", 15)

points = []
colors = [(0, 0, 0), (255, 255, 255)]


class Point():

    def __init__(self, x, y, x_vel, y_vel, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.line = []

    def draw(self):
        if self.x >= WIDTH or self.x <= 0:
            self.x_vel = self.x_vel * -1 
        if self.y >= HEIGTH and self.y < HEIGTH + 50:
            self.y_vel = self.y_vel * -1
        self.x += self.x_vel
        self.y_vel += 1.5
        if self.y_vel > 50:
            self.y_vel = 50
        self.y += self.y_vel
        self.remove()
        if len(self.line)>5:
            self.line.remove(self.line[0])
        self.line.append((self.x, self.y))
        pygame.draw.circle(WIN, self.color, (self.x, self.y), 5)
        if len(self.line)>1:
            pygame.draw.lines(WIN, self.color, False, self.line)

    def remove(self):
        if self.y > HEIGTH + 50:
            points.remove(self)

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                points.clear()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                points.append(
            Point(pos[0],pos[1], randint(-7,7), -15, (randint(0,255),randint(0,255),randint(0,255))))
        WIN.fill(colors[0])
        for point in points:
            point.draw()
        text_len = FONT.render(f"Balls: {len(points)}",True,colors[1])
        WIN.blit(text_len, (0,0))
        pygame.display.update()

    pygame.quit()

main()
