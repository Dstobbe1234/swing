# Example file showing a circle moving on screen
import pygame
import math
clock = pygame.time.Clock()
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)
bobAngle = (math.pi) * 3/4
mouse = False

def swing(mousePos, radius, angle, bobSpeed):
    mouse = True
    while mouse:
        screen.fill("purple")
        pygame.draw.line(screen, 'black', mousePos, player_pos, 1)
        player_pos[0] = mousePos[0] + radius * math.cos(angle)
        player_pos[1] = mousePos[1] + radius * math.sin(angle)
        bobAcceleration = 0.0001 * math.cos(angle)
        bobSpeed += bobAcceleration
        # angle += math.atan(bobSpeed)
        pygame.draw.circle(screen, "red", player_pos, 40)
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if(event.type == pygame.MOUSEBUTTONUP):
                mouse = False
    fall([bobSpeed * math.cos(angle), bobSpeed * math.sin(angle)])
    


def fall(bobSpeedVectors):
    mouse = False
    while not mouse:
        screen.fill("purple")
        bobAcceleration = 0.001
        print(bobSpeedVectors)
        bobSpeedVectors[1] += bobAcceleration
        global player_pos
        player_pos[0] += bobSpeedVectors[0]
        player_pos[1] += bobSpeedVectors[1]
        pygame.draw.circle(screen, "red", player_pos, 40)
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                radius = math.sqrt(((player_pos[1]-mousePos[1])**2) + ((player_pos[0]-mousePos[0])**2))
                mouse = True
    swing(mousePos, radius, math.atan2(player_pos[1]- mousePos[1], player_pos[0] - mousePos[0]), math.sqrt((bobSpeedVectors[0] ** 2) + (bobSpeedVectors[1] ** 2)))

while running:
    fall([0, 0])
    clock.tick(10) 

pygame.quit()
        