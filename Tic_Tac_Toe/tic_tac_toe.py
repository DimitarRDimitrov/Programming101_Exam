import random
from copy import deepcopy


def drawBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(board, symbol):
    if ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or # across the top
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or # across the middle
    (board[1] == symbol and board[2] == symbol and board[3] == symbol) or # across the boardttom
    (board[7] == symbol and board[4] == symbol and board[1] == symbol) or # down the left side
    (board[8] == symbol and board[5] == symbol and board[2] == symbol) or # down the middle
    (board[9] == symbol and board[6] == symbol and board[3] == symbol) or # down the right side
    (board[7] == symbol and board[5] == symbol and board[3] == symbol) or # diagonal
    (board[9] == symbol and board[5] == symbol and board[1] == symbol)):
        return True
    return False


def isSpaceFree(board, move):
    if board[move] == ' ':
        return True
    return False


def playerMove(board):
    move = ' '
    while move not in range(1, 10) or not isSpaceFree(board, int(move)):
        move = int(input("Please enter your move: "))
    board[move] = 'X'

def AI_move(board):
    #try to win
    for i in range(1, 10):
        board_copy = deepcopy(board)
        if isSpaceFree(board_copy, i):
            board_copy[i] = 'O'
            if isWinner(board_copy, "O"):
                board[i] = 'O'
                # drawBoard(board)
                # print("The computer has beaten you!")
                # print("Game over!")
                return False
    #try to block
    for i in range(1, 10):
        board_copy = deepcopy(board)
        if isSpaceFree(board_copy, i):
            board_copy[i] = 'X'
            if isWinner(board_copy, "X"):
                board[i] = 'O'
                return True
    #try to take the centre
    if isSpaceFree(board, 5):
        board[5] = 'O'
        return True
    #take any edge
    available_moves = []
    for i in [1, 3, 7, 9]:
        if isSpaceFree(board, i):
            available_moves.append(i)
    if len(available_moves) > 0:
        i = random.choice(available_moves)
        board[i] = 'O'
        return True
    else:
        for i in [2, 4, 6, 8]:
            if isSpaceFree(board, i):
                available_moves.append(i)
        if len(available_moves) > 0:
            i = random.choice(available_moves)
            board[i] = 'O'
            return True



def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
