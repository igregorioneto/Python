import pygame, random, sys, numpy as np

# Inicializando o pygame
pygame.init()

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
PLAYER = (255, 255, 255)
OBSTACLE = (255, 0, 0)
BACKGROUND = (0, 0, 0)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 2

# Classe do personagem que será controlado pelas setas do teclado
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER)
        self.rect = self.image.get_rect()
        self.rect.centerx = PLAYER_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speed_x = PLAYER_SPEED

        self.rect.x += self.speed_x

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH  

# Classe para obstáculos controlados pela rede neural
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(OBSTACLE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - OBSTACLE_HEIGHT)

    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()

# Classe para a rede neural
class NeuralNetwork:
    def __init__(self):
        # Número de neurônios de entrada, ocultos e saída
        self.input_size = 2
        self.hidden_size = 4
        self.output_size = 1

        # Pesos para as conexões entre os neurônios
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)

    def predict(self, inputs):
        # Propagação direta dos valores de entrada através da rede
        hidden = np.dot(inputs, self.weights_input_hidden)
        hidden = self.sigmoid(hidden)
        output = np.dot(hidden, self.weights_hidden_output)
        output = self.sigmoid(output)
        return output

    def sigmoid(self, x):
        x = np.clip(x, -500,500)
        return 1 / (1 + np.exp(-x))

def main():
    # Iniciando a tela do Jogo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Neural Network Game")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    neural_net = NeuralNetwork()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Gerando obstáculos
        if random.random() < 0.02:
            obstacle = Obstacle()
            all_sprites.add(obstacle)
            obstacles.add(obstacle)

        # Atualiza a posição dos sprites
        all_sprites.update()
        obstacles.update()

        # Controle dos obstáculos pela rede neural
        for obstacle in obstacles:
            obstacle.rect.x += OBSTACLE_SPEED
            inputs = np.array([[obstacle.rect.x, obstacle.rect.y]])
            output = neural_net.predict(inputs)
            if output > 0.5:
                obstacle.rect.y -= 1
            else:
                obstacle.rect.x += 1
        
        hits = pygame.sprite.spritecollide(player, obstacles, False)
        if hits:
            running = False

        # Desenhando na tela
        screen.fill(BACKGROUND)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()


