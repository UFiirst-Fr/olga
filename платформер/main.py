import pygame
from player import *
from blocks import *
from coins import *
import random

pygame.init()

screen = display.set_mode((800, 640))
display.set_caption('Pygame Platformer')

font = pygame.font.SysFont("Arial", 32)

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


def main():
    hero = Player(55, 55)
    left = right = False
    up = False

    entities = pygame.sprite.Group()
    platform = []
    entities.add(hero)

    coins_group = pygame.sprite.Group()

    for i in range(10):
        x_coin = random.randint(32, 768)
        y_coin = random.randint(32, 602)

        coin = Coins(x_coin, y_coin)
        coins_group.add(coin)

    level = [
        "-------------------------",
        "-     --    for         -",
        "-            -----      -",
        "-                       -",
        "-                -----  -",
        "-                       -",
        "----                    -",
        "-         ---- ----------",
        "-                       -",
        "-                       -",
        "- --- ---------         -",
        "-                       -",
        "-   ----- ----- ------- -",
        "-                       -",
        "-     -------  ----     -",
        "-   ----------- -------- -",
        "-                       -",
        "-   ---- --- --- --- - -",
        "-------------------------"]

    timer = pygame.time.Clock()

    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                FRG = Platform(x, y)
                entities.add(FRG)
                platform.append(FRG)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    active = True
    while active:
        timer.tick(60)
        screen.fill('#008000')

        hero.update(left, right, up, platform)
        entities.draw(screen)

        coins_group.update()

        collisions = pygame.sprite.spritecollide(hero, coins_group, True)

        for coin in collisions:
            hero.score += 1

        coins_group.draw(screen)

        score_text = font.render(f"Score:{hero.score}", True, (0, 0, 0))
        screen.blit(score_text, (40, 32))

        x = y = 0
        for row in level:
            for cal in row:
                if cal == "-":
                    FRG = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    FRG.fill(Color(PLATFORM_COLOR))
                    screen.blit(FRG, (x, y))

                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True

            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False

            if event.type == KEYDOWN and event.key == K_UP:
                up = True

            if event.type == KEYUP and event.key == K_UP:
                up = False

        display.update()


if __name__ == "__main__":
    main()
