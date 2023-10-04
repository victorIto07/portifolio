from random import randint
import pygame
from colors import Colors
from config import Config
from grid import Grid
from point import Point
from sidebar import Sidebar

class Game:

    config :Config
    colors = Colors()
    sidebar :Sidebar

    run = True
    clock = pygame.time.Clock()
    grid:Grid
    points = []
    fps:float

    def __init__(self,config):
        self.config = config
        self.sidebar = Sidebar(self.config)
        self.WIN = pygame.display.set_mode((self.config.width, self.config.height))
        self.FONT = pygame.font.SysFont(self.config.font, self.config.title)

    def init(self):
        self.points.clear()
        if self.config.startingPoints:
            for i in range(self.config.n_points):
                self.points.append(Point(randint(0,self.config.width),randint(0,self.config.height)))
        
        self.createTree()

    def createTree(self):
        self.grid = Grid(0, 0, self.config.width, self.config.height, self.config.max_cap,None,self.config,0)
        for point in self.points:
            self.grid.click(point)

    def showFps(self):
        if self.config.showFps:
            self.fps = int(self.clock.get_fps())
            fps_t = self.FONT.render(str(self.fps),False, self.colors.green)
            self.WIN.blit(fps_t, (self.config.width-fps_t.get_width(), 0))

    def showPointsLength(self):
        if self.config.showPointsLength:
            points = len(self.points)
            points_t = self.FONT.render(str(points),False, self.colors.white)
            self.WIN.blit(points_t, (self.config.width-points_t.get_width(), points_t.get_height()))
    
    def showSidebar(self):
        if self.config.showSidebar:
            self.sidebar.draw(self.WIN)

    def drawPoints(self):
        if self.config.drawPoints:
            for point in self.points:
                point.draw(self.WIN)

    def drawPointsLines(self):
        if self.config.drawPointsLines:
            self.grid.render(self.WIN)

    def update(self):
        if self.config.updatePoints:
            dt = self.clock.tick(self.fps)/10
            self.grid.updatePoints(dt)
            if self.config.updateGrids:
                self.createTree()

    def draw(self):
        self.grid.draw(self.WIN)
        self.drawPoints()
        self.drawPointsLines()
    
    def show(self):
        self.showFps()
        self.showPointsLength()
        self.showSidebar()

    def keyboardEvents(self,key):
        if key == pygame.K_SPACE:
            self.config.updatePoints = not self.config.updatePoints
        if key == pygame.K_RIGHT:
            self.config.showSidebar = not self.config.showSidebar
        if key == pygame.K_DOWN:
            self.init()
        if key == pygame.K_UP:
            self.createTree()
        
    def mouseEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.config.showSidebar and not self.config.drawFunction:
                for i in range(1):
                    self.points.append(Point(randint(event.pos[0],event.pos[0]),randint(event.pos[1],event.pos[1]),False))
                self.createTree()
            if self.config.showSidebar:
                self.sidebar.click(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            if not self.config.showSidebar and self.config.drawFunction and event.button == 1:
                self.createTree()

    def events(self):
        if not self.config.showSidebar and self.config.drawFunction and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            for i in range(self.config.pointsDraw):
                self.points.append(Point(randint(pos[0]-self.config.drawArea,pos[0]+self.config.drawArea),randint(pos[1]-self.config.drawArea,pos[1]+self.config.drawArea),False))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.keyboardEvents(event.key)
            self.mouseEvents(event)

    def main(self):
        self.init()
        while self.run:
            self.clock.tick(self.config.fps)
            self.WIN.fill(self.colors.black)
            self.events()
            self.update()
            self.draw()
            self.show()
            pygame.display.update()
        pygame.quit()