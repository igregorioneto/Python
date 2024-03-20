import pygame, sys, random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND = (0,0,0)
FONT_COLOR = (255,255,255)
FONT_SIZE = 36
SNAKE_COLOR = (0,255,0)
APPLE_COLOR = (255,0,0)
SNAKE_WIDTH = 20
APPLE_WIDTH = 20
SNAKE_SPEED = 5

# Initialize Game
def initialize_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SNAKE")
    coin = pygame.mixer.Sound('assets/smw_coin.wav')
    return screen, coin

# Draw elements
def draw_elements(screen, snake, apple, font, points, list_snake):
    screen.fill(BACKGROUND)
    # Game    
    pygame.draw.rect(screen, SNAKE_COLOR, snake)
    pygame.draw.rect(screen, APPLE_COLOR, apple)   

    # Updating Snake
    updating_snake(screen, list_snake) 

    # Fonts
    score_text = font.render(f"Points: {points}", False, FONT_COLOR)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

# Game Over
def game_over(screen, font, points):   
    screen.fill(BACKGROUND)
    game_over_text = font.render(f"Game Over, You points: {points}, press R for reload game.", False, FONT_COLOR)       

    game_over_displayed = False

    while True:        
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:                    
                    return
                
        pygame.display.update()

        if not game_over_displayed:
            pygame.display.flip()
            game_over_displayed = True


# Random int
def random_value(initial, value):
    return random.randint(initial,value)

# Moviment Snake
# Moviment like the original game
def handle_input(snake, control_x, control_y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and control_x != 0:
        control_x = 0
        control_y = -SNAKE_SPEED
    if keys[pygame.K_DOWN] and control_x != 0:
        control_x = 0
        control_y = +SNAKE_SPEED
    if keys[pygame.K_LEFT] and control_y != 0:
        control_x = -SNAKE_SPEED
        control_y = 0
    if keys[pygame.K_RIGHT] and control_y != 0:
        control_x = +SNAKE_SPEED
        control_y = 0
    snake.x += control_x
    snake.y += control_y 
    return control_x, control_y
    

def colision(snake, apple, sound, points, comprimento_cobra):
    if snake.colliderect(apple):
        sound.play()
        points += 1
        apple.x = random_value(0, SCREEN_WIDTH - APPLE_WIDTH)
        apple.y = random_value(0, SCREEN_HEIGHT - APPLE_WIDTH)
        comprimento_cobra += 1
    return points, comprimento_cobra

def verify_snake_bords(snake, list_snake, comprimento_cobra):
    if snake.x < 0:
        snake.x = SCREEN_WIDTH - SNAKE_WIDTH
    if snake.x > SCREEN_WIDTH:
        snake.x = 0
    if snake.y < 0:
        snake.y = SCREEN_HEIGHT - SNAKE_WIDTH
    if snake.y > SCREEN_HEIGHT:
        snake.y = 0 

    if len(list_snake) > comprimento_cobra:
        del list_snake[0]

    return list_snake

def updating_snake(screen, list_snake):
    # Snake draw
    for xy in list_snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (xy[0], xy[1], SNAKE_WIDTH, SNAKE_WIDTH))   

def game_restart(points, comprimento_cobra, list_snake, list_head_snake, control_x, control_y):
    points = 0
    comprimento_cobra = 0
    list_snake = []
    list_head_snake = []
    control_x = SNAKE_SPEED
    control_y = 0
    return points, comprimento_cobra, list_snake, list_head_snake, control_x, control_y

def main():
    screen, coin = initialize_game()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, FONT_SIZE)

    points = 0
    comprimento_cobra = 0
    list_snake = []

    control_x = SNAKE_SPEED
    control_y = 0

    # Snake
    snake = pygame.Rect(50, SCREEN_HEIGHT // 2 - SNAKE_WIDTH // 2, SNAKE_WIDTH, SNAKE_WIDTH)
    # Apple
    apple = pygame.Rect(random_value(0,SCREEN_WIDTH - APPLE_WIDTH), random_value(0,SCREEN_HEIGHT - APPLE_WIDTH), APPLE_WIDTH, APPLE_WIDTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Snake HEAD
        list_head_snake = []
        list_head_snake.append(snake.x)
        list_head_snake.append(snake.y)
        list_snake.append(list_head_snake)

        draw_elements(screen, snake, apple, font, points, list_snake)

        control_x, control_y = handle_input(snake, control_x, control_y)

        points, comprimento_cobra = colision(snake, apple, coin, points, comprimento_cobra)

        list_snake = verify_snake_bords(snake, list_snake, comprimento_cobra)

        if list_snake.count(list_head_snake) > 1:
            game_over(screen, font, points)
            points, comprimento_cobra, list_snake, list_head_snake, control_x, control_y = game_restart(points, comprimento_cobra, list_snake, list_head_snake, control_x, control_y)
        
        clock.tick(60)


if __name__ == "__main__":
    main()