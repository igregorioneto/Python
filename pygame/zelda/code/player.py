import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups) #../graphics/test/player.png
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'graphics', 'test', 'player.png'))
        self.rect = self.image.get_rect(topleft=pos)