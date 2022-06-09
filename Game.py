########################         main.py        ########################


import pygame as pg
import sprites
from settings import *


class Game():
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        '''create all game objects, sprites, and sprite groups and call run()'''

        self.run()


    def run(self):
        '''contains main game loop'''

        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # game loop - update
        pass


    def draw(self):
        '''fill screen, draw objects, sprites to the display, and flip'''
        self.screen.fill(BLACK)

    # anything to be drawn to screen goes here

    pg.display.flip()


    def events(self):
        # game loop - events
        pass


    def show_start_screen(self):
        # screen to start game
        pass


    def show_go_screen(self):
        # screen when game over
        pass


#################################################
###                                   PLAY GAME                                            ###
#################################################

game = Game()
game.new()

# game.show_start_screen()
#
# while game.running:
#     game.new()
#     game.show_go_screen()

pg.quit()