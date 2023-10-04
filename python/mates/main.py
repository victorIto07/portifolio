import pygame
from random import randint
from math import sqrt
from aaline import aaline
from translate import translate

pygame.init()

def random_color():
    return (50+randint(0, 150),50+randint(0, 150),50+randint(0, 150))

class Person:
    def __init__(self, x, y, i):
        self.mate = None
        self.id = i
        self.surf = pygame.surface.Surface((20,20), pygame.SRCALPHA)
        self.surf.convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.center = (x,y)
        self.paint(random_color())
    
    def paint(self, c):
        self.color = c
        self.surf.fill(self.color)

    def set_mate(self, mate):
        self.mate = mate
        mate.mate = self
        myColor = self.color
        mateColor = mate.color
        self.paint((255,0,0))
        mate.paint((255,0,0))
        pygame.draw.circle(self.surf,mateColor, (10,10), 5)
        pygame.draw.circle(mate.surf,myColor, (10,10), 5)
    
    def closest_color(self, closest):
        pygame.draw.circle(self.surf,closest.color, (10,10), 5)
        pygame.draw.circle(self.surf,(0,0,0), (10,10), 5, 1)

class Main:

    WIDTH,HEIGHT = 1000,1000
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    qt_people = 5
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font(size = 30)

    def __init__(self):
        self.set_variables()
        self.running = True
        while self.running:
            self.CLOCK.tick(30)
            self.draw()
            self.read_events()

    def set_variables(self):
        self.people = [Person(randint(0, self.WIDTH), randint(0, self.HEIGHT), i) for i in range(self.qt_people)]

    def read_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.read_keyboard_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.people.append(Person(event.pos[0],event.pos[1], len(self.people)))

    def read_keyboard_events(self, event):
        if event.key == pygame.K_DOWN:
            self.set_variables()
        if event.key == pygame.K_LEFT:
            self.qt_people -= 1
            self.set_variables()
        if event.key == pygame.K_RIGHT:
            self.qt_people += 1
            self.set_variables()
        if event.key == pygame.K_UP:
            self.qt_people += 1
            self.people.append(Person(randint(0, self.WIDTH), randint(0, self.HEIGHT),len(self.people)))
    
    def draw(self):
        self.WIN.fill((0,0,0))
        self.draw_people()
        self.show_fps()
        pygame.display.update()

    def show_fps(self):
        fps_t = self.FONT.render(str(int(self.CLOCK.get_fps())),False, (0,255,0))
        self.WIN.blit(fps_t,(0,0))

    def draw_people(self):
        for person in self.people:
            if person.mate:
                self.WIN.blit(person.surf, person.rect)
                continue
            closest_person = []
            closest_person_dist = [None]
            tri_size = []
            other_people = list(filter(lambda x: (not x.mate) and x.id != person.id, self.people))
            if not len(other_people):
                self.set_variables()
                return
            for other_person in other_people:
                if other_person.id == person.id:
                    continue
                dx = abs(person.rect.centerx - other_person.rect.centerx)
                dy = abs(person.rect.centery - other_person.rect.centery)
                if dx < 20 and dy < 20:
                    person.set_mate(other_person)
                    continue
                dist = sqrt((dx**2)+(dy**2))
                if closest_person_dist[0] == None or closest_person_dist[0] > dist:
                    closest_person_dist[0] = dist
                    if len(closest_person):
                        closest_person.pop()
                    closest_person.append(other_person)
                    tri_size = [int(dx), int(dy)]
            if not len(tri_size):
                self.WIN.blit(person.surf, person.rect)
                continue
            # print(degrees(atan2(tri_size[1],tri_size[0])))
            big_size = tri_size[0] if tri_size[0]>tri_size[1] else tri_size[1]
            r_dx = tri_size[0]/big_size
            r_dy = tri_size[1]/big_size
            if person.rect.centerx > closest_person[0].rect.centerx:
                person.rect.centerx -= r_dx
                closest_person[0].rect.centerx += r_dx
            else:
                person.rect.centerx += r_dx
                closest_person[0].rect.centerx -= r_dx
            if person.rect.centery > closest_person[0].rect.centery:
                closest_person[0].rect.centery += r_dy
                person.rect.centery -= r_dy
            else:
                closest_person[0].rect.centery -= r_dy
                person.rect.centery += r_dy
            a = 5 - (translate(closest_person_dist[0],50, 300, 1, 5))
            aaline(self.WIN, person.color, person.rect.center, closest_person[0].rect.center, a)
            # pygame.draw.line(self.WIN, person.color, person.rect.center, closest_person[0].rect.center, 5)
            person.closest_color(closest_person[0])
            self.WIN.blit(person.surf, person.rect)
Main()