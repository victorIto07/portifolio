import pygame

from config import Config
from colors import Colors

class Sidebar:
    config:Config
    colors = Colors()
    def __init__(self,config):
        self.config = config
        self.FONT = pygame.font.SysFont(self.config.font,self.config.subTitle)
        self.surf = pygame.Surface((self.config.width/4,self.config.height))
        self.surf.set_alpha(self.config.sidebarAlpha)
        self.rect = pygame.Rect(0,0,self.config.width/4,self.config.height)
        self.buttons = []
        self.setButtons()

    def setButtons(self):
        index = 0
        for key,value in self.config.options.items():
            button = {}
            button['key'] = key
            button['value'] = value
            button['type'] = 'bool' if value == True or value == False else 'text'
            text = self.FONT.render(f'{button["key"]}:',True,self.colors.white)
            button['rect'] = pygame.Rect(text.get_width()+5,((text.get_height()*index)+10),15,15)
            self.buttons.append(button)
            index+=1


    def drawOptions(self,WIN):
        index = 0
        for button in self.buttons:
            if button["type"] == 'bool':
                text = self.FONT.render(f'{button["key"]}:',True,self.colors.white)
                WIN.blit(text,(0,(index*text.get_height())+5))
                c = self.colors.green if button["value"] else self.colors.red
                pygame.draw.rect(WIN,c,button["rect"])
            else:
                text = self.FONT.render(f'{button["key"]}:{button["value"]}',True,self.colors.white)
                WIN.blit(text,(0,(index*text.get_height())+5))
            index +=1

    def draw(self,WIN):
        pygame.draw.rect(self.surf,self.colors.grey,self.surf.get_rect())
        WIN.blit(self.surf,self.rect)   
        self.drawOptions(WIN)

    def click(self,pos):
        for button in self.buttons:
            if button["type"] == 'bool' and button["rect"].collidepoint(pos[0],pos[1]):
                button["value"] = not button["value"]
                key = button["key"]
                val = button["value"]
                if key == 'max_cap':
                    self.config.max_cap = val
                elif key == 'n_points':
                    self.config.n_points = val
                elif key == 'drawPoints':
                    self.config.drawPoints = val
                elif key == 'updatePoints':
                    self.config.updatePoints = val
                elif key == 'updateGrids':
                    self.config.updateGrids = val
                elif key == 'drawPointsLines':
                    self.config.drawPointsLines = val
                elif key == 'showPointsLength':
                    self.config.showPointsLength = val
                elif key == 'showFps':
                    self.config.showFps = val
                elif key == 'drawFunction':
                    self.config.drawFunction = val
                elif key == 'pointsDraw':
                    self.config.pointsDraw = val
                elif key == 'drawArea':
                    self.config.drawArea = val
                elif key == 'showGridPoints':
                    self.config.showGridPoints = val
                elif key == 'showBorders':
                    self.config.showBorders = val
                elif key == 'showBackground':
                    self.config.showBackground = val
                elif key == 'showSidebar':
                    self.config.showSidebar = val
                elif key == 'startingPoints':
                    self.config.startingPoints = val
                
