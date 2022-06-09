import pygame as pg
from settings import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self, x_loc, y_loc):
        #initialize sprite class
        pg.sprite.Sprite.__init__(self)

        #create player rectangle
        self.image = pg.image.load("images/player1.png")

        #get/set rectangles coords
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc


        #set player speed
        self.x_velo = 0
        self.y_velo = 0

    def update(self):
        self.rect.x += self.x_velo
        self.rect.y += self.y_velo

        # rect.top, rect.right, rect.bottom, rect.left, rect.center
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 2*P_SIZE:
            self.rect.left = 2*P_SIZE
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.y <= 65:
            self.rect.y = HEIGHT - 2*P_SIZE

class Enemy(pg.sprite.Sprite):
    def __init__(self, x_loc, y_loc, img):
        #initialize sprite class
        pg.sprite.Sprite.__init__(self)

        #create player rectangle
        # self.image = pg.Surface((E_SIZE, E_SIZE))
        self.image = img
        # self.image.fill(RED)

        #get/set rectangles coords
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc


        #set player speed
        self.y_velo = random.choice([2, 3, 4, 5])

    def update(self):
        self.rect.y += self.y_velo

        if self.rect.top >= HEIGHT:
            self.kill()