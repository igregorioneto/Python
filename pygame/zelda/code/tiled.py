import pygame, os
from settings import *

class Tiled(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups) #'../graphics/test/rock.png'
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'graphics', 'test', 'rock.png')).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        