import tic_tac_toe
import unittest


class TestsAI(unittest.TestCase):
    def test_siege_center(self):
        test_board = [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        tic_tac_toe.AI_move(board)
        self.assertEqual(test_board, board)

    def test_siege_angle(self):
        test_board = [' ', 'O', ' ', 'Empty', ' ', 'X', ' ', 'Empty', ' ', 'Empty']
        board = [' ', ' ', ' ', 'Empty', ' ', 'X', ' ', 'Empty', ' ', 'Empty']
        tic_tac_toe.AI_move(board)
        self.assertEqual(test_board, board)

    def test_block_player(self):
        test_board = [' ', ' ', ' ', ' ', 'X', 'X', 'O', ' ', ' ', ' ']
        board = [' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ']
        tic_tac_toe.AI_move(board)
        self.assertEqual(test_board, board)

    def test_win_higher_priority(self):
        test_board = [' ', 'X', 'X', ' ', 'O', 'O', 'O', ' ', ' ', ' ']
        board = [' ', 'X', 'X', ' ', 'O', 'O', ' ', ' ', ' ', ' ']
        tic_tac_toe.AI_move(board)
        self.assertEqual(test_board, board)

    def test_block_priority_over_angle(self):
        test_board = [' ', ' ', ' ', ' ', 'X', 'X', 'O', ' ', ' ', ' ']
        board = [' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ']
        tic_tac_toe.AI_move(board)
        self.assertEqual(test_board, board)


if __name__ == '__main__':
    unittest.main()
