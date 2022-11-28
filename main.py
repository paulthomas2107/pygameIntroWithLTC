import sys

import pygame

# Init PyGame
pygame.init()

# Create window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello Paul !")

# RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255,255)
MAGENTA = (255, 0, 255)

# BG Display
display_surface.fill(BLUE)


# Draw shape
def drawBasicShapes():
    pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
    pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)
    pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 200, 6)
    pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 195, 0)
    pygame.draw.rect(display_surface, MAGENTA, (10, 10, 150, 150))
    pygame.draw.rect(display_surface, CYAN, (500, 100, 50, 100))


# Main Game Loop
running = True
while running:
    # Loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Do stuff
    drawBasicShapes()

    # Update display
    pygame.display.update()
# End  Game Loop
pygame.quit()
sys.exit()
