from pygame import *
import pygame


class Coins (sprite.Sprite):

     def __init__(self,x,y):

        sprite.Sprite.__init__(self)

        self.image = pygame.image.load ("images/coin.png")

        self.rect = self.image.get_rect()

        self.rect.x=x
        self.rect.y=y




