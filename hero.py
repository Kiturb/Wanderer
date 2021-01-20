import pygame
from screen import screen

"""A class to manage the hero"""


class Hero:
    """Initialize the hero and set its starting position."""

    def __init__(self):

        # Load the hero images and initialize hero on top left of the screen.
        self.load_hero_images()
        self.position = 1
        self.face = 'down'
        self.rect = self.image_down.get_rect()
        self.rect.topleft = screen.rect.topleft

    """Draw the hero at its current location."""

    def blitme(self):
        if self.face == 'left':
            screen.full.blit(self.image_left, self.rect)
        elif self.face == 'right':
            screen.full.blit(self.image_right, self.rect)
        elif self.face == 'up':
            screen.full.blit(self.image_up, self.rect)
        elif self.face == 'down':
            screen.full.blit(self.image_down, self.rect)

    def load_hero_images(self):
        self.image_left = pygame.image.load('images/hero-left.gif')
        self.image_right = pygame.image.load('images/hero-right.gif')
        self.image_up = pygame.image.load('images/hero-up.gif')
        self.image_down = pygame.image.load('images/hero-down.gif')

    def update_hero_stats(self):
        pass
