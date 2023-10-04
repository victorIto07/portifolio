import pygame

pygame.init()

class game:

    width,height = 900,900
    WIN = pygame.display.set_mode((width, height))
    running = True
    trace = []
    CLOCK = pygame.time.Clock()

    def __init__(self):
        pygame.mouse.set_visible(False)
        while self.running:
            self.CLOCK.tick(50)
            self.getEvents()
            self.draw()
        pygame.quit()

    def getEvents(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running = False

    def draw(self):
        self.WIN.fill('#000000')
        mousePos = pygame.mouse.get_pos()
        self.updateTrace(mousePos)
        self.drawTrace()
        self.drawPoint(self.trace[-1])
        pygame.display.update()

    def drawTrace(self):
        if len(self.trace)<2:
            return
        pygame.draw.lines(self.WIN, '#ff0000',False, self.trace)

    def drawPoint(self, pos):
        pygame.draw.circle(self.WIN, '#55ff99', pos,5)

    def updateTrace(self, pos):
        self.trace.insert(0,pos)
        if len(self.trace)>30:
            self.trace.pop()
main = game()