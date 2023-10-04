# Example file showing a circle moving on screen
import pygame
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
yAcceleration = 0.01
ySpeed = 0

def swing(pos):
    swinging = True
    while swinging:
        angle = math.atan((pos[1]-player_pos[1])/(pos[0]-player_pos[0]))* (180/math.pi)
        print(angle)
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                swinging = False
    

while running:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            swing(pygame.mouse.get_pos())

    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.display.flip()
    ySpeed += yAcceleration
    player_pos[1] += ySpeed
    if (player_pos[1] > screen.get_height()):
        ySpeed = -ySpeed - 0.01

pygame.quit()

