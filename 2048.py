import pygame 
import random
from GeneratePieces.Mypieces import pieces

pygame.init()

Width = 600
Height = 700
screen = pygame.display.set_mode([Width,Height])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60 
font = pygame.font.Font('freesansbold.ttf', 24)

def new_piece(board):
    over = True
    count = 0
    while any(0 in row for row in board) and count <1:
        row = random.randint(0,3)
        col = random.randint(0, 3)
        if board[row][col]==0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    
    if count < 1 :
        over = True    
        
    return board,over

board_values = [[0 for _ in range(4) ] for _ in range(4)]
game_over= False
spawn_new = True
start_count = 0


def take_turn(direc,board):
    merged = [[]]
    if direc == 'UP':
        pass
    elif direc == 'DOWN':
        pass
    elif direc == 'LEFT':
        pass
    elif direc == 'RIGHT':
        pass
    return board

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

# def pieces(board):
#     for i in range(4):
#         for j in range(4):
#             value = board[i][j]
#             if value > 8:
#                 value_color = colors['light text']
#             else:
#                 value_color = colors['dark text']
#             if value <= 2048:
#                 color =colors[value]
#             else:
#                 color = colors['other']
#             pygame.draw.rect(screen,color , [j * 145 + 20, i * 145  +20,125,125],0,5)
#             if value > 0 :
#                 value_len = len(str(value))
#                 font = pygame.font.Font('freesansbold.ttf', 58 - (6*value_len))
#                 value_text = font.render(str(value), True, value_color)
#                 text_rect = value_text.get_rect(center=(j * 145 + 75,i * 145 + 75))
#                 screen.blit(value_text,text_rect)
              


while True :
    timer.tick(fps)
    screen.fill('blue')
    board()
    pieces(board_values)
    direction = ''
    if spawn_new or start_count < 2:
        board_values , game_over = new_piece(board_values)
        spawn_new = False
        start_count +=1
    if direction != '':
        board_values = take_turn(direction,board_values)
        direction = ''
        spawn_new = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
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


