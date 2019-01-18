import pygame as pg
from options import *
class Tank:
    def __init__(self, image, operator):
        self.image = image
        self.x = self.y = self.oldx = self.oldy =100
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 3
        self.operator = operator
        self.bulletTimer = 15
        self.rotation = self.old_rotation = 0
        self.transformedImage = pg.transform.rotate(self.image, self.rotation)
    def update(self, screen, walls):
        self.old_rotation = self.rotation
        self.oldx = self.x
        self.oldy = self.y
        #self.bulletTimer += 1
        pressed = pg.key.get_pressed()
        if self.operator == 1:
            if not self.x <= 0 and pressed[pg.K_LEFT]:
                self.x -= self.speed
            elif not self.x > SCREEN_X-80 and pressed[pg.K_RIGHT]:
                self.x += self.speed
            if not self.y <= 0 and pressed[pg.K_UP]:
                self.y -= self.speed
            elif not self.y > SCREEN_Y-80 and pressed[pg.K_DOWN]:
                self.y += self.speed
           # if self.bulletTimer >= 30 and pressed[pg.K_SPACE]:
               # self.fireBullet(self.direction)
        elif self.operator == 0:
            if not self.x <= 0 and pressed[pg.K_a]:
                self.x -= self.speed
            elif not self.x > SCREEN_X-80 and pressed[pg.K_d]:
                self.x += self.speed
            if not self.y <= 0 and pressed[pg.K_w]:
                self.y -= self.speed
            elif not self.y > SCREEN_Y-80 and pressed[pg.K_s]:
                self.y += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        self.findDirection(pressed)
        for wall in walls:
           if self.rect.colliderect(wall.rect):
               self.x = self.oldx
               self.y = self.oldy
               break
        if self.rotation != self.old_rotation:
            self.transformedImage = pg.transform.rotate(self.image, self.rotation)
        screen.blit(self.transformedImage, (self.x, self.y))    
        
    def findDirection(self, pressed):
        if self.operator == 1:
            if pressed[pg.K_LEFT]:
                self.rotation = 180
                if pressed[pg.K_UP]:
                    self.rotation -= 45
                elif pressed[pg.K_DOWN]:
                    self.rotation += 45
            elif pressed[pg.K_RIGHT]:
                self.rotation = 0
                if pressed[pg.K_UP]:
                    self.rotation += 45
                elif pressed[pg.K_DOWN]:
                    self.rotation -= 45
            else:
                if pressed[pg.K_UP]:
                    self.rotation = 90
                elif pressed[pg.K_DOWN]:
                    self.rotation = 270
        elif self.operator == 0:
            if pressed[pg.K_a]:
                self.rotation = 180
                if pressed[pg.K_w]:
                    self.rotation -= 45
                elif pressed[pg.K_s]:
                    self.rotation += 45
            elif pressed[pg.K_d]:
                self.rotation = 0
                if pressed[pg.K_w]:
                    self.rotation += 45
                elif pressed[pg.K_s]:
                    self.rotation -= 45
            else:
                if pressed[pg.K_w]:
                    self.rotation = 90
                elif pressed[pg.K_s]:
                    self.rotation = 270
class Bullet:
    def __init__(self, x, y, x_speed, y_speed, image):
        self.image = image
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Wall:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))

