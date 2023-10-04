# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
yAcceleration = 0.1
ySpeed = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)

    # flip() the display to put your work on screen
    pygame.display.flip()
    ySpeed += yAcceleration
    player_pos[1] += ySpeed
    if (player_pos[1] > screen.get_height()):
        ySpeed = -ySpeed - 0.1

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # dt = clock.tick(60) / 1000

pygame.quit()
