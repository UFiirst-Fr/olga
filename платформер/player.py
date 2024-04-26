from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#000000"
JUMP_POWER = 10
GRAVITY = 0.35


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGroud = False
        self.score=0

    def update(self, left, right, up, platforms):
        if up:
            if self.onGroud:
                self.yvel = JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED
        if not (left or right):
            self.xvel = 0

        if not self.onGroud:
            self.yvel += GRAVITY
        self.onGroud = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGroud = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

    #
    # def draw(self, screen):
    #     screen.blit(self.image, (self.rect.x, self.rect.y))
