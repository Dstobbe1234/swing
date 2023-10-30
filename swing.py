import pygame
import math
import random
clock = pygame.time.Clock()
pygame.init()
screenSize = [1280, 720]
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)
mouse = False
boost = 1

import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise


def generateWorld():
    noise = PerlinNoise(octaves=10, seed=1)
    xpix = 64
    ypix = 36
    offsetX = random.randint(0, 5000)
    offsetY = random.randint(0, 5000)
    map = [[noise([i/xpix + offsetX, j/ypix + offsetY]) for j in range(xpix)] for i in range(ypix)]
    for row in range(len(map)):
        for i in range(len(map[row])):
            if(map[row][i] >= -0.1):
                pygame.draw.rect(screen, "white", (row + 20, i + 20, 20, 20))
            



def swing(mousePos, radius, angle, angleSpeed):
    mouse = True

    while mouse:

        screen.fill("black")
        pygame.draw.line(screen, 'white', mousePos, player_pos, 1)
        swingPos = [player_pos.copy()]
        global boost
        bobAcceleration =  0.00001 * math.cos(angle) * boost
        angleSpeed += bobAcceleration
        angle += angleSpeed

        swingPos.append([mousePos[0] + radius * math.cos(angle), mousePos[1] + radius * math.sin(angle)])   
        player_pos[0] = swingPos[1][0]
        player_pos[1] = swingPos[1][1]

        pygame.draw.circle(screen, "white", player_pos, 10)
        pygame.display.flip()

        ev = pygame.event.get()
        for event in ev:
            if(event.type == pygame.MOUSEBUTTONUP):
                if(event.button == 1):
                    bobSpeedVectors = [swingPos[1][0] - swingPos[0][0], swingPos[1][1] - swingPos[0][1]]
                    mouse = False
                elif(event.button == 3):
                    boost = 1
                    #bad
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 3):
                    boost = 3

    fall(bobSpeedVectors)
    


def fall(bobSpeedVectors):
    mouse = False
    while not mouse:
        screen.fill("black")
        bobAcceleration = 0.001
        bobSpeedVectors[1] += bobAcceleration
        global player_pos
        player_pos[0] += bobSpeedVectors[0]
        player_pos[1] += bobSpeedVectors[1]
        pygame.draw.circle(screen, "white", player_pos, 10)
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                radius = math.sqrt(((player_pos[1]-mousePos[1])**2) + ((player_pos[0]-mousePos[0])**2))
                xDiff = player_pos[0]  - mousePos[0]
                bobSpeed = math.atan(math.sqrt(bobSpeedVectors[0] ** 2 + bobSpeedVectors[1] ** 2) / radius) * (xDiff / abs(xDiff)) * (bobSpeedVectors[1] / abs(bobSpeedVectors[1]))
                ##NEEDS FIXING
                mouse = True
    swing(mousePos, radius, math.atan2(player_pos[1]- mousePos[1], player_pos[0] - mousePos[0]), bobSpeed)

# def checkMouse():

# def drawBob():


while running:
    fall([0, 0])
    clock.tick(1) 

pygame.quit()


            


    