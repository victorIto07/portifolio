import pygame
from random import randint

pygame.init()

WIN_W, WIN_H = 800, 800

WIN = pygame.display.set_mode((WIN_W, WIN_H))

FONT = pygame.font.SysFont("arial", 16)

# COLORS
colors = [(0, 0, 0), (255, 255, 255), (255,0,0)]


class Particle:
    def __init__(self, x, y, color, x_vel, y_vel, infected):
        self.x = x
        self.y = y
        if infected:
            self.color = colors[2]
        else:
            self.color = color
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.rect = pygame.Rect(self.x, self.y, 5, 5)
        self.infected = infected

    def draw(self):
        if randint(0,10) == 1:
            self.x_vel = self.x_vel * -1
        if randint(0,10) == 1:
            self.y_vel = self.y_vel * -1
        pygame.draw.rect(WIN, self.color, self.rect,10,50)
        
    def collide(self, other):
        if self.rect.colliderect(other.rect) and (other.infected or self.infected):
            self.color = colors[2]
            other.color = colors[2]
            self.infected = True
            other.infected = True


def main():
    run = True
    particles = []
    clock = pygame.time.Clock()
    for _ in range(400):
        infected = randint(0,100)==1
        particles.append(Particle(randint(0, WIN_W),randint(0, WIN_H), colors[1], 1.5, 1.5,infected))

    while run:
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(colors[0])
        for p in range(len(particles)):
            particles[p].rect.x += particles[p].x_vel
            particles[p].rect.y += particles[p].y_vel
            if particles[p].rect.x < 0:
                particles[p].rect.x = WIN_W
            if particles[p].rect.y < 0:
                particles[p].rect.y = WIN_H
            if particles[p].rect.x > WIN_W:
                particles[p].rect.x = 0
            if particles[p].rect.y > WIN_H:
                particles[p].rect.y = 0
            particles[p].draw()
            for other_p in range(len(particles)):
                if other_p != p:
                    particles[p].collide(particles[other_p])
        if (len(particles)-len([p for P in particles if P.infected])) == 0:
            run = False
        text_infectds = FONT.render(f'People infected: {len([p for P in particles if P.infected])}', True, colors[1], colors[0])
        text_left = FONT.render(f'People left: {len(particles)-len([p for P in particles if P.infected])}', True, colors[1], colors[0])
        WIN.blit(text_infectds,(0,0))
        WIN.blit(text_left,(0,text_infectds.get_height()))


main()
