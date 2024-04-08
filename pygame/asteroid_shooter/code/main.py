import pygame, sys, os

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 640
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")

# creating a surface
# test_surf = pygame.Surface((400,100))
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
bg_surf = pygame.image.load('graphics/background.png').convert_alpha()

# Font
font = pygame.font.Font('graphics/subatomic.ttf', 50)
font_surf = font.render('Space', True, (255, 255, 255))

while True:
    # 1. Inputs
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. updates
    display_surface.fill((0, 0, 0))
    # test_surf.fill((186, 120, 39))
    display_surface.blit(bg_surf, (0,0))
    display_surface.blit(ship_surf, (300,500))
    display_surface.blit(font_surf, (WINDOW_WIDTH // 2 - font_surf.get_width() // 2, 500))

    # display_surface.blit(test_surf, dest=(WINDOW_WIDTH - test_surf.get_width(),0))

    # 3. show the frame
    pygame.display.update()