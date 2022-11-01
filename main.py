import pygame
from pygame.locals import *
import random

pygame.init()
display=pygame.display.set_mode((800,500))
clock=pygame.time.Clock()
fps=60

alien = pygame.image.load("sprites//alien.png")
alien = pygame.transform.scale(alien, (alien.get_size()[0]/5, alien.get_size()[1]/5))
alienSize = alien.get_size()
alienPos = [(i*50, j*50+50) for i in range(15) for j in range(3)]
offset = 1
al = 1

ship = pygame.image.load("sprites//ship.png")
ship = pygame.transform.scale(ship, (ship.get_size()[0]/6, ship.get_size()[1]/6))
shipPos = [0, 400]
speed = 10
delay = 0

lasers = []

while True:
    display.fill(0)
    
    if not alienPos:
        print("You won")
        exit()

    for pos in range(len(lasers)):
        lasers[pos][1] -= 6
        pygame.draw.rect(display, (255, 0, 0), (lasers[pos][0], lasers[pos][1], 2, 8))

    for pos in range(len(alienPos)):

        for shot in range(len(lasers)):
            if alienPos[pos][0] < lasers[shot][0] < alienPos[pos][0]+45 and alienPos[pos][1] < lasers[shot][1] < alienPos[pos][1]+45:
                alienPos[pos] = [-100, -100]
                lasers[shot] = [-100, -100]

        display.blit(alien, (alienPos[pos][0]+offset, alienPos[pos][1]))
        pygame.draw.circle(display, (255, 0, 0), (offset + alienPos[pos][0] + alienSize[0]/2, alienPos[pos][1] + alienSize[1]/2), 2)

    display.blit(ship, shipPos)

    keys = pygame.key.get_pressed()

    if keys[K_LEFT] and shipPos[0] > 0:
        shipPos[0] -= speed
    if keys[K_RIGHT] and shipPos[0] < 710:
        shipPos[0] += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if keys[pygame.K_SPACE] and not delay:
        lasers.append([shipPos[0] + ship.get_size()[0]/2, 400])
        delay = 15

    if delay > 0:
        delay -= 1
    if offset == 60 or offset == 0:
        al *= -1
    offset += al
    for i in lasers:
        if i[1] < 0:
            lasers.pop(0)
    try:
        while True:
            alienPos.remove([-100, -100])
            print(True)
    except:
        pass

    pygame.display.update()
    clock.tick(fps)