import pygame, csv, os
import numpy as np

class Tileset:
    def __init__(self, file, sprite_size=(56, 56), margin=0, spacing=0):
        self.file = file
        self.size = sprite_size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()


    def load(self):

        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing
        
        
        for y in range(y0, h, dy):
            for x in range(x0, w, dx):
                tile = pygame.Surface(self.size, pygame.SRCALPHA)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'


class Tilemap:
    def __init__(self, tileset, map_csv , rect=None): #TODO statt size und dem map = np.zeroes und random zuweisungszeug, param csv, wo tiles angeordnet werden 
        #read csv
        lst = []
        with open(os.path.join(map_csv)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                lst.append([int(x) for x in row])

        self.map = np.array(lst)
        self.tileset = tileset
        

        self.image = pygame.Surface((self.tileset.size[0]*self.map.shape[1], self.tileset.size[1]*self.map.shape[0]))
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()

    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j*self.tileset.size[0], i*self.tileset.size[0]))

    def __str__(self):
        return f'{self.__class__.__name__} {self.map.shape}'    