import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))

pygame.init()

screen_width = 800
screen_hight = 600

screen = pygame.display.set_mode((screen_width, screen_hight))

pygame.display.set_caption("Meu Jogo")

player = Player(0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    elif keys[pygame.K_RIGHT]:
        player.rect.x += 5

    if keys[pygame.K_UP]:
        player.rect.y -= 5
    elif keys[pygame.K_DOWN]:
        player.rect.y += 5

    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    pygame.display.flip()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    screen.fill((255, 255, 255))
    
    player.draw(screen)
    
    pygame.display.update()
    
pygame.quit()
