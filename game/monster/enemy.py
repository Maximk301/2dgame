import pygame
from pygame.locals import *
import os
import random

class enemy(object):
    walkRight = [pygame.image.load('monster/animation/Attackright1.png'), pygame.image.load('monster/animation/Attackright2.png'), pygame.image.load('monster/animation/Attackright3.png'), pygame.image.load('monster/animation/Attackright4.png'), pygame.image.load('monster/animation/Attackright5.png'), pygame.image.load('monster/animation/Attackright6.png')]
    walkLeft = [pygame.image.load('monster/animation/Attackleft1.png'), pygame.image.load('monster/animation/Attackleft2.png'), pygame.image.load('monster/animation/Attackleft3.png'), pygame.image.load('monster/animation/Attackleft4.png'), pygame.image.load('monster/animation/Attackleft5.png'), pygame.image.load('monster/animation/Attackleft6.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
