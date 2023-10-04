from math import sqrt
import pygame
from colors import Colors

from config import Config
from point import Point
from aaline import aaline
from translate import translate


class Grid:
    config: Config
    colors = Colors()

    def __init__(self,x, y,w,h,cap,pos,c,l=0):
        #constructor
        self.config =c
        self.FONT = pygame.font.SysFont(self.config.font,self.config.subTitle)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cap = cap
        self.pos = pos
        self.points = []
        self.layer = l
        self.surf = pygame.Surface((self.w,self.h))
        self.rect = self.surf.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.surf.fill(self.colors.white)
        self.surf.set_alpha(self.config.backgroundAlpha)

        # DONT KNOW WHY ITS NOT NEEDED BUT IT ISNT :)
        # pygame.draw.rect(self.surf,self.colors.white,self.surf.get_rect())

        self.divided = False
    
    def draw(self,WIN):
        #display background
        if self.config.showBackground:
            WIN.blit(self.surf,self.rect)
        
        #show borders of the grid
        if self.config.showBorders:
            pygame.draw.rect(WIN, self.colors.white,self.rect,1)

        if self.divided:
            # draw children if already divided
            self.tl.draw(WIN)
            self.tr.draw(WIN)
            self.bl.draw(WIN)
            self.br.draw(WIN)
        
    def showPointsLength(self,WIN):
        #show ammount of points within itself in the screen
        if self.config.showGridPoints:
            l = self.FONT.render(str(len(self.points)),True, self.colors.white)
            WIN.blit(l, (self.x+self.w-(l.get_width()),self.y))

    def divide(self):
        if self.divided:
            #divide each child
            self.tl.divide()
            self.tr.divide()
            self.bl.divide()
            self.br.divide()
        else:
            #create children
            self.tl = Grid(self.x,self.y,self.w/2,self.h/2,self.cap,'tl',self.config,self.layer+1)
            self.tr = Grid(self.x+self.w/2,self.y, self.w/2,self.h/2,self.cap,'tr',self.config,self.layer+1)
            self.bl = Grid(self.x,self.y+self.h/2,self.w/2,self.h/2,self.cap,'bl',self.config,self.layer+1)
            self.br = Grid(self.x+self.w/2,self.y+self.h/2,self.w/2,self.h/2,self.cap,'br',self.config,self.layer+1)
            self.divided= True

    def click(self,point,c=0):
        c += 1#how deep it is in the tree
        x = point.x
        y = point.y
        if len(self.points)>=self.cap:
            if self.divided:
                if x <= self.x + self.w/2:
                    #left side
                    if y <= self.y + self.h /2:
                        #top side
                        self.tl.click(point,c)
                    else:
                        #bottom side
                        self.bl.click(point,c)
                else:
                    #right side
                    if y <= self.y + self.h /2:
                        #top side
                        self.tr.click(point,c)
                    else:
                        #bottom side
                        self.br.click(point,c)
            else:
                self.divide()
                #insert each point of itself into its children before inserting new Point into them
                self.insertChildren()
                self.click(point)
        else:
            #add point to itself
            self.points.append(point)
    
    def insertChildren(self):
        for point in self.points:
            if point.x <= self.x + self.w/2:
                #left side
                if point.y <= self.y + self.h /2:
                    #top side
                    self.tl.points.append(point)
                else:
                    #bottom side
                    self.bl.points.append(point)
            else:
                #right side
                if point.y <= self.y + self.h /2:
                    #top side
                    self.tr.points.append(point)
                else:
                    #bottom side
                    self.br.points.append(point)
    
    def updatePoints(self,dt):
        if not self.divided:
            for point in self.points:
                # if point.x < 0 or point.x > self.config.width or point.y < 0 or point.y > self.config.height:
                #     self.points.remove(point)
                if point.x < self.x or point.x > self.x+self.w:
                    point.x_vel *= -1
                if point.y < self.y or point.y > self.y+self.h:
                    point.y_vel *= -1
                point.update(dt)
        else:
            self.tl.updatePoints(dt)
            self.tr.updatePoints(dt)
            self.bl.updatePoints(dt)
            self.br.updatePoints(dt)
    
    def render(self,WIN):
        if not self.divided:
            max_d = self.w/2
            min_d = 1
            for point in self.points:
                for other in self.points:
                    if other != point:
                        # pygame.draw.line(WIN, self.colors.green, (point.x,point.y),(other.x,other.y))
                        x_dif = point.x - other.x if point.x > other.x else other.x - point.x
                        y_dif = point.y - other.y if point.y > other.y else other.y - point.y
                        dif = (x_dif**2)+(y_dif**2)
                        if x_dif <= max_d and y_dif <= max_d:
                            a = translate(sqrt(dif), min_d, max_d, 255, 0)
                            a = 255 if a > 255 else (0 if a < 0 else a)
                            aaline(WIN, (4, 217, 255, a),
                                (point.x, point.y), (other.x, other.y))
        else:
            self.tl.render(WIN)
            self.tr.render(WIN)
            self.bl.render(WIN)
            self.br.render(WIN)