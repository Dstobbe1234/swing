import pygame
import math
import random

clock = pygame.time.Clock()
pygame.init()
screenSize = [1200, 720]
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))
clock = pygame.time.Clock()
running = True
mouse = False
boost = 1
gravity = 0.01


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.acceleration = gravity
        self.speedVectors = [0, 0]
        self.angleSpeed = 0
        self.angle = 0
        self.radius = 0
        self.mouse = False
        self.mousePos = []
        with open("persistantData.txt", "r") as persistantDataFile:
            persistantData = persistantDataFile.read().split("\n")
            selectedValList = list(map(float, persistantData[2].split(",")))
            self.color = (
                selectedValList[0], selectedValList[1], selectedValList[2], selectedValList[3])
        self.inRange = False
        self.bounceBool = False
        self.backgroundMove = False

    def swing(self):
        # # position in pendulum before swing
        self.swingPos = [[self.x, self.y]]

        # # Angular Acceleration
        bobAcceleration = -1 * (gravity/self.radius) * math.sin(self.angle)

        # # Angular Velocity
        self.angleSpeed += bobAcceleration

        # # Pendulum Angle
        self.angle += self.angleSpeed

        # # position after angle change
        self.swingPos.append([self.mousePos[0] + self.radius * math.sin(self.angle),
                              self.mousePos[1] + self.radius * math.cos(self.angle)])

        # # position change
        self.x = self.swingPos[1][0]
        self.y = self.swingPos[1][1]

    def fall(self):

        self.acceleration = gravity

        # Y speed is affected by gravity
        self.speedVectors[1] += self.acceleration

        # X position increases at a linear rate based on the final speed of the bob
        self.x += self.speedVectors[0]
        self.y += self.speedVectors[1]

    def checkMouse(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN and self.inRange):

            self.angle = math.atan2(
                self.x - self.mousePos[0], self.y - self.mousePos[1])

            self.radius = math.sqrt(
                ((self.y-self.mousePos[1])**2) + ((self.x-self.mousePos[0])**2))

            speed = abs((self.speedVectors[1] * math.sin(self.angle)) +
                        (self.speedVectors[0] * math.cos(self.angle)))

            self.angleSpeed = math.atan2(speed, self.radius)

            if (self.x > self.mousePos[0]):
                self.angleSpeed *= -1
            self.mouse = True

        elif (event.type == pygame.MOUSEBUTTONUP and self.mouse):
            # Convert Angular speed into vectors
            self.speedVectors = [
                self.swingPos[1][0] - self.swingPos[0][0], self.swingPos[1][1] - self.swingPos[0][1]]
            self.mouse = False

    def draw(self):
        if (self.backgroundMove):
            self.drawX = screenSize[0]/2
        else:
            self.drawX = self.x
        screen.fill("black")
        pygame.draw.circle(screen, self.color,
                           (self.drawX, self.y), 10)
        pygame.draw.circle(screen, self.color, (self.drawX, self.y), 10)
        if (self.mouse):
            if (self.backgroundMove):
                pygame.draw.line(screen, 'white', [self.mousePos[0] - (self.x - screenSize[0]/2), self.mousePos[1]],
                                 (self.drawX, self.y), 1)
            else:
                pygame.draw.line(screen, 'white', [self.mousePos[0], self.mousePos[1]],
                                 (self.drawX, self.y), 1)
