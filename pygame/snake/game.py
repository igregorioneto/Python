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
    #pygame.draw.rect(screen, SNAKE_COLOR, snake)
    pygame.draw.rect(screen, APPLE_COLOR, apple)

    # Snake draw
    for xy in list_snake:
        snake.x = xy[0]
        snake.y = xy[1]
        pygame.draw.rect(screen, SNAKE_COLOR, snake)       

    # Fonts
    score_text = font.render(f"Points: {points}", False, FONT_COLOR)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

# Random int
def random_value(initial, value):
    return random.randint(initial,value)

# Moviment Snake
# Moviment like the original game
def handle_input(snake):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        snake.y -= SNAKE_SPEED
    if keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        snake.y += SNAKE_SPEED
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        snake.x -= SNAKE_SPEED
    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        snake.x += SNAKE_SPEED
    

def colision(snake, apple, sound, points):
    if snake.colliderect(apple):
        sound.play()
        points += 1
        apple.x = random_value(0, SCREEN_WIDTH - APPLE_WIDTH)
        apple.y = random_value(0, SCREEN_HEIGHT - APPLE_WIDTH)
    return points

def updating_snake(snake, list_snake):
    if snake.x < 0:
        snake.x = SCREEN_WIDTH - SNAKE_WIDTH
    if snake.x > SCREEN_WIDTH:
        snake.x = 0
    if snake.y < 0:
        snake.y = SCREEN_HEIGHT - SNAKE_WIDTH
    if snake.y > SCREEN_HEIGHT:
        snake.y = 0

    list_snake.append([snake.x, snake.y])
    return list_snake
    

def main():
    screen, coin = initialize_game()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, FONT_SIZE)

    points = 0
    list_snake = []

    # Snake
    snake = pygame.Rect(50, SCREEN_HEIGHT // 2 - SNAKE_WIDTH // 2, SNAKE_WIDTH, SNAKE_WIDTH)
    # Apple
    apple = pygame.Rect(random_value(0,SCREEN_WIDTH - APPLE_WIDTH), random_value(0,SCREEN_HEIGHT - APPLE_WIDTH), APPLE_WIDTH, APPLE_WIDTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_elements(screen, snake, apple, font, points, list_snake)

        handle_input(snake)

        points = colision(snake, apple, coin, points)

        list_snake = updating_snake(snake, list_snake)

        clock.tick(60)


if __name__ == "__main__":
    main()