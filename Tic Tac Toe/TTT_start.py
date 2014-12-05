import tic_tac_toe

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_turn = "player"
game_not_over = True

while game_not_over:
    if current_turn == "player":
        tic_tac_toe.drawBoard(board)
        tic_tac_toe.playerMove(board)
        if tic_tac_toe.isWinner(board, 'X'):
            tic_tac_toe.drawBoard(board)
            print("You won the game!")
            game_not_over = False
        elif tic_tac_toe.isBoardFull(board):
            tic_tac_toe.drawBoard(board)
            print("The game is a tie!")
            game_not_over = False
        else:
            current_turn = "computer"

    elif current_turn == "computer":
        if tic_tac_toe.AI_move(board) is False:
            print("The AI won the game!")
            game_not_over = False
        else:
            if tic_tac_toe.isBoardFull(board):
                print("The game is a tie!")
            else:
                current_turn = "player"
