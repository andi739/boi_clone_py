import pygame, os
from pygame.locals import *
import numpy as np
from tiles import Tilemap, Tileset
from player import Player

file = 'resources/sprites/tileset.png'

print(__file__)
path = os.path.abspath(__file__)
dir = os.path.dirname(path)

base = os.path.basename(path)
print(base)

root, ext = os.path.splitext(path)
print(root)

class Game:
    W = 1200
    H = 800
    SIZE = W, H

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption('BOI Clone')
        self.running = True

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.tilemap_level = Tilemap(Tileset(file), 'demo_level.csv')
        
        self.player = Player(Tileset('resources/sprites/tileset_characters.png'),self.screen)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                elif event.type == KEYDOWN:
                    if event.key == K_w:
                        self.player.move_up()
                    if event.key == K_s:
                        self.player.move_down()
                    if event.key == K_d:
                        self.player.move_right()
                    if event.key == K_a:
                        self.player.move_left()
                
            self.tilemap_level.render()
            self.screen.blit(self.tilemap_level.image, self.tilemap_level.rect)
            self.player.render()
            pygame.display.update()

            self.dt = self.clock.tick(60)
            
        pygame.quit()

game = Game()
game.run()