import pygame
from config import Config
pygame.init()

from game import Game

config = Config()


game = Game(config)
game.main()