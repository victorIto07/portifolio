from random import randint
import pygame

pygame.init()


WIDTH, HEIGTH = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGTH))

colors = [(0,0,0), (255,255,255),(102,187,255),(255,204,238)]

particles = []

FONT = pygame.font.SysFont("mvboli", 50)

class Particle:
    def __init__(self, x, y, x_vel, y_vel, color, lifetime):
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.x_vel = x_vel
        self.color = color
        self.lifetime = lifetime
    
    def draw(self):
        self.lifetime -= 0.5
        if self.remove():
            particles.remove(self)
        else:
            self.x += self.x_vel
            self.y += self.y_vel
            if self.x > 0 and self.y > 0:
                lifetime = self.lifetime * 10
                if lifetime > 255:
                    lifetime = 255
                elif lifetime < 0:
                    lifetime = 0
                particle_shade = pygame.Surface((40,40))
                particle_shade.set_colorkey(colors[0])
                particle_shade.set_alpha(lifetime*0.1)
                pygame.draw.rect(particle_shade, self.color,particle_shade.get_rect(), 40, 50)
                WIN.blit(particle_shade, (self.x-20,self.y-20))
                
                particle_point = pygame.Surface((5,5))
                particle_point.set_colorkey(colors[0])
                lifetime = self.lifetime * 10
                particle_point.set_alpha(lifetime)
                pygame.draw.rect(particle_point, self.color, particle_point.get_rect(), 5, 50)
                WIN.blit(particle_point, (self.x-2,self.y-2))

    def remove(self):
        return self.lifetime < 0
        
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pos = pygame.mouse.get_pos()
        WIN.fill(colors[0])
        for i in range(2):
            particles.append(Particle(550,HEIGTH/2, randint(-6, 6), randint(-20,-15), (randint(0,255),randint(0,255),randint(0,255)),randint(20,30)))
            particles.append(Particle(WIDTH-550,HEIGTH/2, randint(-6, 6), randint(-20,-15), (randint(0,255),randint(0,255),randint(0,255)),randint(20,30)))
            particles.append(Particle(pos[0],pos[1], randint(-6, 6), randint(-30,-25), (randint(0,255),randint(0,255),randint(0,255)),randint(20,30)))
            particles.append(Particle(200,HEIGTH-200, randint(-6, 6), randint(-30,-25), (randint(0,255),randint(0,255),randint(0,255)),randint(20,30)))
            particles.append(Particle(WIDTH - 200,HEIGTH-200, randint(-6, 6), randint(-30,-25), (randint(0,255),randint(0,255),randint(0,255)),randint(20,30)))
        bg_text = FONT.render("PARABÉNS", True, colors[-1])
        WIN.blit(bg_text, (WIDTH/2-bg_text.get_width()/2,HEIGTH/2-bg_text.get_height()))
        for particle in particles:
            particle.y_vel += 1
            particle.draw()
        pygame.display.update()
    pygame.quit()

main()
