from distutils.spawn import spawn
from numpy import arctan
import pygame
from random import random, randint
from math import atan, ceil, cos, degrees, sin, radians, tan

pygame.init()


class Game:

    points = 0
    FONT = pygame.font.SysFont('Arial', 20)
    FONT_G = pygame.font.SysFont('Arial', 40)
    CLOCK = pygame.time.Clock()
    width, height = 700, 600

    def __init__(self):
        self.WIN = pygame.display.set_mode((self.width, self.height))
        self.player = Player(self.width*.5, self.height*.5)
        self.enemys = []
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.running = True
        self.spanw_rate = 100
        self.run()

    def run(self):
        while self.running:
            self.CLOCK.tick(60)
            self.WIN.fill('#000000')
            self.getEvents()
            self.drawMap()
            self.checkHits()
            if randint(0,self.spanw_rate)==7:
                self.spawnEnemy()
            self.updateEnemys()
            self.drawEnemys()
            self.player.draw(self.WIN)
            self.showStats()
            self.showPoints()
            self.showFps()
            pygame.display.update()
            self.points += 1
            if self.points>300 and self.spanw_rate > 10:
                self.spanw_rate = 100-int(self.points/300)
        pygame.quit()

    def checkHits(self):
        for i in range(len(self.player.shots)-1, -1, -1):
            b = self.player.shots[i]
            for e in self.enemys:
                if b.hit(e.body):
                    self.player.ammo += 10
                    self.enemys.remove(e)
                    self.points += 100
                    # self.player.shots.remove(b)
                    continue

    def spawnEnemy(self):
        self.enemys.append(Enemy(random()*self.width, random()*self.height))

    def drawEnemys(self):
        for e in self.enemys:
            e.draw(self.WIN)

    def showStats(self):
        bg = pygame.Rect(0, 0, 150, 25*(len(self.player.cooldowns)+2))
        pygame.draw.rect(self.WIN, '#cccccc', bg)
        y = 0
        t_ammo = self.FONT.render(
            'Ammo:'+str(self.player.ammo), True, '#000000')
        self.WIN.blit(t_ammo, (0, y))
        y += t_ammo.get_height()+5
        for c in range(len(self.player.cooldowns)):
            t = self.player.cooldowns[c][0]
            t_c = self.FONT.render(
                self.player.cooldowns[c][1]+':'+(str(t)+'t' if t > 0 else 'Ready'), True, '#000000')
            self.WIN.blit(t_c, (0, y))
            y += t_c.get_height() + 5

    def showPoints(self):
        t_points = self.FONT_G.render(
            str(int(self.points/100)), False, '#00ff00')
        self.WIN.blit(t_points, (self.width/2-t_points.get_width()/2, 0))
    
    def showFps(self):
        t_fps = self.FONT.render(str(int(self.CLOCK.get_fps())), False,'#000000')
        self.WIN.blit(t_fps, (self.width-t_fps.get_width(),0))

    def updateEnemys(self):
        for e in self.enemys:
            if e.body.colliderect(self.player.body):
                if self.player.cooldowns[2][0] == 0:
                    self.player.useShield()
                else:
                    self.running = False
                return
            if e.body.centerx > self.player.body.centerx:
                e.body.centerx += -1
            elif e.body.centerx < self.player.body.centerx:
                e.body.centerx += 1
            if e.body.centery > self.player.body.centery:
                e.body.centery += -1
            elif e.body.centery < self.player.body.centery:
                e.body.centery += 1

    def getEvents(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    self.player.blast()
                if e.key == pygame.K_e:
                    self.player.blast()
                    # if self.player.cooldowns[1][0] == 0:
                    #     self.player.dash(self.player.angle)
                    #     self.player.cooldowns[1][0] = 400
                if e.key == pygame.K_z:
                    self.player.gun_mode = (self.player.gun_mode-1)%2
                if e.key == pygame.K_x:
                    self.player.gun_mode = (self.player.gun_mode+1)%2
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1 and self.player.gun_mode==1:
                    self.player.shoot()
                if e.button == 3:
                    if self.player.cooldowns[1][0] == 0:
                        self.player.dash(self.player.angle)
                        self.player.cooldowns[1][0] = 400

        if pygame.mouse.get_pressed()[0] and self.player.gun_mode==0:
            self.player.shoot()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.angle = (self.player.angle+5) % 360
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player.angle = (self.player.angle-5) % 360
        if pygame.key.get_pressed()[pygame.K_w]:
            self.player.body.y += -3
            if self.player.body.top < 0:
                self.player.body.top = 0
        if pygame.key.get_pressed()[pygame.K_d]:
            self.player.body.x += 3
            if self.player.body.right > self.width:
                self.player.body.right = self.width
        if pygame.key.get_pressed()[pygame.K_s]:
            self.player.body.y += 3
            if self.player.body.bottom > self.height:
                self.player.body.bottom = self.height
        if pygame.key.get_pressed()[pygame.K_a]:
            self.player.body.x += -3
            if self.player.body.left < 0:
                self.player.body.left = 0
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.player.shoot()

    def drawMap(self):
        celH = int(self.height/len(self.map))
        for j in range(len(self.map)):
            celW = int(self.width/len(self.map[j]))
            for i in range(len(self.map[j])):
                pygame.draw.rect(self.WIN, '#ffffff' if self.map[j][i] == 1 else '#555555', ((
                    i*celW), (j*celH), celW, celH))


class Player:
    def __init__(self, x, y):
        self.body = pygame.Rect(x, y, 10, 10)
        self.angle = 0
        self.ammo = 100
        self.shots = []
        self.gun_mode = 0
        self.cooldowns = [[0, 'Blast'], [0, 'Dash'], [0, 'Shield']]

    def update(self):
        try:
            pos = pygame.mouse.get_pos()
            a = degrees(atan(abs(self.body.y-pos[1])/abs(self.body.x-pos[0])))
            if self.body.x>pos[0]:
                if self.body.y < pos[1]:
                    a = 90+90-a
                else:
                    a = 180+a
            else:
                if self.body.y>pos[1]:
                    a = 270+90-a
            self.angle = a
        except:
            print('')
        for c in range(len(self.cooldowns)):
            if self.cooldowns[c][0] > 0:
                self.cooldowns[c][0] -= 1

    def draw(self, WIN):
        self.update()
        for b in self.shots:
            if b.body.x > 750 or b.body.x < -50 or b.body.y > 650 or b.body.y < -50:
                self.shots.remove(b)
            else:
                b.draw(WIN)
        if self.gun_mode == 0:
            pygame.draw.line(WIN, '#333333', (self.body.centerx, self.body.centery),
                         (self.body.centerx+(cos(radians(self.angle))*30), self.body.centery+(sin(radians(self.angle))*30)), 7)
        elif self.gun_mode == 1:
            pygame.draw.polygon(WIN, '#333333',[(self.body.centerx,self.body.centery),(self.body.centerx+(cos(radians(self.angle-15))*30),self.body.centery+(sin(radians(self.angle-15))*30)),(self.body.centerx+(cos(radians(self.angle+15))*30),self.body.centery+(sin(radians(self.angle+15))*30))])
        pygame.draw.rect(WIN, '#66ff66', self.body)
        if self.cooldowns[2][0] == 0:
            pygame.draw.circle(
                WIN, '#aaaaff', (self.body.centerx, self.body.centery), 10, 2)
        if self.cooldowns[0][0] == 0:
            if self.gun_mode == 0:
                pygame.draw.line(WIN, '#ff5555', (self.body.centerx+(cos(radians(self.angle))*30), self.body.centery+(sin(radians(
                    self.angle))*30)), (self.body.centerx+(cos(radians(self.angle))*35), self.body.centery+(sin(radians(self.angle))*35)), 8)
            elif self.gun_mode == 1:
                pygame.draw.line(WIN,'#ff5555',(self.body.centerx+(cos(radians(self.angle-15))*30),self.body.centery+(sin(radians(self.angle-15))*30)),(self.body.centerx+(cos(radians(self.angle+15))*30),self.body.centery+(sin(radians(self.angle+15))*30)),3)

    def shoot(self):
        if self.ammo > 0:
            if self.gun_mode == 0:
                self.ammo -= 1
                self.shots.append(Shot(self.body.centerx+(cos(radians(self.angle))*30),
                                self.body.centery+(sin(radians(self.angle))*30), self.angle))
            elif self.gun_mode == 1:
                used_bullets = 0
                if self.ammo >= 10:
                    self.ammo -= 10
                    used_bullets = 10
                else:
                    used_bullets = self.ammo
                    self.ammo = 0
                for a in range(-15,16,int(30/used_bullets)+(1 if used_bullets<10 else 0)):
                    self.shots.append(Shot(self.body.centerx+(cos(radians(self.angle))*30),
                                self.body.centery+(sin(radians(self.angle+a))*30), self.angle+a))
            return
            x_of = cos(radians(self.angle))*-2
            y_of = sin(radians(self.angle))*-2
            self.body.x = float(self.body.x)+x_of
            self.body.y = float(self.body.y)+y_of
            if self.body.left < 0:
                self.body.left = 0
            if self.body.bottom > 600:
                self.body.bottom = 600
            if self.body.right > 700:
                self.body.right = 700
            if self.body.top < 0:
                self.body.top = 0

    def blast(self):
        if self.cooldowns[0][0] == 0:
            self.cooldowns[0][0] = 360
            for a in range(0, 361, 10):
                self.shots.append(Shot(
                    self.body.centerx+(cos(radians(a))*30), self.body.centery+(sin(radians(a))*30), a))

    def dash(self, a):
        self.body.x += int(cos(radians(a))*200)
        self.body.y += int(sin(radians(a))*200)

    def useShield(self):
        self.cooldowns[2][0] = 500
        a = random()*360
        self.dash(a)
        # self.angle = (180+a) % 360


class Shot:
    def __init__(self, x, y, angle):
        self.body = pygame.Rect(x, y, 5, 5)
        self.x_vel = cos(radians(angle))*5
        self.y_vel = sin(radians(angle))*5

    def update(self):
        self.body.x += self.x_vel
        self.body.y += self.y_vel

    def draw(self, WIN):
        self.update()
        pygame.draw.rect(WIN, '#ff0000', self.body, 0, 5)

    def hit(self, body):
        return self.body.colliderect(body)


class Enemy:
    def __init__(self, x, y):
        self.body = pygame.Rect(x, y, 20, 20)

    def draw(self, WIN):
        pygame.draw.rect(WIN, '#ff0000', self.body)


main = Game()
