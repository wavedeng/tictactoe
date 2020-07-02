
def next_move(board,turn):


    next_x = None
    next_y = None
    max_score = None

    for y in range(len(board)):
        for x in range(len(board[y])):
            if(board[y][x]=='.'):
                if(turn):
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'

                score = minimax(board,not turn,0)

                if(max_score == None):
                    max_score = score
                    next_x  = x
                    next_y = y                
                else:
                    if(turn):
                        if(score>=max_score):
                            max_score = score
                            next_x  = x
                            next_y = y
                    else:
                        if(score<=max_score):
                            max_score = score
                            next_x  = x
                            next_y = y
                
                board[y][x] = '.'
    

    return next_x,next_y

                
                
def minimax(board,turn,depth):
    
    score = 0
    winner = checkWin(board)

    if(winner):
        if(winner == "no one"):
            return 0
        elif(winner == "O"):
            return 1
        else:
            return -1


    max_score = None

    for y in range(len(board)):
        for x in range(len(board[y])):
            if(board[y][x]=='.'):
                if(turn):
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'
                
                
                score = minimax(board,not turn,1)
                if max_score == None:
                    max_score = score
                else:
                    if not turn:
                        if(max_score > score):
                            max_score = score
                    else:
                        if(max_score<score):
                            max_score = score

                board[y][x] = '.'
    
    return max_score


def checkWin(board):
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '.'):
            return board[i][0]
    
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '.'):
            return board[0][i]

    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0]!='.'):
        return board[0][0]
    
    if(board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1]!='.'):
        return board[1][1]

    full = True

    for y in range(len(board)):
        for x in range(len(board[y])):
            if(board[y][x]=='.'):
                full = False

    if(full):
        return "no one"
    else:
        return None