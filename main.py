import pygame as pg
import sys
from game import *
from options import *
pg.init()
#pg.mixer.init()

#defined in options
#SCREEN_X, SCREEN_Y = (1200, 700)

pg.display.set_caption("Tanks")
#screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), pg.FULLSCREEN)
#pg.mouse.set_visible(False)
screen = pg.display.set_mode((SCREEN_X, SCREEN_Y))
# while True:
#     events = pg.event.get()
#     for event in events:
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()
Game(screen)
pg.quit()
sys.exit()