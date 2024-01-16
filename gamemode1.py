import pygame
import random
from swing import Ball, running
import math

clock = pygame.time.Clock()
pygame.init()
screenSize = [1200, 720]
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))
clock = pygame.time.Clock()
mouse = False
boost = 1
gravity = 0.01


def game1():
    ball = Ball(screenSize[0]/2, screenSize[1]/2)
    ball.backgroundMove = False
    while running:
        screen.fill("black")
        ball.draw()
        pygame.display.flip()
        if (ball.mouse):
            ball.swing()
        else:
            ball.fall()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                return
            ball.inRange = True
            ball.mousePos = pygame.mouse.get_pos()
            ball.checkMouse(event)
        clock.tick(500)


if __name__ == "__main__":
    game1()
    pygame.quit
