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

colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

def board():
    pygame.draw.rect(screen, 'gray',[0,0,600,600],0,10)

def pieces():
    print('tiles')

while True :
    timer.tick(fps)
    screen.fill('blue')
    board()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.display.flip()
pygame.quit()


