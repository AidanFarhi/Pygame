import pygame

# constants
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
display_surface.fill(BLUE)
pygame.draw.line(display_surface, BLACK, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, BLACK, (100, 100), (250, 150), 5)
pygame.draw.circle(display_surface, RED, (300, 300), 20, 10)
pygame.draw.circle(display_surface, YELLOW, (250, 250), 100, 0)
pygame.draw.rect(display_surface, MAGENTA, (25, 25, 100, 100), 123)
pygame.display.set_caption('Drawing Objects')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
