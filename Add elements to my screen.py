import pygame


pygame.init()


window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pygame Window with Rectangle and Text')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


font = pygame.font.SysFont('Arial', 36)

# Main game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    rect_width, rect_height = 200, 100
    rect_x, rect_y = (window_width - rect_width) // 2, (window_height - rect_height) // 2
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    
    text = font.render('Hello, Pygame!', True, BLACK)
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 150))
    screen.blit(text, text_rect)

    
    pygame.display.flip()

    
    pygame.time.delay(30)


pygame.quit()
