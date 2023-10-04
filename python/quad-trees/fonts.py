import pygame
pygame.init()
for font in pygame.font.get_fonts():
    open('fonts.txt','a').write(font+'\n')