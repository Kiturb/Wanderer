import pygame
from pygame.sprite import Sprite
import math
from random import choice

"""A class to represent a single skeleton"""


class Skeleton(Sprite):
    """Initialize the skeleton and set its starting position."""

    def __init__(self):
        super().__init__()

        # Load the skeleton image and set its rect attribute.
        self.image = pygame.image.load('images/skeleton.gif')
        self.rect = self.image.get_rect()

    def create_random(self, floor_tiles):
        # Start each new skeleton somewhere random on floor type tiles.
        position = choice(floor_tiles)
        floor_tiles.remove(position)
        self.rect.x = (position - 1) % 10 * 72
        self.rect.y = math.floor((position - 1) / 10) * 72
        return floor_tiles

    def update_skeleton_stats(self):
        print("cool")

    def update(self, skeletons):
        skeletons.remove(self)
