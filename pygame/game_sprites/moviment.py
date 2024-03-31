import pygame, sys, os

BACKGROUND = (0,0,0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SIZE = (16,16)

MAIN_DIRECTORY = os.path.dirname(__file__)
IMAGES_DIRECTORY = os.path.join(MAIN_DIRECTORY, 'sprites','characters')

class Player(pygame.sprite.Sprite):
    def __init__(self,x, y, sprite_sheet):
        super().__init__()
        # Carrega a imagem do sprite       
        self.sprites = []
        img = sprite_sheet.subsurface((0, 0), (SPRITE_SIZE[0], SPRITE_SIZE[1]))
        img = pygame.transform.scale(img, (SPRITE_SIZE[0] * 3, SPRITE_SIZE[1] * 3))
        self.sprites.append(img)
        
        self.image = self.sprites[0]

        # Obtém o retângulo da imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)  # Posição inicial em (0, 0)


    def update(self):
        if self.index > 2:
            self.index = 0
        self.index += 0.25
        self.image = self.sprites[int(self.index)]    

def main():
    # Inicializando o pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Movimentação Simples do Player")
    clock = pygame.time.Clock()

    sprite_sheet = pygame.image.load(os.path.join(IMAGES_DIRECTORY, 'player.png')).convert_alpha()

    # Cria um grupo de sprites
    all_groups = pygame.sprite.Group()
    # Instanciando o Jogador
    player = Player(x=100,y=100, sprite_sheet=sprite_sheet)
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