# Example file showing a circle moving on screen
import pygame
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2 )
yAcceleration = 0.01
ySpeed = 0
mouse = False
def swing(pos):
    angle = math.atan2(pos[1]-player_pos[1], (pos[0]-player_pos[0]))
    # print(player_pos[1]-pos[1], pos[0]-player_pos[0])
    print(angle)
    cos = math.cos(angle)
    sin = math.sin(angle)
    if(sin < 0):
        sin*=-1
    pygame.draw.line(screen, 'black', player_pos, [player_pos[0] + (100*cos), player_pos[1] + (100*sin)])
    player_pos[0] += (0.1 * cos)
    player_pos[1] += (0.1 * sin)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = False
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    if(mouse):
        swing(pos)

    # flip() the display to put your work on screen
    pygame.display.flip()
    # ySpeed += yAcceleration
    # player_pos[1] += ySpeed
    


pygame.quit()