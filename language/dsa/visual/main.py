import pygame, sys

from constants import BACKGROUND_COLOR,FONT_COLOR,FONT_SIZE, LINE_COLOR, NODE_COLOR, NODE_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH 

from queue import Queue

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Estrutura de Dados com Python")
    clock = pygame.time.Clock()

    queue = Queue()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #Simula a adição de elementos na fila ao pressionar a barra de espaços
                    queue.enqueue(len(queue.elements) + 1)
                if event.key == pygame.K_r:
                    queue.dequeue()

        screen.fill(BACKGROUND_COLOR)
        queue.draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()