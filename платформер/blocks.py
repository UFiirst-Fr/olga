from pygame import *

'''''
мы импортируем библиотеку пайгейм 
'''''

PLATFORM_WIDTH =32
PLATFORM_HEIGHT=32
PLATFORM_COLOR= "#FF6262"

class Platform (sprite.Sprite):
    """
    мы создаем класс Platform .класс —  это шаблон, с помощью которого удобно описывать
   однотипные объекты. В классе соержатся свойства, правила создания
    и поведение объекта. Объект — экземпляр, созданный на основе шаблона.
     Атрибут — поле, хранящее значение.мы создаём класс платформер для того чтобы сделать твёрдые 
     платформы
    """
    def __init__ (self,x,y):
        """
        мы создаём функцию init
        """
        
        sprite.Sprite.__init__(self)
        self.image=Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect=Rect(x,y,PLATFORM_WIDTH,PLATFORM_HEIGHT)

        '''''
        мы создаем функцию self которая self — это ссылка на текущий 
        экземпляр класса. Это способ обращения к атрибутам и методам класса
         изнутри самого класса
        '''''
