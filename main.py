########################         main.py        ########################


import pygame as pg
import sprites
from settings import *
import random


class Game():
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = SCREEN        #pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = CLOCK       #pg.time.Clock()

        self.running = True
        self.player = None
        self.player_grp = None

        self.bg = pg.image.load("images/road.svg")
        self.bg = pg.transform.scale(self.bg, (WIDTH*2, HEIGHT*2))

        self.vehicles = []
        for i in range(1, 6):
            path = f"images/enemy{1}.png"
            vehicle = pg.image.load(path)
            vehicle = pg.transform.rotate(vehicle, 180)
            self.vehicles.append(vehicle)

        print(self.vehicles)

        self.crash = pg.mixer.Sound("music/jazzcrash.ogg")

        self.lives = None



    def display_score(self):
        score = MED_FONT.render(f"score: {self.score}", True, YELLOW)
        self.screen.blit(score, (60, 10))

    def new(self):
        '''create all game objects, sprites, and sprite groups and call run()'''

        #create sprite groups
        self.player_grp = pg.sprite.GroupSingle()
        self.enemy_grp = pg.sprite.Group()

        #create player object and add it to the group
        self.player = sprites.Player(WIDTH//2, HEIGHT-2*P_SIZE)
        self.player_grp.add(self.player)
        for i in range(20):
            vehicle = random.choice(self.vehicles)
            rand_x = random.randint(4*E_SIZE, WIDTH-2*E_SIZE)
            rand_y = random.randint(-400, -150)

            self.enemy = sprites.Enemy(rand_x, rand_y, vehicle)
            self.enemy_grp.add(self.enemy)

            #lives rectangles
            self.lives = []
            for i in range(lives):
                dimensions = (10, 30)
                life = pg.Surface(dimensions)
                life.fill(YELLOW)
                self.lives.append(life)

        self.score = 0

        self.run()


    def run(self):
        '''contains main game loop'''

        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def detect_collision(self):
        collisions = pg.sprite.groupcollide(self.player_grp, self.enemy_grp, True, True)
        if collisions:
            self.lives.pop()
            self.crash.play()


    def update(self):
        # game loop - update
        self.player.update()
        self.enemy_grp.update()
        self.detect_collision()

        if self.player.rect.y <= 80:
            self.score += 20000

        #respawn enemies

        if len(self.enemy_grp) < 20:
            vehicle = random.choice(self.vehicles)
            rand_x = random.randint(4*E_SIZE, WIDTH-2*E_SIZE)
            rand_y = random.randint(-400, -150)

            self.enemy = sprites.Enemy(rand_x, rand_y, vehicle)
            self.enemy_grp.add(self.enemy)

            #respawn player
        if len(self.player_grp) < 1:
            rand_x = WIDTH//2
            rand_y = HEIGHT-2*P_SIZE

            self.player = sprites.Player(rand_x, rand_y)
            self.player_grp.add(self.player)

        if len(self.lives) == 0:
            self.playing = False


    def draw(self):
        '''fill screen, draw objects, sprites to the display, and flip'''
        self.screen.fill(WHITE)

        # anything to be drawn to screen goes here

        self.screen.blit(self.bg, (0, 0))
        self.display_score()
        for index, life in enumerate(self.lives):
            location = (400 + index*20, 15)
            self.screen.blit(life, location)

        pg.draw.rect(SCREEN, BLACK, (0, 50, WIDTH, 10))
        self.player_grp.draw(SCREEN)
        self.enemy_grp.draw(SCREEN)

        pg.display.flip()


    def events(self):
        # game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.player.x_velo = 5
                if event.key == pg.K_LEFT:
                    self.player.x_velo = -5
                if event.key == pg.K_UP:
                    self.player.y_velo = -5
                if event.key == pg.K_DOWN:
                    self.player.y_velo = 5
            if event.type == pg.KEYUP:
                self.player.x_velo = 0
                self.player.y_velo = 0


    def show_start_screen(self):
        # screen to start game
        pg.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        clock = pg.time.Clock()
        running = True

        title = MED_FONT.render(f"         PRESS SPACE TO START", True, YELLOW)

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        running = False

            screen.fill(BLACK)
            screen.blit(title, (60, 200))
            pg.display.flip()


    def show_go_screen(self):
        # screen when game over
        pg.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        clock = pg.time.Clock()
        running = True

        title = MED_FONT.render(f"PRESS SPACE TO START A NEW GAME\n"
                                f"ALSO BTW IF YOU PRESS Q THE GAME QUITS", True, YELLOW)

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        running = False
                    elif event.key == pg.K_q:
                        quit()

            screen.fill(BLACK)

            screen.blit(title, (25, 200))

            pg.display.flip()


#################################################
###                                   PLAY GAME                                            ###
#################################################

game = Game()

game.show_start_screen()
#
while game.running:
    game.new()
    game.show_go_screen()

pg.quit()