from pygame import *
from Colors import Colors

colors = Colors()

class Head:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        
    def update(self,pai):
        self.x += pai.x_vel
        self.y += pai.y_vel
    
    def draw(self, WIN):
        draw.circle(WIN,colors.red, (self.x, self.y), self.r, self.r*2)
        draw.circle(WIN,colors.black, (self.x-(self.r/3), self.y-(self.r/3)), self.r*.1, int(self.r*.2))
        draw.circle(WIN,colors.black, (self.x+(self.r/3), self.y-(self.r/3)), self.r*.1, int(self.r*.2))
        draw.circle(WIN, colors.black, (self.x, self.y), self.r*.6, 2, draw_bottom_right=True)
        draw.circle(WIN, colors.black, (self.x, self.y), self.r*.6, 2, draw_bottom_left=True)