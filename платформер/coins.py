from pygame import *
'''''
мы импортируем библеотеку пайгейм
'''''
import pygame


class Coins (sprite.Sprite):
   """
   мы создаем класс —  это шаблон, с помощью которого удобно описывать
   однотипные объекты. В классе соержатся свойства, правила создания
    и поведение объекта. Объект — экземпляр, созданный на основе шаблона.
     Атрибут — поле, хранящее значение.Мы создаем сласс коинс для того чтобы
     сделать в будующим монетки

     """




   def __init__(self,x,y):

     sprite.Sprite.__init__(self)

     self.image = pygame.image.load ("images/coin.png")

     self.rect = self.image.get_rect()

     self.rect.x=x
     self.rect.y=y




