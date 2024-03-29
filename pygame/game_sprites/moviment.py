import pygame, sys, os

BACKGROUND = (0,0,0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAIN_DIRECTORY = os.path.dirname(__file__)
IMAGES_DIRECTORY = os.path.join(MAIN_DIRECTORY, 'sprites','characters')

class Player(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        # Carrega a imagem do sprite
        self.image = pygame.image.load(os.path.join(IMAGES_DIRECTORY, 'player.png')).convert_alpha()
        # Obtém o retângulo da imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

def main():
    # Inicializando o pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Movimentação Simples do Player")
    clock = pygame.time.Clock()
    # Cria um grupo de sprites
    all_groups = pygame.sprite.Group()
    # Instanciando o Jogador
    player = Player(x=100,y=100)
    # Adicionando no grupo de sprites
    all_groups.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_groups.update()
        screen.fill(BACKGROUND)

        all_groups.draw(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    main()