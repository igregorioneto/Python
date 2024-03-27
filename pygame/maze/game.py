import pygame, sys

# Constantes
CELL_SIZE = 40
WALL_COLOR = (0, 0, 0)  # Cor das paredes
PATH_COLOR = (255, 255, 255)  # Cor dos caminhos
DESTINATION_COLOR = (255, 0, 0)  # Cor do ponto de destino
PLAYER_COLOR = (97, 94, 233)  # Cor do jogador
BACKGROUND = (255,255,255) # Cor do Background
FPS = 60 # FPS do jogo

# Representação do labirinto
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 3, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Função para desenhar o labirinto
def draw_maze(screen):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                color = WALL_COLOR
            elif cell == 0:
                color = PATH_COLOR
            elif cell == 2:
                color = DESTINATION_COLOR
            elif cell == 3:
                color = PLAYER_COLOR
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (0,0,0), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((len(maze[0]) * CELL_SIZE, len(maze) * CELL_SIZE))
    pygame.display.set_caption("Maze")
    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND)
        # Desenhando Labirinto em tela
        draw_maze(screen=screen) 

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()


