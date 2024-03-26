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
OBSTACLE_SPEED = 5

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
        super().__init__(self)
        pass

def main():
    # Iniciando a tela do Jogo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Neural Network Game")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    obstacle = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualiza a posição dos sprites
        all_sprites.update()

        # Desenhando na tela
        screen.fill(BACKGROUND)
        all_sprites.draw(screen)
        pygame.display.flip()
        
        clock.tick(FPS)

if __name__ == "__main__":
    main()


