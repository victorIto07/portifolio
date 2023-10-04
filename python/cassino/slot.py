from random import shuffle,randint

from colors import Colors


class Slot:

    colors = Colors()
    speed = 0

    def __init__(self, arr):
        self.order = arr.copy()
        shuffle(self.order)
        self.index = randint(0, (len(arr)-1))
        self.color = self.colors.white

    def getValue(self):
        return self.order[int(self.index)]

    def getPrevious(self):
        return self.order[(int(self.index)-1) % len(self.order)]

    def getNext(self):
        return self.order[(int(self.index)+1) % len(self.order)]

    def update(self):
        if self.speed > 0:
            self.index = (self.index + self.speed) % len(self.order)
            self.speed += -0.01
        if self.speed < 0:
            self.speed = 0
