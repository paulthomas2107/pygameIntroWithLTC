import sys

import pygame

# Init PyGame
pygame.init()

# Create window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello Paul !")

# Main Game Loop
running = True
while running:
    # Loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# End  Game Loop
pygame.quit()
sys.exit()