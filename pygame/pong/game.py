import pygame, sys

# Constantes do Jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    return screen

def draw_elements(screen, player1, player2, ball, point_player1, point_player2, font):
    screen.fill(BG_COLOR)
    # Desenhando jogadores e bola
    pygame.draw.rect(screen, (255,255,255), player1)
    pygame.draw.rect(screen, (255,255,255), player2)
    pygame.draw.ellipse(screen, (255,255,255), ball)
    # Desenhando pontuação
    score_text = font.render(f"Player 1: {point_player1} Player2: {point_player2}", True, (255,255,255))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

def handle_input(player1, player2):
    keys = pygame.key.get_pressed()
    # Movimentação Player 1
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.y += PADDLE_SPEED

    # Movimentação Player 2
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
        player2.y += PADDLE_SPEED

def update_ball(ball, ball_speed_x, ball_speed_y, point_player1, point_player2, winner, player1, player2):
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colidindo com os Players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Colisões com as bordas da tela
    if ball.top <= 0 or ball.top >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <=0:
        point_player2 += 1
        reset_ball(ball)
    if ball.right >= SCREEN_WIDTH:
        point_player1 += 1
        reset_ball(ball)

    # Verifica vencedor
    if point_player1 == 3 or point_player2 == 3:
        winner = "Player 1" if point_player1 == 3 else "Player 2"

    return ball_speed_x, ball_speed_y, point_player1, point_player2, winner

def reset_ball(ball):
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


def show_go_screen(screen, font, winner):
    # Criar uma superfície de cor de fundo
    background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_surface.fill((255,255,255))

    # Desenhando a superfície na tela.
    screen.blit(background_surface, (0,0))

    # Texto do Vencedor
    winner_surface = font.render(f"{winner} Wins!", True, (0,0,0))
    text_rect = winner_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2))
    screen.blit(winner_surface, text_rect)

    # Texto para jogar novamente
    replay_surface = font.render("Press space bar to play again", True, (0,0,0))
    replay_rect = replay_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
    screen.blit(replay_surface, replay_rect)

    pygame.display.flip()

    # Loop para pressionar a tecla de espaço
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                
def main():
    screen = initialize_game()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    player1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    player2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y
    point_player1 = 0
    point_player2 = 0
    winner = "" 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        handle_input(player1, player2)

        ball_speed_x, ball_speed_y, point_player1, point_player2, winner = update_ball(ball, ball_speed_x, ball_speed_y, point_player1, point_player2, winner, player1, player2)
    
        draw_elements(screen, player1, player2, ball, point_player1, point_player2, font)

        if winner:
            show_go_screen(screen, font, winner)
            point_player1 = 0
            point_player2 = 0
            reset_ball(ball)
            winner = ""

        clock.tick(60)


if __name__ == "__main__":
    main()