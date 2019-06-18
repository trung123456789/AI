import time
import constants

def CheckStateGame(board):
    state_game = constants.DRAW_STATE
    if CheckNgang(board):
        state_game = CheckNgang(board)
    if CheckDoc(board):
        state_game = CheckDoc(board)
    if CheckCheoXuoi(board):
        state_game = CheckCheoXuoi(board)
    if CheckCheoNguoc(board):
        state_game = CheckCheoNguoc(board)

    return state_game

def CheckNgang(board):
    value = [1,4,7]
    for item in value:
        if board['{}'.format(item)] is  board['{}'.format(item + 1)] is board['{}'.format(item + 2)] is constants.X_PLAY:
            return constants.WIN_STATE
        if board['{}'.format(item)] is  board['{}'.format(item + 1)] is board['{}'.format(item + 2)] is constants.O_PLAY:
            return constants.LOSE_STATE

def CheckDoc(board):
    value = [1,2,3]
    for item in value:
        if board['{}'.format(item)] is  board['{}'.format(item + 3)] is board['{}'.format(item + 6)] is constants.X_PLAY:
            return constants.WIN_STATE
        if board['{}'.format(item)] is  board['{}'.format(item + 3)] is board['{}'.format(item + 6)] is constants.O_PLAY:
            return constants.LOSE_STATE

def CheckCheoXuoi(board):
    if board[constants.LOCATE_1] is  board[constants.LOCATE_5] is board[constants.LOCATE_9] is constants.X_PLAY:
        return constants.WIN_STATE
    if board[constants.LOCATE_1] is  board[constants.LOCATE_5] is board[constants.LOCATE_9] is constants.O_PLAY:
        return constants.LOSE_STATE

def CheckCheoNguoc(board):
    if board[constants.LOCATE_3] is  board[constants.LOCATE_5] is board[constants.LOCATE_7] is constants.X_PLAY:
        return constants.WIN_STATE
    if board[constants.LOCATE_3] is  board[constants.LOCATE_5] is board[constants.LOCATE_7] is constants.O_PLAY:
        return constants.LOSE_STATE

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

def PrintChess(board):
    temp = ''
    for item in range(len(board)):
        if item % 3 == 0:
            print("{}\n".format(temp))
            temp = ''
        if board['{}'.format(item+1)] is not '':
            temp = temp + constants.NOT_BLANK.format(board['{}'.format(item+1)])
        else:
            temp = temp + constants.BLANK
    print("{}\n".format(temp))

def PlayGame(state, rotate, board):
    while state is not constants.EXIT_GAME:
        PrintChess(board)
        print('Type locate state {locate} to continue game or Use E to stop game:'.format(locate=constants.LOCATE))
        try:
            state = input()
            if int(state) in constants.LOCATE and board['{}'.format(state)] is '':
                if rotate is 1:
                    board['{}'.format(state)] = constants.X_PLAY
                    rotate = 0
                else:
                    board['{}'.format(state)] = constants.O_PLAY
                    rotate = 1
        except ValueError:
            print("That's not an int!")
            print("No.. input string is not an Integer. It's a string")

        if CheckStateGame(board) is constants.WIN_STATE:
            print(constants.FINISH_FOR_X)
            PrintChess(board)
            state = constants.EXIT_GAME
        if CheckStateGame(board) is constants.LOSE_STATE:
            print(constants.FINISH_FOR_O)
            PrintChess(board)
            state = constants.EXIT_GAME








board = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}

# a = CheckStateGame(board)
# print(a)
PlayGame("X", 0, board)