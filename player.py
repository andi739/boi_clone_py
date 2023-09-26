import pygame
from tiles import Tileset

class Player:
    def __init__(self, tileset : Tileset, screen : pygame.Surface, sprite_size=(56, 56), start_pos = (56,56)):
        self.tileset = tileset
        self.screen = screen
        self.pos_x, self.pos_y = start_pos
        self.size_x, self.size_y = sprite_size

        #TODO erstma nur unarmed
        self.map = {'north_unarmed':0,'south_unarmed':1}
        self.current_map_index = self.map['north_unarmed']
    def render(self):
        tile = self.tileset.tiles[self.current_map_index]
        self.screen.blit(tile, (self.pos_x, self.pos_y))

    def check_collision(self, colidable_objects = None):
        pass#TODO

    def move_up(self):
        self.check_collision()
        self.pos_y -= self.size_y#TODO check ob y-achse nach oben oder untern geht
        self.current_map_index = self.map['north_unarmed']
        self.render()

    def move_down(self):
        self.check_collision()
        self.pos_y += self.size_y
        self.current_map_index = self.map['south_unarmed']
        self.render()

    def move_left(self):
        self.check_collision()
        self.pos_x -= self.size_x
        self.current_map_index = self.map['north_unarmed']
        self.render()

    def move_right(self):
        self.check_collision()
        self.pos_x += self.size_x
        self.current_map_index = self.map['south_unarmed']
        self.render()