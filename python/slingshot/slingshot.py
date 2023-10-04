from random import randint,random
import pygame

pygame.init()

WIDTH, HEIGTH = 1800, 900
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
FONT = pygame.font.SysFont('arial', 20, True)

colors = [(0, 0, 0), (255, 255, 255), (50, 50, 50), (200, 67, 67),(91,200,16)]

center = (WIDTH/2, HEIGTH/2)
points = []
particles = []
score = [0]


run = [True]


class Ball:
    def __init__(self, x, y, x_vel, y_vel, color):
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.x_start = x
        self.rect = pygame.Rect(x-3, y-3, 6, 6)
        self.att = True
        self.track = False
        self.points = []

    def draw(self):
        # if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y > HEIGTH:
        #     run[0] = False
        if self.x_start < center[0] and self.rect.x > center[0]:
            self.att = False
            self.track = True
        elif self.x_start > center[0] and self.rect.x < center[0]:
            self.att = False
            self.track = True
        if self.att == True:
            self.x_vel += (center[0] - self.rect.x)*.002
            self.y_vel += (center[1] - self.rect.y)*.002
        else:
            self.y_vel += .3
        if self.track == True:
            points.append((self.rect.x, self.rect.y))
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        pygame.draw.rect(WIN, self.color, self.rect, 6, 50)

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
        # self.x_vel -= gravity
        self.x += self.x_vel
        self.y_vel += .2
        self.y += self.y_vel

        self.lifetime -= .08
        if self.lifetime <= 0:
            particles.remove(self)
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
            particle_point.set_alpha(lifetime)
            pygame.draw.rect(particle_point, self.color,
                             particle_point.get_rect(), self.brightness, 50)
            WIN.blit(particle_point, (self.x-self.brightness /
                     2, self.y-self.brightness/2))

class Target:
    def __init__(self, x, y, color, width):
        self.color = color
        self.width = width
        self.rect = pygame.Rect(
            x+self.width/2, y+self.width/2, self.width, self.width)

    def draw(self):
        pygame.draw.rect(WIN, self.color, self.rect)


def main():
    clock = pygame.time.Clock()
    ball = None
    target = Target(randint(WIDTH-200, WIDTH-100) if randint(0, 1) ==
                    0 else randint(100, 200), randint(100, HEIGTH-100), colors[3], 30)
    while run[0]:
        clock.tick(90)
        WIN.fill(colors[0])
        text_score = FONT.render(f'Score: {score[0]}',False, colors[4])
        WIN.blit(text_score, (center[0]-text_score.get_width()/2,10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                points.clear()
                ball = Ball(pos[0], pos[1], 0, 0, colors[1])
        pygame.draw.line(WIN, colors[2], (WIDTH/2, 0), (WIDTH/2, HEIGTH), 1)
        if len(points) > 1:
            pygame.draw.lines(WIN, colors[1], False, points)
        if ball != None:
            ball.draw()
        pygame.draw.circle(WIN, colors[1], (WIDTH/2, HEIGTH/2), 5, 5)
        if ball != None:
            if target.rect.colliderect(ball.rect):
                score[0] += 1
                for _ in range(50):
                    particles.append(
                    Particle(target.rect.x, target.rect.y, random(), randint(-8, -3), (randint(0, 255), randint(0, 255), randint(0, 255)), 5, randint(2, 4)))
                target = Target(randint(WIDTH-200, WIDTH-100) if randint(0, 1) ==
                                0 else randint(100, 200), randint(100, HEIGTH-100), colors[3], 30)
        for particle in particles:
            particle.draw()
        target.draw()
        pygame.display.update()
    pygame.quit()


main()
