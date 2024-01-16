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
chunkSize = 300
chunkNum = 5
ball = None
background = None
flag = None
trampolines = None
buttons = None


class Background:
    def __init__(self):
        self.w = chunkSize * chunkNum
        self.x = ball.x - screenSize[0]/2
        self.y = screenSize[1]/2

    def draw(self):
        self.x = ball.x - screenSize[0]/2

        screen.fill("black")
        ball.draw()
        flag.draw()
        for trampoline in trampolines:
            trampoline.draw()
            trampoline.checkCollision()
        ball.inRange = False
        for button in buttons:
            if button.checkRange():
                ball.inRange = True
                ball.mousePos = [button.position[0], button.position[1]]
            button.draw()
        pygame.display.flip()


class Trampoline:
    def __init__(self, rect, orientation):
        self.rect = rect
        self.orientation = orientation

    def checkCollision(self):
        testX = ball.x
        testY = ball.y

        if (ball.x < self.rect[0]):
            testX = self.rect[0]
        elif (ball.x > self.rect[0] + self.rect[2]):
            testX = self.rect[0] + self.rect[2]

        if (ball.y < self.rect[1]):
            testY = self.rect[1]
        elif (ball.y > self.rect[1] + self.rect[3]):
            testY = self.rect[1] + self.rect[3]

        distY = ball.y - testY
        distX = ball.x - testX

        if (math.sqrt(distX**2 + distY**2) <= 10):
            if (not ball.bounceBool):
                ball.bounceBool = True
                self.bounce()
        else:
            ball.bounceBool = False

    def bounce(self):
        if (ball.mouse):
            ball.angleSpeed += (abs(ball.angleSpeed) /
                                ball.angleSpeed) * 0.5/ball.radius
            ball.angleSpeed *= -1
        else:
            if (self.orientation == "vert"):
                ball.speedVectors[0] += (abs(ball.speedVectors[0]) /
                                         ball.speedVectors[0]) * 0.25
                ball.speedVectors[0] *= -1
            else:
                ball.speedVectors[1] += (abs(ball.speedVectors[1]) /
                                         ball.speedVectors[1]) * 0.25
                ball.speedVectors[1] *= -1

    def draw(self):
        pygame.draw.rect(
            screen, "white", (self.rect[0] - background.x, self.rect[1], self.rect[2], self.rect[3]))


class Button:
    def __init__(self, position):
        self.position = position
        self.rangeRadius = 150
        self.color = "white"

    def checkRange(self):
        if (math.sqrt((self.position[0]-ball.x)**2 + (self.position[1]-ball.y)**2) <= 10 + self.rangeRadius) and not ball.mouse:
            self.color = "red"
            return True
        self.color = "white"

    def draw(self):
        pygame.draw.circle(
            screen, self.color, (self.position[0] - background.x, self.position[1]), 5)


def generateChunks():
    for n in range(chunkNum):
        possibleChunks = [[Trampoline(
            [chunkSize*n, 500, 100, 5], "horiz"), Button([120 + chunkSize*n, 300])], [Trampoline(
                [chunkSize*n, 500, 50, 5], "horiz"), Button([100 + chunkSize*n, 300]), Trampoline([150 + chunkSize*n, 500, 50, 5], "horiz")]]
        randomIndex = random.randint(0, len(possibleChunks)-1)
        randomChunk = possibleChunks[randomIndex]
        for object in randomChunk:
            if (type(object).__name__ == "Trampoline"):
                trampolines.append(object)
            else:
                buttons.append(object)


class Flag():
    def __init__(self, x):
        self.x = x

    def draw(self):
        pygame.draw.line(screen, 'white', [self.x - background.x, 0],
                         [self.x - background.x, screenSize[1]], 5)

    def collision(self):
        if (ball.x >= self.x):
            return True


def die():
    if (ball.y >= screenSize[1]):
        return True


def game2():
    global ball
    global background
    global flag
    global buttons
    global trampolines
    ball = Ball(0, screenSize[1]/2)
    ball.backgroundMove = True
    trampolines = []
    buttons = []
    generateChunks()
    background = Background()
    flag = Flag(chunkNum * chunkSize)
    while running:
        background.draw()
        if (ball.mouse):
            ball.swing()
        else:
            ball.fall()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                return
            ball.checkMouse(event)
        if (die()):
            return

        if (flag.collision()):
            with open("persistantData.txt") as persistantDataFile:
                lines = persistantDataFile.readlines()
                lines[0] = str(int(lines[0]) + 5) + '\n'
                with open("persistantData.txt", "w") as persistantDataFile:
                    for line in lines:
                        persistantDataFile.write(line)
            return

        clock.tick(500)


if __name__ == "__main__":
    game2()
    pygame.quit
