from random import randint
from types import new_class
import pygame

pygame.init()

WIDTH, HEIGTH = 800, 800

n = 5

rows, cols = int(WIDTH/n), int(HEIGTH/n)

WIN = pygame.display.set_mode((WIDTH, HEIGTH))

grid = []


def init():
    if len(grid) > 0:
        grid.clear()
    for r in range(rows):
        grid.append([])
        for c in range(cols):
            grid[r].append(0)

    grid[int(rows/2)][int(cols/2)] = 12680


def shuffle():
    for j in range(rows-1):
        for i in range(cols-1):
            if grid[j][i] > 3:
                grid[j][i] -= 4
                grid[j-1][i] += 1
                grid[j+1][i] += 1
                grid[j][i-1] += 1
                grid[j][i+1] += 1


def render():
    for j in range(rows):
        for i in range(cols):
            cel = grid[j][i]
            color = ''
            if cel == 0:
                color = '#000000'
            elif cel == 1:
                color = '#00ff00'
            elif cel == 2:
                color = '#0000ff'
            elif cel == 3:
                color = '#ffffff'
            else:
                color = '#ff0000'
            pygame.draw.rect(WIN, color, pygame.Rect(i*n, j*n, n, n))


run = True
clock = pygame.time.Clock()
init()
while run:
    # clock.tick(60)
    for _ in range(5):
        shuffle()
    render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                init()

    pygame.display.update()

pygame.quit()
