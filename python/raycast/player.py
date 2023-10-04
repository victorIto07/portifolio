import pygame
from math import sin, cos, radians, tan


class Player:

    angle = 0
    show_body = True
    depth_view = 2

    def __init__(self, x, y, map_size):
        self.body = pygame.Rect(x, y, 10, 10)
        self.map_size = map_size

    def draw(self, WIN, grid):
        # draw body
        if self.show_body:
            pygame.draw.rect(WIN, '#ff5555', self.body, 0, 5)

        # draw ray
        row_height = self.map_size[1]/len(grid)
        row_number = int(self.body.centery // row_height)
        row_into = grid[row_number]
        col_width = self.map_size[0]/len(row_into)
        col_number = int(self.body.centerx // col_width)
        ray_color = '#ffffff'

        # RAIO COORDENADAS
        vert_ray_x = None
        vert_ray_y = None
        vert_depth_view = 0
        vert_found = False
        while not vert_found:
            if self.angle == 90:
                vert_ray_x = self.body.centerx
                vert_ray_y = self.map_size[1]
            elif self.angle == 270:
                vert_ray_x = self.body.centerx
                vert_ray_y = 0
            elif self.angle > 270 or self.angle < 90:
                # olhando pra direita
                vert_ray_x = col_width*(col_number+vert_depth_view+1)
                vert_ray_y = self.body.centery + (tan(radians(self.angle))*(vert_ray_x-self.body.centerx))
            else:
                # olhando pra esquerda
                vert_ray_x = col_width*(col_number-vert_depth_view)
                vert_ray_y = self.body.centery + (tan(radians(180-self.angle))*(self.body.centerx-vert_ray_x))
                
            vert_row_number = int(vert_ray_y / row_height)
            vert_col_number = int(vert_ray_x / col_width)
            if not (self.angle > 270 or self.angle < 90):
                vert_col_number -= 1
            
            vr_index = vert_row_number if vert_row_number < len(grid) else len(grid) - 1
            vr_index = vert_row_number if vert_row_number >= 0 else 0
            vc_index = vert_col_number if vert_col_number < len(grid[vr_index]) else len(grid[vr_index]) - 1
            vc_index = vert_col_number if vert_col_number >= 0 else 0
            print(vr_index,vc_index)
            if not grid[vr_index][vc_index]:
                vert_depth_view += 1
            else:
                vert_found = True
        dist_vert = ((abs(vert_ray_y-self.body.centery)**2) + (abs(vert_ray_x-self.body.centerx)**2))**0.5
        pygame.draw.line(WIN, ray_color, (self.body.centerx,self.body.centery), (vert_ray_x, vert_ray_y), 1)
            

        # RAIO ABSCISSAS
        # hoz_ray_x = None
        # hoz_ray_y = None
        # hoz_row_number = None
        # hoz_col_number = None
        # hoz_depth_view = self.depth_view
        # if self.angle == 0:
        #     hoz_ray_y = self.body.centery
        #     hoz_ray_x = self.map_size[0]
        # elif self.angle == 180:
        #     hoz_ray_y = self.body.centery
        #     hoz_ray_x = 0
        # elif self.angle > 180 and self.angle < 360:
        #     # olhando pra cima
        #     hoz_ray_y = row_height*(row_number-hoz_depth_view)
        #     hoz_ray_x = self.body.centerx - (tan(radians(270 - self.angle))*(self.body.centery-hoz_ray_y))
        #     hoz_row_number = int(hoz_ray_y // row_height)
        #     hoz_col_number = int(hoz_ray_x // col_width)
        #     ray_color = '#55ff55' if grid[hoz_row_number-1][hoz_col_number] else '#ff5555'
        # else:
        #     # olhando pra baixo
        #     hoz_ray_y = row_height*((row_number+1)+hoz_depth_view)
        #     hoz_ray_x = self.body.centerx + ((hoz_ray_y-self.body.centery) * tan(radians(90-self.angle)))
        #     hoz_row_number = int(hoz_ray_y // row_height)
        #     hoz_col_number = int(hoz_ray_x // col_width)
        #     ray_color = '#55ff55' if grid[hoz_row_number][hoz_col_number] else '#ff5555'
        # # print(hoz_col_number, hoz_row_number)
        # dist_hoz = ((abs(hoz_ray_y-self.body.centery)**2) +
        #             (abs(hoz_ray_x-self.body.centerx)**2))**0.5

        # ray_x = hoz_ray_x if dist_hoz < dist_vert else vert_ray_x
        # ray_y = hoz_ray_y if dist_hoz < dist_vert else vert_ray_y
        # pygame.draw.line(WIN, '#5555ff', (self.body.centerx,
        #                  self.body.centery), (ray_x, ray_y), 1)
