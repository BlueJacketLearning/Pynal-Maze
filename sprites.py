import pygame
from config import *

# player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)

        self.start_x = x * TILESIZE
        self.start_y = y * TILESIZE

        self.rect = self.image.get_rect(topleft=(self.start_x, self.start_y))

        self.x_change = 0
        self.y_change = 0

# player movement and colision
    def update(self):
        self.movement()

        self.rect.x += self.x_change
        if self.collide_blocks():
            self.reset_position()

        self.rect.y += self.y_change
        if self.collide_blocks():
            self.reset_position()

        self.collide_goal()

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.x_change = PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.y_change = -PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.y_change = PLAYER_SPEED

#when player collides with the wall it resets
    def collide_blocks(self):
        return pygame.sprite.spritecollide(self, self.game.blocks, False)

    def collide_goal(self):
        if pygame.sprite.spritecollide(self, self.game.goals, False):
            self.game.win()

    def reset_position(self):
        self.rect.topleft = (self.start_x, self.start_y)


# sprites for block / wall and the goal
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect(topleft=(x * TILESIZE, y * TILESIZE))


class Goal(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.goals
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect(topleft=(x * TILESIZE, y * TILESIZE))
