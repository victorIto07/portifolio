import pygame
from random import randint, random

pygame.init()

WIDTH, HEIGTH = 1920, 1080

WIN = pygame.display.set_mode((WIDTH, HEIGTH))

colors = [(0, 0, 0), (255, 255, 255), (30, 30, 30)]

fireworks = []
particles = []

gravity = .2


class Firework:
    def __init__(self, x, y, y_vel, color, lifetime):
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.color = color
        self.lifetime = lifetime
        self.exploded = False

    def draw(self):
        self.lifetime -= .1
        if self.lifetime <= 0:
            self.explode()
        self.y_vel -= .3
        self.y += self.y_vel

        pygame.draw.circle(WIN, self.color, (self.x, self.y), 5, 5)

    def explode(self):
        for _ in range(50):
            particles.append(
                Particle(self.x, self.y, random(), randint(-8, -3), (randint(0, 255), randint(0, 255), randint(0, 255)), 5, randint(2, 4)))
        fireworks.remove(self)

class Particle:
    def __init__(self, x, y, x_vel, y_vel, color, lifetime, brightness):
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.x_vel = x_vel * randint(2, 5)
        if randint(0, 1) == 0:
            self.x_vel *= -1
        self.color = color
        self.lifetime = lifetime
        self.brightness = brightness

    def draw(self):
        self.lifetime -= .08
        if self.lifetime <= 0:
            particles.remove(self)
        # self.x_vel -= gravity
        self.x += self.x_vel
        self.y_vel += gravity
        self.y += self.y_vel

        lifetime = self.lifetime * 50
        if lifetime > 255:
            lifetime = 255
        if lifetime > -1:
            particle_shade = pygame.Surface(
                (self.brightness*8, self.brightness*8))
            particle_shade.set_colorkey(colors[0])
            particle_shade.set_alpha(lifetime*0.1)
            pygame.draw.rect(particle_shade, self.color,
                             particle_shade.get_rect(), self.brightness*8, 50)
            WIN.blit(particle_shade, (self.x-self.brightness *
                     4, self.y-self.brightness*4))

            particle_point = pygame.Surface((3, 3))
            particle_point.set_colorkey(colors[0])
            particle_shade.set_alpha(lifetime)
            pygame.draw.rect(particle_point, self.color,
                             particle_point.get_rect(), self.brightness, 50)
            WIN.blit(particle_point, (self.x-self.brightness /
                     2, self.y-self.brightness/2))


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        WIN.fill(colors[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fireworks.append(
                    Firework(pos[0], pos[1], 0, colors[2], randint(5, 7)))

        if randint(0, 25) == 0:
            fireworks.append(Firework(
                randint(20, WIDTH-20), randint(HEIGTH-20, HEIGTH), 0, colors[2], randint(5, 7)))

        if len(fireworks) > 0:
            for firework in fireworks:
                firework.draw()
        if len(particles) > 0:
            for particle in particles:
                particle.draw()
        pygame.display.update()

    pygame.quit()


main()
