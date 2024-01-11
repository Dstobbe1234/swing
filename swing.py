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
        self.color = "white"

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

    def checkMouse(self):
        ev = pygame.event.get()
        for event in ev:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.mousePos = pygame.mouse.get_pos()
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

            elif (event.type == pygame.MOUSEBUTTONUP):
                # Convert Angular speed into vectors
                self.speedVectors = [
                    self.swingPos[1][0] - self.swingPos[0][0], self.swingPos[1][1] - self.swingPos[0][1]]
                self.mouse = False

            elif (event.type == pygame.QUIT):
                print("quit")
                global running
                running = False

    def draw(self):
        screen.fill("black")
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
        if (self.mouse):
            pygame.draw.line(screen, 'white', self.mousePos,
                             (self.x, self.y), 1)


ball = Ball(screenSize[0]/2, screenSize[1]/2)




def loop():
    while running:

        if (ball.mouse):
            ball.swing()
        else:
            ball.fall()

        screen.fill("black")
        ball.draw()
        pygame.display.flip()

        ball.checkMouse()

        clock.tick(500)


if __name__ == "__main__":
    loop()
    pygame.quit
