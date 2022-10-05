import pygame

# Constants
HEIGHT_AND_WIDTH = 600

# Colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
BLACK = (0, 0, 0)

pygame.init()

# Define font
new_york = pygame.font.SysFont('newyork', 18)

display_surface = pygame.display.set_mode((HEIGHT_AND_WIDTH, HEIGHT_AND_WIDTH))
pygame.display.set_caption('Blitting text!')

text = new_york.render('New York Font!', True, GREEN, DARK_GREEN)
text_rect = text.get_rect()
text_rect.center = (HEIGHT_AND_WIDTH // 2, HEIGHT_AND_WIDTH // 2)

running = True
while running:

    display_surface.blit(text, text_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
