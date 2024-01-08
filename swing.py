from matplotlib import pyplot as plt
import numpy as np
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
gravity = 0.0005
offsetX = random.randint(0, 5000)
offsetY = random.randint(0, 5000)


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
        self.swinging = False
        self.count = 0

    def swing(self):
        self.aVelocity = 0
        while self.mouse:
            self.draw()

            swingPos = [[self.x, self.y]]
            # self.angle = -1 * math.atan2(
            #     self.x - self.mousePos[0], self.y - self.mousePos[1])

            # perpendicularGravity = (
            #     gravity / self.radius) * math.sin(self.angle)

            # self.angleSpeed += perpendicularGravity

            # print(perpendicularGravity)

            # self.angle += self.angleSpeed

            # swingPos.append([self.mousePos[0] + self.radius * math.cos(self.angle),
            #                 self.mousePos[1] + self.radius * math.sin(self.angle)])

            # self.x = swingPos[1][0]
            # self.y = swingPos[1][1]

            bobAcceleration = (gravity/self.radius) * math.cos(self.angle)
            # ## Angular Acceleration
            # bobAcceleration =  (gravity/self.radius) * math.cos(self.angle)

            # Angular Velocity
            self.angleSpeed += bobAcceleration
            # ## Angular Velocity
            # self.angleSpeed += bobAcceleration

            # Pendulum Angle
            self.angle += self.angleSpeed
            # ## Pendulum Angle
            # self.angle += self.angleSpeed

            # position after angle change
            swingPos.append([self.mousePos[0] + self.radius * math.cos(self.angle),
                            self.mousePos[1] + self.radius * math.sin(self.angle)])
            # ## position after angle change
            # swingPos.append([self.mousePos[0] + self.radius * math.cos(self.angle), self.mousePos[1] + self.radius * math.sin(self.angle)])

            # position change
            self.x = swingPos[1][0]
            self.y = swingPos[1][1]

            # # event loop
            # ev = pygame.event.get()
            # for event in ev:
            # if (event.type == pygame.MOUSEBUTTONUP):
            #     if (event.button == 1):
            #         self.speedVectors = [
            #             swingPos[1][0] - swingPos[0][0], swingPos[1][1] - swingPos[0][1]]
            #         self.mouse = False

    def fall(self):
        points = []
        while not self.mouse:

            self.draw()

            self.acceleration = gravity

            # Y speed is affected by gravity
            self.speedVectors[1] += self.acceleration

            # X position increases at a linear rate based on the final speed of the bob
            self.x += self.speedVectors[0]
            self.y += self.speedVectors[1]

            ev = pygame.event.get()
            for event in ev:
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.mousePos = pygame.mouse.get_pos()
                    self.radius = math.sqrt(
                        ((self.y-self.mousePos[1])**2) + ((self.x-self.mousePos[0])**2))
                    self.mouse = True

        self.swing()

    def draw(self):
        screen.fill("black")
        pygame.draw.circle(screen, "white", (self.x, self.y), 10)
        if (self.mouse):
            pygame.draw.line(screen, 'white', self.mousePos,
                             (self.x, self.y), 1)
        pygame.display.flip()


class Prediction:
    def __init__(self):
        self.fallPos = []
        self.pendulumPos = []

    def plotFall(self, xSpeed, ySpeed):

        randomX = random.randint()
        y = ((ball.speedVectors[1] + (1/2 * gravity * ((x - ball.x) /
             ball.speedVectors[0])))*((x - ball.x)/ball.speedVectors[0]) + ball.y)


ball = Ball(screenSize[0]/2, screenSize[1]/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball.fall()
    clock.tick(100)


pygame.quit()
