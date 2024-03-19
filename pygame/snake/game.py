import pygame, sys

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
SNAKE_SPEED = 10


def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SNAKE")
    return screen

def draw_elements(screen,snake):
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, SNAKE_COLOR, snake)

    pygame.display.flip()


def main():
    screen = initialize_game()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, FONT_SIZE)

    # Snake
    snake = pygame.Rect(50, SCREEN_HEIGHT // 2 - SNAKE_WIDTH // 2, SNAKE_WIDTH, SNAKE_WIDTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_elements(screen, snake)


if __name__ == "__main__":
    main()