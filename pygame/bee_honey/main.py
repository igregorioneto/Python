import pygame
from obj import Obj
from menu import Menu

class Main:
    def __init__(self, sizex, sizey, title):
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        self.menu = Menu()

        # self.start_screen = Obj('assets/start.png', 0, 0)
    
    def draw(self):
        # self.window.fill([0,0,0])
        # self.start_screen.drawing(self.window)
        if not self.menu.change_scene:
            self.menu.draw(self.window)

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            
            self.menu.events(events)

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()

if __name__ == "__main__":
    game = Main(360, 640, "BeeHoney")
    game.update()