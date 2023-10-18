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
velocity = [0, 0]
acceleration = [0, 0]
gravity = 1
mouse = False

class pendulum:
    def __init__(self, pos):
        self.pos = pos
    def getAngle(self):
        angle = math.atan2(player_pos[1]- self.pos[1], player_pos[0] - self.pos[0])
        return angle

while running:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            radius = math.sqrt(((player_pos[1]-pos[1])**2) + ((player_pos[0]-pos[0])**2))
            bobAngle = math.atan2(player_pos[1]- pos[1], player_pos[0] - pos[0])
            bobSpeed = 0.0001
            airRes = 0
            mouse = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = False
    screen.fill("purple")
    
    if(mouse):
        player_pos[0] = pos[0] + radius * math.cos(bobAngle)
        player_pos[1] = pos[1] + radius * math.sin(bobAngle)
        bobAcceleration = 0.0001 * math.cos(bobAngle)
        bobSpeed += bobAcceleration
        bobAngle += bobSpeed
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.display.flip()
    # clock.tick(60) 

pygame.quit()
        