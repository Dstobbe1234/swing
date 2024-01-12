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


class Trampoline:
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def checkCollision(self):
        testX = ball.x
        testY = ball.y

        if (ball.x < self.position[0]):
            testX = self.position[0]
        elif (ball.x > self.position[0] + 100):
            testX = self.position[0] + 100

        if (ball.y < self.position[1]):
            testY = self.position[1]
        elif (ball.y > self.position[1] + 5):
            testY = self.position[1] + 5

        distY = ball.y - testY
        distX = ball.x - testX

        if (math.sqrt(distX**2 + distY**2) <= 10):
            self.bounce()

    def bounce(self):
        if (ball.mouse):
            ball.angleSpeed += (abs(ball.angleSpeed) /
                                ball.angleSpeed) * 0.5/ball.radius
            ball.angleSpeed *= -1
        else:
            if (self.orientation == "vert"):
                ball.speedVectors[0] *= -1
            else:
                ball.speedVectors[1] *= -1

    def draw(self):
        pygame.draw.rect(
            screen, "white", (self.position[0], self.position[1], 100, 5))


class Button:
    def __init__(self, position):
        self.position = position
        self.rangeRadius = 50
        self.color = "white"

    def checkRange(self):
        if math.sqrt((self.position[0]-ball.x)**2 + (self.position[1]-ball.y)**2) <= 10 + self.rangeRadius:
            self.color = "red"
            return True

    def draw(self):
        pygame.draw.circle(
            screen, self.color, (self.position[0], self.position[1]), 5)


trampolines = []
buttons = []


def generateChunks():
    possibleChunks = [[Trampoline(
        [screenSize[0]/2, 500], "horiz"), Trampoline([screenSize[0]/2 + 100, 500], "horiz"), Button([screenSize[0]/2 + 50, 300])]]
    randomIndex = random.randint(0, len(possibleChunks)-1)
    randomChunk = possibleChunks[randomIndex]
    for object in randomChunk:
        if (type(object).__name__ == "Trampoline"):
            trampolines.append(object)
        else:
            buttons.append(object)


ball = Ball(screenSize[0]/2, screenSize[1]/2)


def loop():
    while running:
        inRange = False
        screen.fill("black")
        ball.draw()
        for trampoline in trampolines:
            trampoline.draw()
            trampoline.checkCollision()
        # for button in buttons:
        #     if button.checkRange():
        #         inRange = True
        #     button.draw()
        pygame.display.flip()

        # if (ball.mouse and inRange):
        if (ball.mouse):
            ball.swing()
        else:
            ball.fall()

        ball.checkMouse()

        clock.tick(500)


if __name__ == "__main__":
    generateChunks()
    loop()
    pygame.quit
