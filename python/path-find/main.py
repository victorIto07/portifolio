from math import sqrt
from random import random, shuffle
import pygame

from config import Config
from point import Point

pygame.init()

class PathFind:
    run = True
    config = Config().props
    WIN = pygame.display.set_mode((config["width"],config["height"]))
    FONT = pygame.font.SysFont('arial',25, True)
    CLOCK = pygame.time.Clock()
    points:list = []
    points_order:list = []
    best_length:float = None
    tries = 0

    def main(self):
        self.createPoints()
        while self.run:
            self.WIN.fill('#000000')
            self.readEvents()
            self.drawLines()
            self.drawPoints()
            self.drawBestLines()
            self.setOrder()
            self.showTries()
            pygame.display.update()
            self.shufflePoints()
        pygame.quit()

    def createPoints(self):
        self.points.clear()
        self.points_order.clear()
        self.tries = 0
        for i in range(0,self.config["qt_points"]):
            p = Point(random()*self.config["width"],random()*self.config["height"])
            self.points.append(p)
            self.points_order.append(p)
        
    def drawPoints(self):
        for point in self.points:
            point.draw(self.WIN)
    
    def drawLines(self):
        for i in range(0, len(self.points)-1):
            p = self.points[i]
            np = self.points[i+1]
            pygame.draw.line(self.WIN, '#0000ff', (p.x,p.y), (np.x,np.y))
    
    def drawBestLines(self):
        for i in range(0, len(self.points_order)-1):
            p = self.points_order[i]
            np = self.points_order[i+1]
            pygame.draw.line(self.WIN, '#ff00ff', (p.x,p.y), (np.x,np.y),3)
    
    def setOrder(self):
        dt = 0
        for i in range(0, len(self.points)-1):
            p = self.points[i]
            np = self.points[i+1]
            dx = p.x-np.x if p.x>np.x else np.x-p.x
            dy = p.y-np.y if p.y>np.y else np.y-p.y
            dt += sqrt(dx**2+dy**2)
        if self.best_length == None or self.best_length > dt:
            self.best_length = dt
            self.points_order = self.points.copy()
    
    def shufflePoints(self):
        shuffle(self.points)
        self.tries += 1

    def showTries(self):
        tries_text = self.FONT.render(str(self.tries),False, '#00ff00')
        self.WIN.blit(tries_text, (0,0))

    def readEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.createPoints()

pathFinder = PathFind()

pathFinder.main()