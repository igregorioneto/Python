import pygame
from obj import Obj

class Main:
    def __init__(self, sizex, sizey, title):
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True
    
    def draw(self):
        pass

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()

if __name__ == "__main__":
    game = Main(320, 640, "BeeHoney")
    game.update()