import pygame
from random import randint

"""Track statistics for Wanderer."""


class GameStats:
    """Initialize statistics."""

    def __init__(self):
        self.reset_hero_stats()

    """Initialize statistics that can change during the game."""

    def reset_hero_stats(self):
        d6 = randint(1, 6)
        self.level = 1
        self.max_hp = 20 + 3 * d6
        self.current_hp = 20 + 3 * d6
        self.dp = 2 * d6
        self.sp = 5 + d6
        self.update_caption()

    def update_caption(self):
        pygame.display.set_caption(f"Wanderer by Kitti Urbán                        Hero (Level {self.level})         "
                                   f"        HP: {self.current_hp}/{self.max_hp} | DP: {self.dp} | SP: {self.sp}")


stats = GameStats()
