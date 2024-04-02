import pygame, os
from obj import Player

class Main:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode([800,600])
        self.title = pygame.display.set_caption("Game Sprites")

        self.loop = True
        self.fps = pygame.time.Clock()
        
        path = os.path.dirname(os.path.abspath(__file__))
        self.player = Player(os.path.join(path, "assets", "player.png"), 0 - 48, 0 - 48, 48, 48, 288, 480, 2.5)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.events()
            self.draw()
            self.fps.tick(30)
            pygame.display.update()            

    def draw(self):
        self.window.fill([0,0,0])
        self.player.drawing(self.window)

Main().update()