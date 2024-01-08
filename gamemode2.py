import random

class Trampoline:
    def __init__(self, position):
        self.position = position
    def bounce(self):
        print("filler")


class Button:
    def __init__(self, position):
        self.position = position
    def checkRange(self):
        print("filler")

trampolines = []
buttons = []

def generateChunks():
    possibleChunks = [[[Trampoline([0, 100]), Trampoline([20, 100]), Button([40, 50])]]]
    randomIndex = random.randint(0, len(possibleChunks))
    randomChunk = possibleChunks[randomIndex]
    for object in randomChunk:
        if(type(object).__name__ == "Trampoline"):
            trampolines.append(object)
        else:
            buttons.append(object)
