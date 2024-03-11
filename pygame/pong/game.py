import pygame, sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

player1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.y += PADDLE_SPEED

    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
        player2.y += PADDLE_SPEED

    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.top >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, (255,255,255), player1)
    pygame.draw.rect(screen, (255,255,255), player2)
    pygame.draw.ellipse(screen, (255,255,255), ball)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)