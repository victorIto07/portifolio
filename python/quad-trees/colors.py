from random import randint


class Colors:
    white = '#ffffff'
    black = '#000000'
    grey = '#aaaaaa'
    green = '#36FF39'
    purple = '#7700EE'
    red = '#ff0000'
    blue = '#1188FF'
    yellow = '#ceff00'
    pink = '#ff1693'
    randomColors = [green,purple, red,blue,yellow,pink]

    def random(self):
        return self.randomColors[randint(0,len(self.randomColors)-1)]