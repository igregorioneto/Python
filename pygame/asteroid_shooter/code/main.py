import pygame, sys, os

# Pygame Init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 640
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# Ship
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
# ship_rotate = pygame.transform.rotate(ship_surf, -45)
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# Laser
laser_surf = pygame.image.load('graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)

# Background
bg_surf = pygame.image.load('graphics/background.png').convert_alpha()

# Font
font = pygame.font.Font('graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255, 255, 255))
text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 80))

while True:
    # Events
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(120) / 1000

    # updates
    ship_rect.center = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        print(ship_rect.center)

    laser_rect.y -= round(200 * dt)

    # Drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf, (0,0))    
    
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255,255,255), text_rect.inflate(30,30), width=8, border_radius=5)

    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(ship_surf, ship_rect)    


    # draw the final frame
    pygame.display.update()