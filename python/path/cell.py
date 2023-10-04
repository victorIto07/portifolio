from random import randint

class Cell:
    def __init__(self, path, cell_size, color, initial_pos):
        self.dead = False
        self.storage = None
        self.cell_size = cell_size
        self.color = color
        self.radius = 4 + randint(0, 2)
        self.pos = self.pos_from_coord(initial_pos)
        self.change_path(path)
        self.dest = self.pos_from_coord(self.path[self.idx+1])
        self.set_speed()

    def change_path(self,path):
        self.path = path
        self.path_len = len(self.path)
        self.idx = self.path.index(self.coord_from_pos(self.pos))
    
    def set_speed(self):
        self.speed = (0 if self.pos[0] == self.dest[0] else 1 if self.pos[0] < self.dest[0] else -1, 0 if self.pos[1] == self.dest[1] else 1 if self.pos[1] < self.dest[1] else -1)

    def next_dest(self):
        if self.idx < self.path_len - 1:
            self.idx += 1
            self.dest = self.pos_from_coord(self.path[self.idx])
            self.set_speed()
        else:
            self.dead = True

    def update(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        if (self.pos[0] > self.dest[0] and self.speed[0] > 0) or (self.pos[0] < self.dest[0] and self.speed[0] < 0):
            self.pos[0] = self.dest[0]
        if (self.pos[1] > self.dest[1] and self.speed[1] > 0) or (self.pos[1] < self.dest[1] and self.speed[1] < 0):
            self.pos[1] = self.dest[1]
        if self.dest == self.pos:
            self.next_dest()

    def pos_from_coord(self, coord):
        return [coord[0]*self.cell_size[0]+self.cell_size[0]/2, coord[1]*self.cell_size[1]+self.cell_size[1]/2]
    
    def coord_from_pos(self, pos):
        return (int(pos[0] / self.cell_size[0]), int(pos[1] / self.cell_size[1]))