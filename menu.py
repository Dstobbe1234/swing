

import pygame
import math
import random
clock = pygame.time.Clock()
pygame.init()
screenSize = [1200, 720]
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))
clock = pygame.time.Clock()
running = True


class Button:
    def __init__(self, rect, text):
        self.rect = rect
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = self.font.render(text, False, (0, 0, 0))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if ((mousePos[0] > self.rect[0] and mousePos[0] < self.rect[0] + self.rect[2]) and
               (mousePos[1] > self.rect[1] and mousePos[1] < self.rect[1] + self.rect[3])):
                return True

    def draw(self):
        pygame.draw.rect(screen, "green", self.rect)
        screen.blit(self.text, (0, 0))


def menu():
    button1 = Button([5, screenSize[1]/2, 50, 50], "game mode 1")
    button2 = Button(
        [screenSize[0] - 5, screenSize[1]/2, 50, 50], "game mode 2")
    global running
    while running:

        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False

            if (button1.is_clicked(event)):
                gameMode = 1
                break

            if (button2.is_clicked(event)):
                gameMode = 2
                break

        screen.fill("black")
        button1.draw()
        button2.draw()
        pygame.display.flip()


menu()
