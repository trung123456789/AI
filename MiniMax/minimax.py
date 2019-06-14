def CheckStateGame(board):
    state_game = 'DRAW_GAME'
    if CheckNgang(board):
        state_game = CheckNgang(board)
    if CheckDoc(board):
        state_game = CheckNgang(board)
    if CheckCheoXuoi(board):
        state_game = CheckNgang(board)
    if CheckCheoNguoc(board):
        state_game = CheckNgang(board)

    return state_game

def CheckNgang(board):
    value = [1,4,7]
    for item in value:
        if board['{}'.format(item)] is  board['{}'.format(item + 1)] is board['{}'.format(item + 2)] is 'X':
            return 'WIN_GAME'
        if board['{}'.format(item)] is  board['{}'.format(item + 1)] is board['{}'.format(item + 2)] is 'O':
            return 'LOSE_GAME'

def CheckDoc(board):
    value = [1,2,3]
    for item in value:
        if board['{}'.format(item)] is  board['{}'.format(item + 3)] is board['{}'.format(item + 6)] is 'X':
            return 'WIN_GAME'
        if board['{}'.format(item)] is  board['{}'.format(item + 3)] is board['{}'.format(item + 6)] is 'O':
            return 'LOSE_GAME'

def CheckCheoXuoi(board):
    if board['1'] is  board['5'] is board['9'] is 'X':
        return 'WIN_GAME'
    if board['1'] is  board['5'] is board['9'] is 'O':
        return 'LOSE_GAME'

def CheckCheoNguoc(board):
    if board['3'] is  board['5'] is board['7'] is 'X':
        return 'WIN_GAME'
    if board['3'] is  board['5'] is board['7'] is 'O':
        return 'LOSE_GAME'

def findBestMove(board):
    bestMove = None
    for move in board :
        if move > bestMove:
            bestMove = move
    return bestMove

# def MiniMax(board, isMaximizingPlayer):
#     if(CheckStateGame(curMove) == 'WIN_GAME'):
#         return MAX
#     if(CheckStateGame(curMove) == 'LOSE_GAME'):
#         return MIN
#     if( CheckStateGame(curMove) == 'DRAW_GAME'): 
#         return DRAW_VALUE
#     if isMaximizingPlayer:
#         bestVal = "-INFINITY"
#         for move in board:
#             value = MiniMax(board, False)
#             bestVal = max( bestVal, value) 
#         return bestVal
#     else :
#         bestVal = "+INFINITY" 
#         for move in board :
#             value = MiniMax(board,True)
#             bestVal = min( bestVal, value) 
#         return bestVal

board = {'1': '', '2': '', '3': 'O', '4': '', '5': 'O', '6': '', '7': 'O', '8': '', '9': ''}

a = CheckStateGame(board)
print(a)