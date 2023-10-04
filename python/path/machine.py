from colors import Colors

class Machine:
    def __init__(self, coord):
        self.target = None
        self.coord = coord
        self.color = Colors().random()