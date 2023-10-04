from runpy import run_path
import pygame
from random import random

from colors import Colors
from slot import Slot
pygame.init()


class Cassino:

    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont('Arial', 50)
    FONT_SMALL = pygame.font.SysFont('Arial', 26)
    colors = Colors()

    width, height = 900, 900
    button_height = 50

    fps_lock = 60

    slots = []
    running = True
    spinning = False
    added = True

    balance = 100
    bet = 10

    def __init__(self):
        self.WIN = pygame.display.set_mode((self.width, self.height))
        self.setupFooter()
        self.setupButtons()
        self.slot_width = self.width / 5
        self.slot_height = self.height / 4
        self.slot_model = pygame.Rect(0, 0, self.slot_width, self.slot_height)
        self.shuffleSlots()
        self.run()

    def setupFooter(self):
        self.footer_height = self.height / 7
        self.footer = pygame.Rect(
            0, self.height-self.footer_height, self.width, self.footer_height)

    def setupButtons(self):
        col_size = self.width/6
        footer_y = self.height-self.footer_height
        y = footer_y + (self.footer_height/2-self.button_height/2)
        self.button_plus_1 = pygame.Rect(
            col_size*3+10, y, col_size-10, self.button_height)
        self.button_plus_5 = pygame.Rect(
            col_size*4+10, y, col_size-10, self.button_height)
        self.button_minus_1 = pygame.Rect(
            col_size*2+10, y, col_size-10, self.button_height)
        self.button_minus_5 = pygame.Rect(
            col_size*1+10, y, col_size-10, self.button_height)
        self.button_play = pygame.Rect(
            col_size*5+10, y-10, col_size-10, self.button_height+20)

    def shuffleSlots(self):
        slots_model = [1, 2, 3, 4, 5]
        self.slots.clear()
        for i in range(3):
            self.slots.append(Slot(slots_model))

    def run(self):
        self.running = True
        while self.running:
            self.CLOCK.tick(self.fps_lock)
            self.getEvents()
            self.draw()
            pygame.display.update()

    def getEvents(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.play()
                if e.key == pygame.K_DOWN:
                    self.slots_index = (1 + self.slots_index) % 5
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    x, y = e.pos[0], e.pos[1]
                    if self.button_play.collidepoint(x, y):
                        self.play()
                    if self.bet > 1 and self.button_minus_1.collidepoint(x, y):
                        self.bet -= 1
                    if self.bet > 5 and self.button_minus_5.collidepoint(x, y):
                        self.bet -= 5
                    if self.bet <= self.balance-1 and self.button_plus_1.collidepoint(x, y):
                        self.bet += 1
                    if self.bet <= self.balance-5 and self.button_plus_5.collidepoint(x, y):
                        self.bet += 5

    def draw(self):
        self.drawBackground()
        self.drawSlots()
        self.drawBalance()
        self.drawFooter()
        self.drawButtons()

    def drawBackground(self):
        self.WIN.fill(self.colors.black)

    def drawSlots(self):
        for i in range(len(self.slots)):
            x, y = self.slot_width + self.slot_width*i, 100
            self.slot_model.x = x
            self.slot_model.y = y
            pygame.draw.rect(self.WIN, self.colors.red, self.slot_model, 5)
            slot = self.slots[i]
            slot.update()
            content_v = slot.getValue()
            previous_v = slot.getPrevious()
            next_v = slot.getNext()
            running = self.slots[0].speed > 0 or self.slots[1].speed > 0 or self.slots[2].speed > 0
            c = 0
            if running:
                c = self.colors.white
            else:
                if self.checKValues():
                    c = self.colors.green
                else:
                    c = self.colors.red
            if not running:
                self.checkWin()
            content = self.FONT.render(str(content_v), False, c)
            previous = self.FONT.render(
                str(previous_v), False, self.colors.white)
            next = self.FONT.render(str(next_v), False, self.colors.white)
            self.WIN.blit(content, (x +
                          (self.slot_width-content.get_width())/2, y+self.slot_height/3))
            self.WIN.blit(previous, (x +
                          (self.slot_width-previous.get_width())/2, y-previous.get_height()))
            self.WIN.blit(next, (x +
                          (self.slot_width-next.get_width())/2, y+self.slot_height))

    def drawBalance(self):
        text = self.FONT.render(str(
            self.balance), True, (self.colors.green if self.balance > 30 else self.colors.red))
        self.WIN.blit(text, (0, 0))

    def drawFooter(self):
        pygame.draw.rect(self.WIN, self.colors.grey, self.footer)
        bet_text = self.FONT.render(
            f'+{self.bet}', False, self.colors.dark_green)
        self.WIN.blit(bet_text, (20, (self.height-self.footer_height) +
                      (self.footer_height/2-bet_text.get_height()/2)))

    def drawButtons(self):
        pygame.draw.rect(self.WIN, self.colors.green, self.button_plus_1)
        text_plus_1 = self.FONT_SMALL.render('+1', False, self.colors.black)
        self.WIN.blit(text_plus_1, (self.button_plus_1.x+(self.button_plus_1.width/2-text_plus_1.get_width()/2),
                      self.button_plus_1.y+(self.button_plus_1.height/2-text_plus_1.get_height()/2)))
        pygame.draw.rect(self.WIN, self.colors.green, self.button_plus_5)
        text_plus_5 = self.FONT_SMALL.render('+5', False, self.colors.black)
        self.WIN.blit(text_plus_5, (self.button_plus_5.x+(self.button_plus_5.width/2-text_plus_5.get_width()/2),
                      self.button_plus_5.y+(self.button_plus_5.height/2-text_plus_5.get_height()/2)))
        pygame.draw.rect(self.WIN, self.colors.red, self.button_minus_1)
        text_minus_1 = self.FONT_SMALL.render('-1', False, self.colors.black)
        self.WIN.blit(text_minus_1, (self.button_minus_1.x+(self.button_minus_1.width/2-text_minus_1.get_width()/2),
                      self.button_minus_1.y+(self.button_minus_1.height/2-text_minus_1.get_height()/2)))
        pygame.draw.rect(self.WIN, self.colors.red, self.button_minus_5)
        text_minus_5 = self.FONT_SMALL.render('-5', False, self.colors.black)
        self.WIN.blit(text_minus_5, (self.button_minus_5.x+(self.button_minus_5.width/2-text_minus_5.get_width()/2),
                      self.button_minus_5.y+(self.button_minus_5.height/2-text_minus_5.get_height()/2)))
        pygame.draw.rect(self.WIN, self.colors.green, self.button_play)
        play_text = self.FONT.render('PLAY', False, self.colors.black)
        self.WIN.blit(play_text, (self.button_play.x+(self.button_play.width/2-play_text.get_width()/2),
                      self.button_play.y+(self.button_play.height/2-play_text.get_height()/2)))

    def checkWin(self):
        if self.checKValues() and not self.spinning and not self.added:
            self.balance += self.bet * 3
            self.added = True

    def checKValues(self):
        return self.slots[0].getValue() == self.slots[1].getValue() and self.slots[1].getValue() == self.slots[2].getValue()

    def play(self):
        if self.bet > 0 and not self.spinning and self.balance >= self.bet:
            self.balance -= self.bet
            self.added = False
            for slot in self.slots:
                slot.speed = 1.5 + random()


cassino = Cassino()
