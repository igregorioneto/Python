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

point_player1 = 0
point_player2 = 0

winner = ""

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

font = pygame.font.Font(None, 36)

player1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

def show_go_screen(winner):
    # Criar uma superfície de cor de fundo
    background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_surface.fill((255,255,255))

    # Desenhando a superfície na tela.
    screen.blit(background_surface, (0,0))

    # Verificar o vencedor
    if winner == "Player 1":
        winner_text = "Player 1 Wins!"
    elif winner == "Player 2":
        winner_text = "Player 2 Wins!"
    else:
        winner_text = "It's a Tie!"
        
    # Rendezirar Texto do Vencedor
    text_surface = font.render(winner_text, True, (0,0,0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text_surface, text_rect)

    # Renderizar o texto para jogar novamente
    replay_surface = font.render("Press space bar to play again", True, (0,0,0))
    replay_rect = replay_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
    screen.blit(replay_surface, replay_rect)

    pygame.display.flip()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True

        pygame.time.Clock().tick(60)


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

    if ball.left <= 0:
        point_player2 += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        print(f"Ponto Player 2: {point_player2}")
    elif ball.right >= SCREEN_WIDTH:
        point_player1 += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        print(f"Ponto Player 1: {point_player1}")

    if point_player1 == 3:
        # pygame.quit()
        winner = "Player 1"
        show_go_screen(winner)
    if point_player2 == 3:
        # pygame.quit()
        winner = "Player 2"
        show_go_screen(winner=winner)

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    screen.fill(BG_COLOR)

    score_text = font.render(f"Player 1: {point_player1} Player2: {point_player2}", True, (255,255,255))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.draw.rect(screen, (255,255,255), player1)
    pygame.draw.rect(screen, (255,255,255), player2)
    pygame.draw.ellipse(screen, (255,255,255), ball)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)