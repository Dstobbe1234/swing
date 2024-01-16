from turtle import back
import pygame
from itertools import permutations
colors = []
flags = 0
selectedColor = ""

clock = pygame.time.Clock()
pygame.init()
screenSize = [1200, 720]
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))
clock = pygame.time.Clock()
running = True


class ColorButton:
    def __init__(self, rect, price, color):
        self.rect = rect
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.price = price
        self.priceDisplay = self.font.render(
            f"{self.price} F", False, (0, 0, 0))
        self.color = color

    def checkClick(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if ((mousePos[0] > self.rect[0] and mousePos[0] < self.rect[0] + self.rect[2]) and
               (mousePos[1] > self.rect[1] and mousePos[1] < self.rect[1] + self.rect[3])):
                global flags
                global selectedColor
                global colors
                if ((self.color) in colors):
                    selectedColor = self.color
                    with open("persistantData.txt") as persistantDataFile:
                        lines = persistantDataFile.readlines()
                        lines[2] = f'{self.color[0]},{self.color[1]},{self.color[2]},{self.color[3]}'
                        with open("persistantData.txt", "w") as persistantDataFile:
                            for line in lines:
                                persistantDataFile.write(line)
                elif (self.price <= flags):
                    colors.append(self.color)
                    selectedColor = self.color
                    flags -= self.price
                    colorsData = []
                    for i in range(len(colors)):
                        colorsData.append(
                            f'{colors[i][0]},{colors[i][1]},{colors[i][2]},{colors[i][3]} ')
                    colorsData[-1] = colorsData[-1][:-1]
                    colorData = colorsData[-1]
                    with open("persistantData.txt", "w") as persistantDataFile:
                        persistantDataFile.writelines(
                            f'{flags}\n{"".join(colorsData)}\n{colorData}')
                        persistantDataFile.close()

    def draw(self):
        if (self.color == selectedColor):
            self.selected = True
        else:
            self.selected = False
        if (self.selected):
            pygame.draw.rect(screen, "blue", self.rect)
        else:
            pygame.draw.rect(screen, "white", self.rect)
        if (self.color == (255, 255, 255, 255)):
            pygame.draw.circle(
                screen, "black", (self.rect[0] + self.rect[2]/2, self.rect[1] + self.rect[3]/2), 21)
        pygame.draw.circle(
            screen, self.color, (self.rect[0] + self.rect[2]/2, self.rect[1] + self.rect[3]/2), 20)
        if (self.color not in colors):
            screen.blit(self.priceDisplay, (self.rect[0], self.rect[1]))


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


def selectSkin():
    white = pygame.Color(0)
    global flags
    global colors
    global selectedColor
    with open("persistantData.txt", "r") as persistantDataFile:
        persistantData = persistantDataFile.read().split("\n")
        flags = int(persistantData[0])
        colors = persistantData[1].split(" ")
        for i in range(len(colors)):
            valList = list(map(int, colors[i].split(",")))
            colors[i] = (valList[0], valList[1], valList[2], valList[3])
        selectedValList = list(map(int, persistantData[2].split(",")))
        selectedColor = (
            selectedValList[0], selectedValList[1], selectedValList[2], selectedValList[3])
        persistantDataFile.close()

    buttons = []
    allColors = []
    for hue in range(0, 360, 30):
        dark = pygame.Color(0)
        light = pygame.Color(0)

        dark.hsla = (hue, 30, 50, 100)
        light.hsla = (hue, 30, 70, 100)
        allColors.append(light)
        allColors.append(dark)
    for y in range(175, (4 * 150) + 100, 150):
        for x in range(175, (6 * 150) + 175, 150):
            buttons.append(
                ColorButton([x, y, 100, 100], (len(buttons) + 5) * 5, allColors[len(buttons)]))
    white = pygame.Color(0)
    white.hsla = (0, 0, 100, 100)
    buttons.append(ColorButton([screenSize[0]/2 - 50, 50, 100, 100], 0, white))

    back = Button(
        [80, 80, 60, 60], "back")
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif (back.is_clicked(event)):
                running = False
            for button in buttons:
                button.checkClick(event)

        screen.fill("black")
        for button in buttons:
            button.draw()
        back.draw()
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f"{flags}F", False, (255, 255, 255))
        screen.blit(text, (screenSize[0]-80, 80))
        pygame.display.flip()


if __name__ == "__main__":
    selectSkin()
