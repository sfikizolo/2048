import pygame 
import random

pygame.init()

Width = 600
Height = 700
screen = pygame.display.set_mode([Width,Height])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60 
font = pygame.font.Font('freesansbold.ttf', 24)

while True :
    timer.tick(fps)
    screen.fill('blue')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.display.flip()
pygame.quit()


