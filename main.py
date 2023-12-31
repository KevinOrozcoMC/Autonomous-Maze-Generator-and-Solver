import pygame as pg
import sys

from map import *
from player import *
from settings import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *


class Game:
    def __init__(self):
        # render screen and clock for frame rate
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        # get delta of time
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        # instance of map class
        self.map = Map(self)
        # instance of player
        self.player = Player(self)

        self.object_renderer = ObjectRenderer(self)
        # instance of ray casting method
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        # instance of sprite object
        # self.static_sprite = SpriteObject(self)
        # instance of animated sprites
        # self.animated_sprite = AnimatedSprite(self)

    # update screen and display information
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        # self.static_sprite.update()
        # self.animated_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(str(int(self.clock.get_fps())))


    def draw(self):
        # make a black screen
         self.screen.fill('black')  # no longer needed after draw_background method
         self.object_renderer.draw()
        # draw map
        # self.map.draw()
        # draw player
        # self.player.draw()


    # event handler
    def check_events(self):
        for event in pg.event.get():
            # if player hits the X at top right or presses escape key exit the game
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    # game loop calling update and draw methods
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
