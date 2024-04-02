import pygame

class Obj:
    def __init__(self, image, x, y, frame_width, frame_height, scale_factor=1):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        
        self.sprite_sheet = pygame.image.load(image).convert_alpha()
        # Vai guardar cada quadro da imagem
        self.frames = []

        # Configurar a matriz de frames (x, y, largura, altura)
        for i in range(0, self.sprite_sheet.get_width(), frame_width):
            self.frames.append(self.sprite_sheet.subsurface((i, 0, frame_width, frame_height)))

        self.sprite.image = pygame.transform.scale(self.frames[0], (frame_width * scale_factor, frame_height * scale_factor))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame_index = 0
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

class Player(Obj):
    def __init__(self, image, x, y, frame_width, frame_height, scale_factor=1):
        super().__init__(image, x, y, frame_width, frame_height, scale_factor)
        