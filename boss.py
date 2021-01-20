import pygame
from screen import screen
import math
from random import choice
from gamestats import stats

"""A class to represent the boss enemy"""


class Boss():
    """Initialize the boss and set its starting position."""

    def __init__(self, main_game):
        super().__init__()

        self.main_game = main_game
        # Load the boss image and set its rect attribute.
        self.image = pygame.image.load('images/boss.gif')
        self.rect = self.image.get_rect()

    def create_random(self, floor_tiles):
        # Start each new skeleton somewhere random on floor type tiles.
        position = choice(floor_tiles)
        self.rect.x = (position - 1) % 10 * 72
        self.rect.y = math.floor((position - 1) / 10) * 72
        self.alive = True

    """Draw the boss at its current location."""

    def blitme(self, hero):
        if self.alive:
            screen.full.blit(self.image, self.rect)
        else:
            self.main_game._create_skeletons_boss()
            stats.level += 1
            stats.update_caption()
            hero.face = 'down'
            hero.rect.topleft = screen.rect.topleft
            hero.position = 1

    def update(self, boss):
        self.alive = False
