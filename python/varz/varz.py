from math import radians, sin, cos
from random import randint, random
import pygame
import colorsys


pygame.init()

qt_points = 6
angles = []

delta_angle = 0

radius = 150
delta_radius = 0.04

delta_h = .00005

for i in range(qt_points):
    a = 360/qt_points*i
    angles.append(a)

WIN = pygame.display.set_mode((900,900))
h = 0
center = (450,450)
run = True
inner_touches = 0

def translate(l1,l2,r1,r2,v):
    l_off = l2-l1
    r_off = r2-r1
    p = v/l_off
    return r1 + r_off * p

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    if radius >= 450:
        delta_radius *= -1
    elif radius <= 75:
        delta_radius *= -1
        inner_touches += 1

    radius+=delta_radius

    delta_angle = translate(75 , 450, 0, 0.01, radius)

    h = (h + delta_h)%1

    for i in range(qt_points):
        angles[i] += delta_angle
        x = center[0]+(cos(radians(angles[i]))*radius)
        y = center[1]+(sin(radians(angles[i]))*radius)
        c = colorsys.hls_to_rgb(h,.5, 1)
        cor = (c[0]*255,c[1]*255,c[2]*255)
        pygame.draw.circle(WIN, cor,(x,y), 1)

    pygame.display.update()