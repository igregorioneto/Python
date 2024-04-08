import pygame, sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 640
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")

# creating a surface
test_surf = pygame.Surface((400,100))

while True:
    # 1. Inputs
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. updates
    display_surface.fill((15, 140, 122))
    test_surf.fill((186, 120, 39))

    display_surface.blit(test_surf, dest=(WINDOW_WIDTH - test_surf.get_width(),0))

    # 3. show the frame
    pygame.display.update()