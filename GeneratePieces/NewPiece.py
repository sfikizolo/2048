import random

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