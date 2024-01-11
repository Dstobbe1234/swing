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
    def __init__(self, position):
        self.position = position
    # def checkCollision(self):

        # if(ball.x> self.position[0] + 100):
        #     testX = self.position[0] + 100
        # else:
        #     testX = self.position[0]
        
        # if(ball.y > self.position[1] + 5):
        #     testY = self.position[1] + 5
        # else:
        #     testY = self.position[1]
        

        # distY = ball.y - testY
        # distX = ball.x - testX

        # if(math.sqrt(distX**2 + distY**2) <= 10 * 2):
        #     ball.color = "red"
        # else:
        #     ball.color = "white"

    def draw(self):
        pygame.draw.rect(screen, "white", (self.position[0], self.position[1], 100, 5))

class Button:
    def __init__(self, position):
        self.position = position
    def checkRange(self):
        print("filler")

trampolines = []
buttons = []

def generateChunks():
    possibleChunks = [[Trampoline([screenSize[0]/2, 500]), Trampoline([screenSize[0]/2 + 100, 500]), Button([40, 50])]]
    randomIndex = random.randint(0, len(possibleChunks)-1)
    randomChunk = possibleChunks[randomIndex]
    for object in randomChunk:
        if(type(object).__name__ == "Trampoline"):
            trampolines.append(object)
        else:
            buttons.append(object)


ball = Ball(screenSize[0]/2, screenSize[1]/2)
def loop():
    while running:

        screen.fill("black")
        ball.draw()
        for trampoline in trampolines:
            trampoline.draw()
            # trampoline.checkCollision()
        pygame.display.flip()

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