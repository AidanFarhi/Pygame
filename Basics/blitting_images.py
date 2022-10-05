import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Blitting images!")

# Create images... returns a Surface object with the image drawn on it.
# We can then get the rect of the surface and use the rect to position the image.
dragon_left_image = pygame.image.load('images/dragon.png')  # surface object
dragon_left_rect = dragon_left_image.get_rect()                  # rect object
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load('images/dragon.png')
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

running = True
while running:

    pygame.display.update()
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
