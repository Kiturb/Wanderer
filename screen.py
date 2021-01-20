import pygame

"""A class to store all settings for the screen."""


class Screen:
    """Initialize the game's screen."""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Wanderer by Kitti Urbán")
        self.full = pygame.display.set_mode((720, 720))
        self.background = pygame.image.load('images/full-map.png')
        self.wall_list = [4, 14, 16, 18, 19, 22, 23, 24, 26, 28, 29, 36, 41, 42, 43, 44, 46, 47, 48,
                          49, 52, 54, 62, 64, 66, 67, 69, 76, 77, 79, 82, 83, 84, 89, 94, 96, 97]
        self.rect = self.full.get_rect()


screen = Screen()
