import pygame
pygame.init()

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)



game_over = True

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Toby's Block Game UwU")

clock = pygame.time.Clock()

while game_over:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              game_over = False # Flag that we are done so we can exit the while loop

        screen.fill(white)
        pygame.draw.rect(screen, red, [55, 200, 100, 70],0)

        pygame.display.flip()

        pygame.display.update()
        clock.tick(60)


pygame.quit()

