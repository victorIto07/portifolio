from random import randint, random
import pygame

pygame.init()
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

balls = []

selected_color = [0]
selected_pallet = ['main']

main_colors = ['#000000', '#ffffff', '#050505',
               (143, 206, 0), (204, 0, 0)]
colors = {"main": [(225, 247, 213), (255, 189, 189), (201, 201, 255), (255, 255, 255), (241, 203, 255)
                   ],
          "cyberpunk": [
              (214, 0, 255), (189, 0, 255), (0, 30,
                                             255), (0, 184, 255), (0, 255, 159)
],
    "premiere_league": [
              (4, 245, 255), (233, 0, 82), (255,
                                            255, 255), (0, 255, 133), (56, 0, 60)
],
    "vaporwave": [(255, 0, 193), (150, 0, 255), (73, 0, 255), (0, 184, 255), (0, 255, 249)],
    "bootstrap": [(217, 83, 79), (249, 249, 249), (91, 192, 222), (92, 184, 92), (66, 139, 202)]
}
buttons = []

FONT = pygame.font.SysFont("corbel", 20)
pallets = []

clicked = [True]

text_show = FONT.render('Show menus', True, main_colors[4])
text_show_rect = text_show.get_rect()
text_show_rect.x, text_show_rect.y = WIDTH - \
    text_show.get_width()-15, text_show.get_height()
show = [True]

hover = [False]


class Ball:
    def __init__(self, x, y, color, size_x, size_y, x_vel, y_vel, line_width):
        self.x = x
        self.y = y
        if randint(0, 1) == 1:
            x_vel *= -1
        if randint(0, 1) == 1:
            y_vel *= -1
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.size_x = size_x
        self.size_y = size_y
        self.line_width = line_width

    def draw(self):
        if self.x > WIDTH or self.x < 0:
            self.x_vel *= -1
        if self.y > HEIGHT or self.y < 0:
            self.y_vel *= -1
        # if self.x > WIDTH:
        #     self.x = 0
        # if self.x < 0:
        #     self.x = WIDTH
        # if self.y > HEIGHT:
        #     self.y = 0
        # if self.y < 0:
        #     self.y = HEIGHT

        self.x += self.x_vel
        self.y += self.y_vel
        surf = pygame.Surface((self.size_x, self.size_y))
        pygame.draw.rect(surf, self.color, surf.get_rect(), self.size_x, 50)
        WIN.blit(surf, (self.x-self.size_x/2, self.y-self.size_y/2))


def create_balls():
    balls.clear()
    buttons.clear()
    pallets.clear()
    # SET PALLET AS COLORS
    for color in colors[selected_pallet[0]]:
        for _ in range(randint(2, 3)):
            balls.append(Ball(randint(50, WIDTH - 50), randint(
                50, HEIGHT-50), color, 10, 10, random(), random(), randint(1, 3)))
    dif_colors = list(set(map(lambda x: x.color, balls)))
    for i in range(len(dif_colors)):
        surf = pygame.Surface((15, 15))
        rect = surf.get_rect()
        rect.x, rect.y = 20, 35*(i+1)
        buttons.append([surf, rect, dif_colors[i]])
    txt_placement = 20
    for key in colors.keys():
        text_pallet = FONT.render(key, True, colors[key][0])
        rect_pallet = text_pallet.get_rect()
        rect_pallet.x, rect_pallet.y = txt_placement, HEIGHT-50
        txt_placement += text_pallet.get_width() + 15
        pallets.append([text_pallet, rect_pallet, key])


def render_balls():
    pos = pygame.mouse.get_pos()
    WIN.fill(main_colors[2])
    for ball in balls:
        ball.draw()
        poly = []
        others = list(filter(lambda x: x.color == ball.color, balls))
        for i in range(len(others)-1, -1, -1):
            other = others[i]
            poly.append((other.x, other.y))
        if len(poly) > 1:
            pygame.draw.polygon(WIN, ball.color, poly, ball.line_width)
    if not show[0]:
        WIN.blit(FONT.render('Show menus', True,
                 main_colors[3]), text_show_rect)
    else:
        WIN.blit(text_show, text_show_rect)
    if text_show_rect.collidepoint(pos[0], pos[1]):
        hover[0] = True
        if pygame.mouse.get_pressed()[0] and clicked[0]:
            show[0] = not show[0]
            clicked[0] = False
    if show[0]:
        text_sel_pal = FONT.render(
            f'Pallet: {selected_pallet[0]}', True, (colors[selected_pallet[0]][0]))
        WIN.blit(text_sel_pal, (20, 5))
        for button in buttons:
            if button[1].collidepoint(pos[0], pos[1]):
                hover[0] = True
                if pygame.mouse.get_pressed()[0]:
                    selected_color.clear()
                    selected_color.append(button[2])
            pygame.draw.rect(button[0], button[2], button[1], 10, 5)
            WIN.blit(button[0], (button[1].x, button[1].y))
            if selected_color[0] == button[2]:
                text = 'Selected color'
            else:
                text = '<- Select this color'
            text_color = FONT.render(text, True, button[2])
            WIN.blit(text_color, (button[1].x+20, button[1].y-3))
        for i in range(len(pallets)):
            pallet = pallets[i]
            WIN.blit(pallet[0], pallet[1])
            if pallet[1].collidepoint(pos[0], pos[1]):
                hover[0] = True
                if pygame.mouse.get_pressed()[0] and clicked[0]:
                    selected_pallet.clear()
                    selected_color.clear()
                    selected_color.append(0)
                    selected_pallet.append(pallet[2])
                    create_balls()
                    clicked[0] = False
    if hover[0] == True:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    hover[0] = False

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(main_colors[0])
    create_balls()
    while run:
        clock.tick(90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    create_balls()
                    render_balls()
            if event.type == pygame.MOUSEBUTTONDOWN and selected_color[0] != 1:
                clicked[0] = True
                if event.button == pygame.BUTTON_RIGHT and selected_color[0] != 0:
                    pos = pygame.mouse.get_pos()
                    balls.append(Ball(
                        pos[0], pos[1], selected_color[0], 10, 10, random(), random(), randint(1, 3)))
            if event.type == pygame.MOUSEBUTTONUP:
                clicked[0] = True
        render_balls()
        pygame.display.update()
    pygame.quit()


main()
