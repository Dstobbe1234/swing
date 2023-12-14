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
        while self.mouse:
            self.draw()


            ## position in pendulum before swing
            swingPos = [[self.x, self.y]]
            
            ## Angular Acceleration
            bobAcceleration =  (gravity/self.radius) * math.cos(self.angle)

            ## Angular Velocity
            self.angleSpeed += bobAcceleration

            ## Pendulum Angle
            self.angle += self.angleSpeed

            ## position after angle change
            swingPos.append([self.mousePos[0] + self.radius * math.cos(self.angle), self.mousePos[1] + self.radius * math.sin(self.angle)])

            ## position change
            self.x = swingPos[1][0]
            self.y = swingPos[1][1]

            ## event loop
            ev = pygame.event.get()
            for event in ev:
                if(event.type == pygame.MOUSEBUTTONUP):
                    if(event.button == 1):
                        ## Convert Angular speed into vectors
                        self.speedVectors = [swingPos[1][0] - swingPos[0][0], swingPos[1][1] - swingPos[0][1]]
                        pendulum = Pendulum(math.sqrt(self.speedVectors[0]**2 + self.speedVectors[1]**2), self.y, self.x)
                        pendulum.calculate()
                        pygame.display.flip()
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
                    self.count +=1
                    self.mousePos = pygame.mouse.get_pos()
                    self.radius = math.sqrt(((self.y-self.mousePos[1])**2) + ((self.x-self.mousePos[0])**2))
                    xDiff = self.x - self.mousePos[0]
                    self.angleSpeed = math.atan(math.sqrt(self.speedVectors[0] ** 2 + self.speedVectors[1] ** 2) / self.radius) * (xDiff / abs(xDiff)) * (self.speedVectors[1] / abs(self.speedVectors[1]))
                    self.mouse = True
                    if(self.count > 1):
                        data = np.array(points)
                        x, y = data.T
                        polyline = np.linspace(points[0][0], points[-1][0], 100)
                        model = np.poly1d(np.polyfit(x, y, 2))
                        print(model)
                        plt.subplot(1, 2, 2)
                        plt.scatter(x,y)
                        plt.plot(polyline, model(polyline), "red")
                        plt.show()
                        
        self.swing()
    
    def draw(self):
        screen.fill("black")
        pygame.draw.circle(screen, "white", (self.x, self.y), 10)
        if(self.mouse):
            pygame.draw.line(screen, 'white', self.mousePos, (self.x, self.y), 1)
        pygame.display.flip()

class Pendulum:
    def __init__(self, initSpeed, h0, x0):
        self.initSpeed = initSpeed
        self.h0 = h0
        self.x0 = x0
    def calculate(self):
        points = []
        x = 0
        for n in range(750):
            x+= 1
            y = (-1/2 * gravity * (((x * ball.speedVectors[0]) + ball.x)**2)) + (ball.speedVectors[1] * ((x * ball.speedVectors[0]) + ball.x)) + self.h0
            points.append([x, y])
        print(gravity)
        print(ball.speedVectors[1])
        print(ball.speedVectors[0])
        print(ball.x, ball.y)

        data = np.array(points)
        x, y = data.T
        plt.subplot(1, 2, 2)
        plt.scatter(x,y)
        plt.show()


        




# class Terrain:
#     def generate(self):
#         self.mousePos = 



ball = Ball(screenSize[0]/2, screenSize[1]/2)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball.fall()
    clock.tick(100)



pygame.quit()




    