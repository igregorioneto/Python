import pygame, sys, os
from random import randint, uniform

def laser_update(laser_list, speed = 300):
    for laser in laser_list:
        laser.y -= round(speed * dt)
        if laser.bottom < 0:
            laser_list.remove(laser)

def laser_timer(can_shoot, duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

def meteor_update(meteor_list, speed = 300):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)

def display_score():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255,255,255), text_rect.inflate(30,30), width=8, border_radius=5)

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
laser_list = []

# Background
bg_surf = pygame.image.load('graphics/background.png').convert_alpha()

# Font
font = pygame.font.Font('graphics/subatomic.ttf', 50)

can_shoot = True
shoot_time = None

meteor_surf = pygame.image.load('graphics/meteor.png').convert_alpha()
meteor_list = []

music = pygame.mixer.init('sounds/music.wav')
laser_sound = pygame.mixer.Sound('sounds/laser.ogg')
explosion = pygame.mixer.Sound('sounds/explosion.wav')

can_meteor = True
meteor_time = None
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

while True:
    # Events
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

            # timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer:
           x_pos = randint(-100, WINDOW_WIDTH+100)
           y_pos = randint(-100,-50)
           meteor_rect = meteor_surf.get_rect(center = (x_pos,y_pos))
           direction = pygame.math.Vector2(uniform(-0.5,0.5), 1)
           meteor_list.append((meteor_rect, direction))

    dt = clock.tick(120) / 1000

    # updates
    ship_rect.center = pygame.mouse.get_pos()

    laser_update(laser_list)
    meteor_update(meteor_list)
    can_shoot = laser_timer(can_shoot, 400)

    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()  

    for laser_react in laser_list:
        for meteor_tuple in meteor_list:
            meteor_rect = meteor_tuple[0]
            if laser_react.colliderect(meteor_rect):
                laser_list.remove(laser_rect)
                meteor_list.remove(meteor_tuple)
    

    # Drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf, (0,0))    
    
    display_score()

    for laser in laser_list:
        display_surface.blit(laser_surf, laser)

    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf, meteor_tuple[0])    

    display_surface.blit(ship_surf, ship_rect)    

    # draw the final frame
    pygame.display.update()