import pygame
from pygame.sprite import _Group
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png')
        self.rect = self.image.get_rect(topleft=pos)