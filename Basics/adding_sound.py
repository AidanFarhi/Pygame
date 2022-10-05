import pygame

pygame.init()

HEIGHT = WIDTH = 500

display_surface = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Adding sound")

# load sound effects
sound_1 = pygame.mixer.Sound('sounds/blip.wav')
sound_2 = pygame.mixer.Sound('sounds/hit.wav')
music = pygame.mixer.music.load('sounds/music.wav')

running = True
while running:
    sound_1.play()
    pygame.time.delay(1000)
    sound_2.play()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
