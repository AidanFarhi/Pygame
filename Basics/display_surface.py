import pygame

# set game constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# initialize pygame
pygame.init()

# create game surface and set caption
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World!")

# the main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
