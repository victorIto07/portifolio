from random import randint

class Colors:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    dark_grey = (50, 50, 50)
    light_grey = (155, 155, 155)
    brown = (184, 134, 11)

    def cel_color(self, value):
        if value == 0:
            return self.dark_grey
        if value == 1:
            return self.blue
        if value == 2:
            return self.green

    def random(self):
        return (75 + randint(0, 105), 75 + randint(0, 105), 75 + randint(0, 105))
