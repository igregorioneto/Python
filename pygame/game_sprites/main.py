import pygame

class Main:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode([800,600])
        self.title = pygame.display.set_caption("Game Sprites")

        self.loop = True
        self.fps = pygame.time.Clock()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.events()
            pygame.display.update()

Main().update()