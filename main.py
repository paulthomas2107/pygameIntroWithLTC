import sys

import pygame

# Init PyGame
pygame.init()

# Create window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello Paul !")

# Images
arrow_left = pygame.image.load("graphics/previous.png")
arrow_left_rect = arrow_left.get_rect()
arrow_left_rect.topleft = (0, 0)

arrow_right = pygame.image.load("graphics/next.png")
arrow_right_rect = arrow_right.get_rect()
arrow_right_rect.topright = (WINDOW_WIDTH, 0)

arrow_right_2 = pygame.image.load("graphics/next.png")
arrow_right_rect_2 = arrow_right_2.get_rect()
arrow_right_rect_2.topright = (WINDOW_WIDTH, 0)
arrow_right_rect_2.centerx = WINDOW_WIDTH // 2
arrow_right_rect_2.bottom = WINDOW_HEIGHT


# RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
DARK_GREEN = (10, 50, 10)

# Game vars
VELOCITY = 10

# BG Display
display_surface.fill(BLACK)


# Draw shape
def drawBasicShapes():
    pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
    pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)
    pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 200, 6)
    pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 195, 0)
    pygame.draw.rect(display_surface, MAGENTA, (10, 10, 150, 150))
    pygame.draw.rect(display_surface, CYAN, (500, 100, 50, 100))


def blittingImages():
    # Image
    display_surface.blit(arrow_left, arrow_left_rect)
    display_surface.blit(arrow_right, arrow_right_rect)
    pygame.draw.line(display_surface, WHITE, (0, 75), (WINDOW_WIDTH, 75), 4)


def moreImages():

    display_surface.blit(arrow_right_2, arrow_right_rect_2)


def showFonts():
    # Text
    fonts = pygame.font.get_fonts()
    for _ in fonts:
        print(_)


def useCustomFont():
    # Set Fonts
    system_font = pygame.font.SysFont('calibri', 64)
    custom_font = pygame.font.Font('./fonts/AttackGraffiti.ttf', 32)
    system_text = system_font.render("Dragons Rule !", True, GREEN, DARK_GREEN)
    system_text_rect = system_text.get_rect()
    system_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    custom_text = custom_font.render("Move The Dragon Soon...", True, GREEN)
    custom_text_rect = custom_text.get_rect()
    custom_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)
    # Blit to screen
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)


def useSounds():
    sound_1 = pygame.mixer.Sound('sounds/zap.wav')
    sound_2 = pygame.mixer.Sound('sounds/explosion.wav')

    sound_1.play(loops=1)
    pygame.time.delay(1000)
    sound_2.play(loops=1)
    pygame.time.delay(1000)

    sound_2.set_volume(.1)
    sound_2.play(loops=1)
    pygame.time.delay(1000)

    # Background music
    pygame.mixer.music.load("sounds/theme.wav")
    pygame.mixer.music.play(1, 0.0)
    pygame.mixer.stop()


# useSounds()

# Main Game Loop
running = True
while running:
    # Loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                arrow_right_2 = pygame.image.load("graphics/next.png")
                arrow_right_rect_2.x += VELOCITY
            if event.key == pygame.K_LEFT:
                arrow_right_2 = pygame.image.load("graphics/previous.png")
                arrow_right_rect_2.x -= VELOCITY
            if event.key == pygame.K_UP:
                arrow_right_rect_2.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                arrow_right_rect_2.y += VELOCITY

    display_surface.fill(BLACK)

    # Do stuff
    # drawBasicShapes()
    blittingImages()
    useCustomFont()
    moreImages()

    # Update display
    pygame.display.update()
# End  Game Loop
pygame.quit()
sys.exit()
