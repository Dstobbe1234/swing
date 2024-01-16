import pygame
from gamemode1 import game1
from gamemode2 import game2
from skins import selectSkin
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
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if ((mousePos[0] > self.rect[0] and mousePos[0] < self.rect[0] + self.rect[2]) and
               (mousePos[1] > self.rect[1] and mousePos[1] < self.rect[1] + self.rect[3])):
                return True

    def draw(self):
        pygame.draw.rect(screen, "green", self.rect)
        screen.blit(self.text, (self.rect[0], self.rect[1]))


def menu():
    button1 = Button([150, screenSize[1]/2, 200, 200], "game mode 1")
    button2 = Button(
        [screenSize[0] - 350, screenSize[1]/2, 200, 200], "game mode 2")
    skin = Button(
        [screenSize[0] - 80, 80, 60, 60], "skin")

    screen.fill("black")
    button1.draw()
    button2.draw()
    skin.draw()
    pygame.display.flip()
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            elif (button1.is_clicked(event)):
                return 1

            elif (button2.is_clicked(event)):
                return 2

            elif (skin.is_clicked(event)):
                return 3


if __name__ == "__main__":
    while True:
        exitCode = menu()
        if (exitCode == 0):
            break
        if (exitCode == 1):
            # PLAY 1st GAME MODE
            game1()
        elif (exitCode == 2):
            # PLAY 2nd GAME MODE
            game2()
        elif (exitCode == 3):
            selectSkin()
