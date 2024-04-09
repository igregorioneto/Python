import pygame, sys, os

# Pygame Init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 640
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# Ship
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# Laser
laser_surf = pygame.image.load('graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)

# Background
bg_surf = pygame.image.load('graphics/background.png').convert_alpha()

# Font
font = pygame.font.Font('graphics/subatomic.ttf', 50)
font_surf = font.render('Space', True, (255, 255, 255))
font_rect = font_surf.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 80))

while True:
    # Events
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(120)

    # updates
    ship_rect.center = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        print(ship_rect.center)

    laser_rect.y -= 4

    # Drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf, (0,0))    
    display_surface.blit(ship_surf, ship_rect)    
    display_surface.blit(font_surf, font_rect)
    display_surface.blit(laser_surf, laser_rect)

    # draw the final frame
    pygame.display.update()