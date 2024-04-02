import pygame

class Obj:
    def __init__(self, image, x, y, sprite_width, sprite_height, pixels_x, pixels_y, scale_factor=1):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        
        self.sprite_sheet = pygame.image.load(image).convert_alpha()
        # Vai guardar cada quadro da imagem
        self.frames = []

        for j in range(0, pixels_y, sprite_height):
            for i in range(0, pixels_x, sprite_width):
                sprite = self.sprite_sheet.subsurface((i, j, sprite_width, sprite_height))
                sprite = pygame.transform.scale(sprite, (sprite_width * scale_factor, sprite_height * scale_factor))
                self.frames.append(sprite)
        
        self.frame_index = 0

        self.sprite.image = self.frames[self.frame_index]
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

class Player(Obj):
    def __init__(self, image, x, y, sprite_width, sprite_height, pixels_x, pixels_y, scale_factor=1):
        super().__init__(image, x, y, sprite_width, sprite_height, pixels_x, pixels_y, scale_factor)