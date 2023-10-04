import pygame

from configs import Configs
from game import Game

pygame.init()

configs = Configs().props
game = Game(configs)

game.start()