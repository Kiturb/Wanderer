import sys
import pygame
from screen import screen
from gamestats import stats
from settings import settings
from hero import Hero
from boss import Boss
from skeleton import Skeleton

"""Overall class to manage game assets and behavior."""


class Wanderer:
    """Initialize the game, and create game resources."""

    def __init__(self):
        self.hero = Hero()
        self.skeletons = pygame.sprite.Group()
        self._create_skeletons_boss()

    """Start the main loop for the game."""

    def run_game(self):
        # Watch for keyboard and mouse event.
        while True:
            self._check_events()
            self._update_screen()

    """Respond to keypresses and mouse events."""

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    """Update images on the screen, and flip to the new screen."""

    def _update_screen(self):
        # Redraw the screen and hero during each pass through the loop.
        screen.full.blit(screen.background, (0, 0))
        self.hero.blitme()
        # Draw the skeletons # pygame.sprite.Group.draw(self.skeletons, self.screen)
        self.skeletons.draw(screen.full)
        self.boss.blitme(self.hero)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    """Create 3 skeletons"""

    def _create_skeletons_boss(self):
        floor_tiles = [5, 6, 7, 8, 9, 10, 15, 17, 20, 25, 27, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 45, 50, 51, 53,
                       55,
                       56, 57, 58, 59, 61, 63, 65, 68, 70, 71, 72, 73, 74, 75, 78, 80, 81, 85, 86, 87, 88, 90, 91, 92,
                       93,
                       95, 98, 99, 100]
        for skeleton in range(3):
            skeleton = Skeleton()
            floor_tiles = skeleton.create_random(floor_tiles)
            self.skeletons.add(skeleton)
        self.boss = Boss(self)
        self.boss.create_random(floor_tiles)

    def attack_skeleton(self):
        self.skeleton_coll.update(self.skeletons)

    def attack_boss(self):
        self.boss.update(self.boss)

    """Respond to keypresses."""

    def _check_keydown_events(self, event):
        # Face left and move the hero to the left by one until screen edge or wall
        if event.key == pygame.K_LEFT:
            self.hero.face = 'left'
            if self.hero.rect.left > 0 and (self.hero.position - 1) not in screen.wall_list:
                self.hero.rect.x -= 72
                self.hero.position -= 1
        # Face right and move the hero to the right by one until screen edge or wall
        if event.key == pygame.K_RIGHT:
            self.hero.face = 'right'
            if self.hero.rect.right < screen.rect.right and (self.hero.position + 1) not in screen.wall_list:
                self.hero.rect.x += 72
                self.hero.position += 1
        # Face up and move the hero up by one until screen edge or wall
        if event.key == pygame.K_UP:
            self.hero.face = 'up'
            if self.hero.rect.top > 0 and (self.hero.position - 10) not in screen.wall_list:
                self.hero.rect.y -= 72
                self.hero.position -= 10
        # Face down and move the hero down by one until screen edge or wall
        if event.key == pygame.K_DOWN:
            self.hero.face = 'down'
            if self.hero.rect.bottom < screen.rect.bottom and (self.hero.position + 10) not in screen.wall_list:
                self.hero.rect.y += 72
                self.hero.position += 10
        # Attack if collision with skeleton or boss
        if event.key == pygame.K_SPACE:
            self.skeleton_coll = pygame.sprite.spritecollideany(self.hero, self.skeletons)
            if self.skeleton_coll:
                self.attack_skeleton()
            if self.hero.rect.colliderect(self.boss):  # pygame.sprite.collide_rect(sprite1, sprite2)
                self.attack_boss()
        # Quit the game
        elif event.key == pygame.K_q:
            sys.exit()


if __name__ == '__main__':
    main_game = Wanderer()
    main_game.run_game()
