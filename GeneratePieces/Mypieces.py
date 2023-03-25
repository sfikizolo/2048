def take_turn(direc,board):
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range (i):
                        if board[q][j]==0:
                            shift +=1 
                    if shift > 0:
                        board[i-shift][j] = board[i][j]
                        board[i][j]=0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        board[i-shift-1][j] *=2
                        board[i-shift][j]=0
                        merged[i-shift-1][j]=True

         