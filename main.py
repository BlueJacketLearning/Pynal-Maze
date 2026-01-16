import pygame
import sys
from config import *
from sprites import *

# basic pygame settings
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Maze Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("arial", 48)
        self.small_font = pygame.font.SysFont("arial", 24)

# creates the tilemap and objects
    def create_tilemap(self):
        for y, row in enumerate(tilemap):
            for x, tile in enumerate(row):
                if tile == "B":
                    Block(self, x, y)
                if tile == "P":
                    self.player = Player(self, x, y)
                if tile == "G":
                    Goal(self, x, y)

    def new(self):
        self.state = "playing"
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.goals = pygame.sprite.LayeredUpdates()
        self.create_tilemap()

# when the player wins
    def win(self):
        self.state = "win"

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        self.clock.tick(FPS)

# end screen
    def draw_win_screen(self):
        self.screen.fill(BLACK)

        text = self.font.render("the end", True, WHITE)

        self.screen.blit(
            text, text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 20))
        )

        pygame.display.update()
        self.clock.tick(FPS)

    def main(self):
        while self.running:
            self.events()
            if self.state == "playing":
                self.update()
                self.draw()
            elif self.state == "win":
                self.draw_win_screen()

g = Game()
g.new()
g.main()

pygame.quit()
sys.exit()
