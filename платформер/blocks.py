from pygame import *

'''''
мы импортируем библиотеку пайгейм 
'''''

PLATFORM_WIDTH =32
PLATFORM_HEIGHT=32
PLATFORM_COLOR= "#FF6262"
с
class Platform (sprite.Sprite):
    """
    мы создаем класс Platform 
    """
    def __init__ (self,x,y):
        sprite.Sprite.__init__(self)
        self.image=Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect=Rect(x,y,PLATFORM_WIDTH,PLATFORM_HEIGHT)

        '''''
        мы создаем функцию self которая self — это ссылка на текущий 
        экземпляр класса. Это способ обращения к атрибутам и методам класса
         изнутри самого класса
        '''''
