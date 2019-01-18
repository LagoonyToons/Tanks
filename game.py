import pygame as pg
from player import *

class Game:
    def __init__(self, screen):
        self.loadImages()
        self.clock = pg.time.Clock()
        self.player = Tank(self.tankImage, 1)
        self.player2 = Tank(self.tankImage, 0)
        self.screen = screen

        self.wall = Wall(self.wallImage, SCREEN_X/2, SCREEN_Y/2)

        self.players = [self.player, self.player2]
        self.bullets = []
        self.walls = [self.wall]

        self.gameloop()

    def gameloop(self):
        while True:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return
            for wall in self.walls:
                wall.update(self.screen)
            self.player.update(self.screen, self.walls)
            self.player2.update(self.screen, self.walls)
            #self.screen.blit(self.player.image, (self.player.x, self.player.y))
            #self.screen.blit(self.player2.image, (self.player2.x, self.player2.y))
            pg.display.update()
            self.screen.fill(pg.Color("black"))
            self.clock.tick(60)

    def loadImages(self):
        self.bulletImage = pg.transform.scale(pg.image.load("bullet.png"), (25, 25))
        self.tankImage = pg.transform.scale(pg.image.load("tank.png"), (80, 80))
        self.wallImage = pg.transform.scale(pg.image.load("wall.jpg"), (120, 20))
