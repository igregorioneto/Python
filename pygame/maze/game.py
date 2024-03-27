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
def draw_maze(screen, player):
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

# Classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()


def find_number_position(maze, number):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == number:
                return i, j
    return None

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((len(maze[0]) * CELL_SIZE, len(maze) * CELL_SIZE))
    pygame.display.set_caption("Maze")
    
    clock = pygame.time.Clock()

    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                position_player = find_number_position(maze,3)
                if keys[pygame.K_LEFT]:
                    next_position = (position_player[0], position_player[1] - 1)
                    if maze[next_position[0]][next_position[1]] == 0:            
                        maze[next_position[0]][next_position[1]] = 3
                        maze[position_player[0]][position_player[1]] = 0   
                if keys[pygame.K_RIGHT]:
                    next_position = (position_player[0], position_player[1] + 1)
                    if maze[next_position[0]][next_position[1]] == 0:
                        maze[next_position[0]][next_position[1]] = 3
                        maze[position_player[0]][position_player[1]] = 0
                if keys[pygame.K_UP]:
                    next_position = (position_player[0] - 1, position_player[1])
                    if maze[next_position[0]][next_position[1]] == 0:
                        maze[next_position[0]][next_position[1]] = 3
                        maze[position_player[0]][position_player[1]] = 0
                if keys[pygame.K_DOWN]:
                    next_position = (position_player[0] + 1, position_player[1])
                    if maze[next_position[0]][next_position[1]] == 0:
                        maze[next_position[0]][next_position[1]] = 3
                        maze[position_player[0]][position_player[1]] = 0

        screen.fill(BACKGROUND)
        # Desenhando Labirinto em tela
        draw_maze(screen=screen, player=player) 

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()


