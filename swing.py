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
import numpy as np
from matplotlib import pyplot as plt

class Ball:
    def __init__(self, x, y):
        self.x  = x
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
        self.angle = math.atan2(self.y- self.mousePos[1], self.x - self.mousePos[0])
        # dtheta = 0
        t = 0
        x = []
        y = []
        # dt = 1
        while self.mouse:
            self.draw()

            # ## position in pendulum before swing
            # swingPos = [[self.x, self.y]]
            
            # ## Angular Acceleration
            # bobAcceleration =  (gravity/self.radius) * math.cos(self.angle)

            # ## Angular Velocity
            # self.angleSpeed += bobAcceleration

            # ## Pendulum Angle
            # self.angle += self.angleSpeed

            # ## position after angle change
            # swingPos.append([self.mousePos[0] + self.radius * math.cos(self.angle), self.mousePos[1] + self.radius * math.sin(self.angle)])

            # ## position change
            # self.x = swingPos[1][0]
            # self.y = swingPos[1][1]
            
            # # ddtheta = -1 * gravity * math.cos(self.angle)/self.radius
            # # dtheta = dtheta + ddtheta * dt
            # # self.angle = self.angle - dtheta * dt
            # # self.x = self.mousePos[0] + self.radius * math.cos(self.angle)
            # # self.y = (self.mousePos[1] + self.radius * math.sin(self.angle))
            # x.append(t)
            # y.append(self.angle)
            # t +=1
            # self.angle = math.atan2(self.y- self.mousePos[1], self.x - self.mousePos[0])
            # x += math.cos(gravity * math.cos(self.angle)) - math.cos(gravity * math.sin(self.angle))
            # y += math.sin(gravity * math.cos(self.angle)) - math.sin(gravity * math.sin(self.angle))


            



            ## event loop
            ev = pygame.event.get()
            for event in ev:
                if(event.type == pygame.MOUSEBUTTONUP):
                    if(event.button == 1):
                        ## Convert Angular speed into vectors
                        # plt.plot(x, y)
                        # x = np.linspace(x[0], x[-1], 100)
                        # y = math.cos(x)
                        # # print(x)
                        # # y = gravity * math.cos(x) * self.radius
                        # plt.plot(x, y)

                        # plt.show()
                        self.speedVectors = [swingPos[1][0] - swingPos[0][0], swingPos[1][1] - swingPos[0][1]]
                        self.mouse = False
        # self.fall()

    def fall(self):
        points = []
        while not self.mouse:

            self.draw()

            self.acceleration = gravity

            ## Y speed is affected by gravity
            self.speedVectors[1] += self.acceleration

            ## X position increases at a linear rate based on the final speed of the bob 
            self.x += self.speedVectors[0]
            self.y += self.speedVectors[1]
            points.append([self.x, self.y])
            ev = pygame.event.get()
            for event in ev:
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    self.mousePos = pygame.mouse.get_pos()
                    self.radius = math.sqrt(((self.y-self.mousePos[1])**2) + ((self.x-self.mousePos[0])**2))
                    xDiff = self.x - self.mousePos[0]
                    ##TODO: FIX 
                    self.angleSpeed = math.atan(math.sqrt(self.speedVectors[0] ** 2 + self.speedVectors[1] ** 2) / self.radius) * (xDiff / abs(xDiff)) * (self.speedVectors[1] / abs(self.speedVectors[1]))
                    # self.angleSpeed = math.sqrt((self.speedVectors[0]**2) + (self.speedVectors[1]**2)) / self.radius * (xDiff / abs(xDiff)) * (self.speedVectors[1] / abs(self.speedVectors[1]))
                    # print(self.speedVectors[0], self.speedVectors[1], self.radius)
                    # print(self.angleSpeed)
                    self.mouse = True
                        
        self.swing()
    
    def draw(self):
        screen.fill("black")
        pygame.draw.circle(screen, "white", (self.x, self.y), 10)
        if(self.mouse):
            pygame.draw.line(screen, 'white', self.mousePos, (self.x, self.y), 1)
        pygame.display.flip()

class Prediction:
    def __init__(self):
        self.fallPos = []
        self.pendulumPos = []
    def plotFall(self, xSpeed, ySpeed):
        
        randomX = random.randint()
        y = ((ball.speedVectors[1] + (1/2 * gravity * ((x - ball.x)/ball.speedVectors[0])))*((x - ball.x)/ball.speedVectors[0]) + ball.y)

    # def plotPendulum(self, speed, radius):

# def generateWorld():
#     for n in range(random.randint(5, 10)):







ball = Ball(screenSize[0]/2, screenSize[1]/2)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball.fall()
    clock.tick(100)



pygame.quit()




    