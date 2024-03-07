from draw_structure import DrawStructure
from constants import BACKGROUND_COLOR,FONT_COLOR,FONT_SIZE, LINE_COLOR, NODE_COLOR, NODE_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH 

import pygame, sys

# Classe para representar uma Fila
class Queue(DrawStructure):
    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        if self.elements:
            return self.elements.pop(0)
        else:
            return None
        
    def draw(self, screen):
        x = 50
        y = SCREEN_HEIGHT // 2
        for element in self.elements:
            pygame.draw.circle(screen, NODE_COLOR, (x, y), 20)
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render(str(element), True, FONT_COLOR)
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)
            x += 50