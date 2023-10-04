import pygame
from colors import Colors
from cell import Cell
from machine import Machine
from storage import Storage

pygame.init()

COLORS = Colors()

class Main:
    WIDTH, HEIGHT = 800, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont('Arial',20,True)
    COLORS = Colors()
    qt_cols = 10
    qt_rows = 10
    selected_cel = None
    selected_machine = None
    fg_creating_path = False
    fg_creating_storage = False
    fg_creating_machine = False
    fg_selecting_machine_target = False
    new_path = None
    time = 0
    machine_size = (30, 30)
    storage_size = (50, 50)

    def __init__(self):
        self.run()
        self.set_variables()
        while 1:
            self.CLOCK.tick(60)
            self.read_events()
            self.update()
            self.draw()
            if self.running:
                self.time += 1

    def set_variables(self):
        self.cell_size = (self.WIDTH / self.qt_cols, self.HEIGHT / self.qt_rows)
        self.grid = [[0 for i in range(self.qt_cols)] for j in range(self.qt_rows)]
        self.paths = []
        self.cells = []
        self.machines = []
        self.storages = []

    def run(self):
        self.running = True

    def stop(self):
        self.running = False

    def read_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.read_keyboard_events(event)
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                or event.type == pygame.MOUSEBUTTONUP
            ):
                self.read_mouse_events(event)

    def read_keyboard_events(self, event):
        if event.key == pygame.K_p:
            self.stop() if self.running else self.run()
        if event.key == pygame.K_DOWN:
            self.set_variables()
        if event.key == pygame.K_SPACE:
            self.create_cells()
        if event.key == pygame.K_m or event.key == pygame.K_1:
            self.fg_creating_machine = True
            self.stop()
        if event.key == pygame.K_s or event.key == pygame.K_2:
            self.fg_creating_storage = True
            self.stop()

    def read_mouse_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.fg_creating_machine and not self.fg_selecting_machine_target:
                    _coord = self.coord_from_pos(event.pos)
                    self.selected_machine = Machine(_coord)
                    self.machines.append(self.selected_machine)
                    self.grid[_coord[1] + 1][_coord[0]] = 2
                    self.grid[_coord[1] - 1][_coord[0]] = 2
                    self.grid[_coord[1]][_coord[0] + 1] = 2
                    self.grid[_coord[1]][_coord[0] - 1] = 2
                    self.fg_selecting_machine_target = True
                elif self.fg_creating_machine and self.fg_selecting_machine_target:
                    _coord = self.coord_from_pos(event.pos)
                    if (
                        _coord[0] == self.selected_machine.coord[0]
                        and (abs(_coord[1] - self.selected_machine.coord[1]) == 1)
                    ) or (
                        _coord[1] == self.selected_machine.coord[1]
                        and (abs(_coord[0] - self.selected_machine.coord[0]) == 1)
                    ):
                        self.selected_machine.target = (_coord[0], _coord[1])
                        self.fg_creating_machine = False
                        self.fg_selecting_machine_target = False
                        self.grid[self.selected_machine.coord[1] + 1][
                            self.selected_machine.coord[0]
                        ] = 0
                        self.grid[self.selected_machine.coord[1] - 1][
                            self.selected_machine.coord[0]
                        ] = 0
                        self.grid[self.selected_machine.coord[1]][
                            self.selected_machine.coord[0] + 1
                        ] = 0
                        self.grid[self.selected_machine.coord[1]][
                            self.selected_machine.coord[0] - 1
                        ] = 0
                        self.run()
                elif self.fg_creating_storage:
                    _coord = self.coord_from_pos(event.pos)
                    self.storages.append(Storage(_coord))
                    self.fg_creating_storage = False
                    self.run()
                else:
                    self.fg_creating_path = True
                    self.stop()
                    self.new_path = []
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and not self.fg_creating_machine:
                self.fg_creating_path = False
                if len(self.new_path) > 1:
                    for coord in self.new_path:
                        self.grid[coord[1]][coord[0]] = 0
                    self.paths.append(self.new_path)
                    self.update_storages()
                else:
                    self.grid[self.new_path[0][1]][self.new_path[0][0]] = 0
                self.run()

    def update(self):
        if not self.time % 90 and self.running:
            self.create_cells()
        if self.fg_creating_path:
            pos = pygame.mouse.get_pos()
            coord = (int(pos[0] / self.cell_size[0]), int(pos[1] / self.cell_size[1]))
            v = self.grid[coord[1]][coord[0]]
            if not v:
                self.grid[coord[1]][coord[0]] = 1
                self.new_path.append(coord)

    def create_cells(self):
        for machine in self.machines:
            self.spawn_cel(machine)
        for storage in self.storages:
            storage.release()

    def draw(self):
        self.draw_background()
        self.draw_grid()
        self.draw_paths()
        self.draw_machines()
        self.draw_cels()
        self.draw_storages()
        pygame.display.update()

    def draw_background(self):
        self.WIN.fill(COLORS.black)

    def draw_grid(self):
        for j in range(self.qt_rows):
            for i in range(self.qt_rows):
                # pygame.draw.rect(self.WIN, COLORS.cel_color(self.grid[j][i]), (i * self.cell_size[0],j * self.cell_size[1], self.cell_size[0], self.cell_size[1]))
                c = None
                if self.fg_creating_machine or self.fg_creating_storage:
                    _i,_j = self.coord_from_pos(pygame.mouse.get_pos())
                    if _i == i and _j == j:
                        c = COLORS.blue
                if c == None:
                    c = COLORS.cel_color(self.grid[j][i])
                pygame.draw.rect(
                    self.WIN,
                    c,
                    (
                        i * self.cell_size[0],
                        j * self.cell_size[1],
                        self.cell_size[0],
                        self.cell_size[1],
                    ),
                    1,
                )

    def draw_paths(self):
        for path in self.paths:
            pygame.draw.lines(
                self.WIN,
                COLORS.white,
                False,
                [
                    [
                        coord[0] * self.cell_size[0] + self.cell_size[0] / 2,
                        coord[1] * self.cell_size[1] + self.cell_size[1] / 2,
                    ]
                    for coord in path
                ],
                2,
            )
            pygame.draw.circle(
                self.WIN,
                COLORS.green,
                (
                    self.cell_size[0] * path[0][0] + self.cell_size[0] / 2,
                    self.cell_size[1] * path[0][1] + self.cell_size[1] / 2,
                ),
                7,
            )
            pygame.draw.circle(
                self.WIN,
                COLORS.red,
                (
                    self.cell_size[0] * path[-1][0] + self.cell_size[0] / 2,
                    self.cell_size[1] * path[-1][1] + self.cell_size[1] / 2,
                ),
                5,
            )

    def draw_cels(self):
        for cell in self.cells:
            if cell.dead:
                _storage = self.storage_on_coord(self.coord_from_pos(cell.pos))
                if _storage:
                    if _storage.capacity > _storage.length:
                        cell.dead = False
                        _storage.add(cell)
                    else:
                        self.cells.remove(cell)
                    continue
                new_path = self.path_on_coord(self.coord_from_pos(cell.pos), cell.path)
                if new_path:
                    cell.dead = False
                    cell.change_path(new_path)
                    pygame.draw.circle(self.WIN, cell.color, cell.pos, cell.radius)
                    continue
                self.cells.remove(cell)
            elif not cell.storage:
                pygame.draw.circle(self.WIN, cell.color, cell.pos, cell.radius)
                if self.running:
                    cell.update()

    def draw_machines(self):
        for machine in self.machines:
            p = self.pos_from_coord(machine.coord)
            if machine.target:
                pygame.draw.line(
                    self.WIN, machine.color, p, self.pos_from_coord(machine.target), 4
                )
                pygame.draw.circle(
                    self.WIN, machine.color, self.pos_from_coord(machine.target), 5
                )
            pygame.draw.rect(
                self.WIN,
                machine.color,
                (
                    p[0] - self.machine_size[0] / 2,
                    p[1] - self.machine_size[1] / 2,
                    self.machine_size[0],
                    self.machine_size[1],
                ),
                0,
                10,
            )
            pygame.draw.rect(
                self.WIN,
                (machine.color[0]-35,machine.color[1]-35,machine.color[2]-35),
                (
                    p[0] - self.machine_size[0] / 2,
                    p[1] - self.machine_size[1] / 2,
                    self.machine_size[0],
                    self.machine_size[1],
                ),
                2,
                10,
            )

    def draw_storages(self):
        for storage in self.storages:
            p = self.pos_from_coord(storage.coord)
            pygame.draw.rect(
                self.WIN,
                COLORS.red if storage.length == storage.capacity else COLORS.brown,
                (
                    p[0] - self.storage_size[0] / 2,
                    p[1] - self.storage_size[1] / 2,
                    self.storage_size[0],
                    self.storage_size[1],
                ),
                0,
                10,
            )
            _cap = self.FONT.render(str(storage.length), False, COLORS.black)
            self.WIN.blit(_cap, (p[0]-_cap.get_width()/2,p[1]-_cap.get_height()/2))

    def path_on_coord(self, coord, current_path):
        for _path in self.paths:
            if _path == current_path:
                continue
            if coord in _path:
                return _path
            
    def storage_on_coord(self, coord):
        for _storage in self.storages:
            if _storage.coord == coord:
                return _storage
            
    def update_storages(self):
        for storage in self.storages:
            for path in self.paths:
                if storage.coord == path[0]:
                    storage.add_path(path)

    def spawn_cel(self, _machine):
        self.cells.append(Cell(self.path_on_coord(_machine.target, None), self.cell_size, _machine.color, _machine.target))

    def pos_from_coord(self, coord):
        return [
            coord[0] * self.cell_size[0] + self.cell_size[0] / 2,
            coord[1] * self.cell_size[1] + self.cell_size[1] / 2,
        ]

    def coord_from_pos(self, pos):
        return (int(pos[0] / self.cell_size[0]), int(pos[1] / self.cell_size[1]))

Main()
