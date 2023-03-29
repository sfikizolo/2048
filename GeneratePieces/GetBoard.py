import pygame 

pygame.init()
Width = 600
Height = 700
screen = pygame.display.set_mode([Width,Height])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60 
font = pygame.font.Font('freesansbold.ttf', 24)

def board():
    pygame.draw.rect(screen, 'gray',[0,0,600,600],0,10)