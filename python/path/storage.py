class Storage:
    def __init__(self, coord):
        self.paths = []
        self.path_lenth = 0
        self.coord = coord
        self.capacity = 50
        self.cells = []
        self.length = 0

    def add(self, cell):
        self.cells.append(cell)
        cell.storage = self
        self.length += 1

    def add_path(self, path):
        if path in self.paths:
            return
        self.paths.append(path)
        self.path_lenth = len(self.paths)

    def release(self):
        if self.path_lenth and self.length:
            for path in self.paths:
                if self.length:
                    _cell = self.cells.pop(0)
                    self.length -= 1
                    _cell.idx = 0
                    _cell.path = path
                    _cell.path_len = len(path)
                    _cell.dest = _cell.pos_from_coord(_cell.path[1])
                    _cell.set_speed()
                    _cell.storage = None