import pygame

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)

    # start the main loop for the game.
    while true:
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()

    while true:
        for event in pygame.event.get():
            sys.exit()

        pygame.display.flip()


run_game()
