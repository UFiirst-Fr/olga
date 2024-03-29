import pygame
from pygame import *

pygame.init()

screen = display.set_mode((800, 640))
display.set_caption('Pygame Platformer')

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


def main():
    level = [
        "-------------------------",
        "-     --                -",
        "-            -----      -",
        "-                       -",
        "-                -----  -",
        "-                       -",
        "-___                    -",
        "-         _____________ -",
        "-                       -",
        "-                       -",
        "- ___  ________         -",
        "-                       -",
        "-   ____ ________ _____ -",
        "-                       -",
        "-     _____ _____       -",
        "-   ________   ________ -",
        "-                       -",
        "-------------------------"

    ]
    active = True
    while active:

        screen.fill('#008000')

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

        display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                pygame.quit()

main()