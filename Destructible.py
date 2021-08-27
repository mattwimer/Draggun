import pygame as pg
import random as r


class Destructible:
    def __init__(self, image=None, x=0, y=0):
        if image is None:
            image = r.choice([''])
        self.surface = pg.image.load(image + '.png')
        self.rect = self.surface.get_rect(x=x, y=y)
