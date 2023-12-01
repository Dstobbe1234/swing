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
gravity = 0.00001
offsetX = random.randint(0, 5000)
offsetY = random.randint(0, 5000)
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

def swing(mousePos, radius, angle, angleSpeed):
    mouse = True

    while mouse:
        draw()
        pygame.draw.line(screen, 'white', mousePos, player_pos, 1)
        # pygame.draw.line(screen, "red", )
        print(angle)
        pygame.display.flip()
        swingPos = [player_pos.copy()]
        bobAcceleration =  (gravity/radius) * math.cos(angle)
        angleSpeed += bobAcceleration
        angle += angleSpeed

        swingPos.append([mousePos[0] + radius * math.cos(angle), mousePos[1] + radius * math.sin(angle)])   
        player_pos[0] = swingPos[1][0]
        player_pos[1] = swingPos[1][1]

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
        draw()
        pygame.display.flip()
        bobAcceleration = gravity
        bobSpeedVectors[1] += bobAcceleration
        global player_pos
        player_pos[0] += bobSpeedVectors[0]
        player_pos[1] += bobSpeedVectors[1]
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

def draw():
    screen.fill("black")
    pygame.draw.circle(screen, "white", player_pos, 10)


while running:
    fall([0, 0])

pygame.quit()


            


    