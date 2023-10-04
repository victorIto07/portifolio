import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 900, 900

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

colors = [
    (0, 0, 0),
    (255, 255, 255)
]

balls = []

class Particle:
    def __init__(self, x, y, x_vel, y_vel, color, lifetime, parent):
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.x_vel = x_vel
        self.color = color
        self.lifetime = lifetime
        self.parent = parent
    
    def draw(self):
        self.lifetime -= 0.2
        if self.remove():
            self.parent.particles.remove(self)
        else:
            self.x_vel += .04 if self.x_vel < 0 else -.04
            self.x += self.x_vel
            self.y += self.y_vel
            if self.x > 0 and self.y > 0:
                lifetime = self.lifetime * 25
                if lifetime > 255:
                    lifetime = 255
                elif lifetime < 0:
                    lifetime = 0
                particle_shade = pygame.Surface((40,40))
                particle_shade.set_alpha(lifetime*0.1)
                pygame.draw.rect(particle_shade, self.color,particle_shade.get_rect(), 40, 50)
                WIN.blit(particle_shade, (self.x-20,self.y-20))
                
                particle_point = pygame.Surface((5,5))
                lifetime = self.lifetime * 10
                particle_point.set_alpha(lifetime)
                pygame.draw.rect(particle_point, self.color, particle_point.get_rect(), 5, 50)
                WIN.blit(particle_point, (self.x-2,self.y-2))

    def remove(self):
        return self.lifetime < 0
        

class Ball():

    def __init__(self, x, y, x_vel, y_vel, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.particles = []

    def draw(self):
        if self.y >= HEIGHT:
            self.y_vel = self.y_vel * -1 * .96
        self.x_vel -= 0.01
        self.y += self.y_vel
        ball_surf = pygame.Surface((10,10))
        pygame.draw.rect(ball_surf, self.color,ball_surf.get_rect(), 40, 50)
        WIN.blit(ball_surf, (self.x-5,self.y-5))

def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors[0])
    while run:
        WIN.fill(colors[0])
        clock.tick(90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                balls.append(Ball(x,y, 0, 0, colors[1]))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    balls.remove(balls[randint(0,len(balls)-1)])
        if len(balls)>0:
            for ball in balls:
                ball.y_vel += 0.5
                ball.particles.append(Particle(ball.x, ball.y, randint(-2, 2),2,(randint(0,255),randint(0,255),randint(0,255)),10, ball))
                for particle in ball.particles:
                    particle.draw()
                ball.draw()
        pygame.display.update()
    pygame.quit()


main()
