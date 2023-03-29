import pygame 
import random
from GeneratePieces import Turn,GetBoard,GetPieces,NewPiece

pygame.init()

Width = 600
Height = 700
screen = pygame.display.set_mode([Width,Height])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60 
font = pygame.font.Font('freesansbold.ttf', 24)


board_values = [[0 for _ in range(4) ] for _ in range(4)]
game_over= False
spawn_new = True
start_count = 0
direction =""


colors = {0: (204, 192, 179),2: (238, 228, 218),4: (237, 224, 200),
          8: (242, 177, 121),16: (245, 149, 99),32: (246, 124, 95),
          64: (246, 94, 59),128: (237, 207, 114),256: (237, 204, 97),
          512: (237, 200, 80),1024: (237, 197, 63),2048: (237, 194, 46),
          'light text': (249, 246, 242),'dark text': (119, 110, 101),
          'other': (0, 0, 0),'bg': (187, 173, 160)}



              

run = True

while run:
    timer.tick(fps)
    screen.fill('blue')
    GetBoard.board()
    GetPieces.pieces(board_values)
    if spawn_new or start_count < 2:
        board_values , game_over = NewPiece.new_piece(board_values)
        spawn_new = False
        start_count +=1
    if direction != '':
        board_values = Turn.take_turn(direction,board_values)
        direction = ''
        spawn_new = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN" 
            elif event.key == pygame.K_LEFT:
                direction = "LEFT" 
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT" 


    pygame.display.flip()
pygame.quit()


