import pygame
import sys

# Contantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NODE_RADIUS = 20
NODE_COLOR = (255, 255, 255)
LINE_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 24

# Classe para representar o nó na lista
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Classe para representar a lista
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def draw(self, screen):
        current = self.head
        x = 50
        y = SCREEN_HEIGHT // 2
        while current:
            pygame.draw.circle(screen, NODE_COLOR, (x, y), NODE_RADIUS)
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render(str(current.value), True, (0,0,0))
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect.topleft)
            if current.next:
                pygame.draw.line(screen, LINE_COLOR, (x + NODE_RADIUS, y), (x + 2 * NODE_RADIUS, y))
            x += 3 * NODE_RADIUS
            current = current.next


# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("LinkedList With Pygame")
    clock = pygame.time.Clock()

    linked_list = LinkedList()
    input_text = ""
    linked_list.insert(1)
    #linked_list.insert(2)
    #linked_list.insert(3)
    #linked_list.insert(4)
    #linked_list.insert(5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #value = input("Digite o valor para adicionar: ")
                    try:
                        value = int(input_text)
                        linked_list.insert(value)
                        input_text = ""
                    except ValueError:
                        print("Valor inválido. Por favor, insira o número inteiro.")
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(BACKGROUND_COLOR)
        linked_list.draw(screen)

        font = pygame.font.Font(None, FONT_SIZE)
        input_surface = font.render(input_text, True, FONT_COLOR)
        screen.blit(input_surface, (50,50))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()