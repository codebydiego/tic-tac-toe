import unittest
from src.tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """
    Test suite for the TicTacToe class.
    """

    def setUp(self):
        """
        Set up a new game instance before each test.
        """
        self.game = TicTacToe()

    def test_initialize_board(self):
        """
        Test that the board is initialized correctly.
        """
        self.assertEqual(self.game.board, [[" " for _ in range(3)] for _ in range(3)])

    def test_switch_player(self):
        """
        Test that the current player switches correctly.
        """
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "O")
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "X")

    def test_check_winner(self):
        """
        Test that the check_winner method correctly identifies a winner.
        """
        self.game.board = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertTrue(self.game.check_winner("X"))
        self.assertFalse(self.game.check_winner("O"))

    def test_check_tie(self):
        """
        Test that the check_tie method correctly identifies a tie.
        """
        self.game.board = [
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.game.check_tie())
        self.game.board[0][0] = " "
        self.assertFalse(self.game.check_tie())

    def test_computer_move(self):
        """
        Test that the computer_move method selects an empty cell.
        """
        self.game.board = [
            ["X", "O", "X"],
            ["X", " ", "O"],
            ["O", "X", "O"]
        ]
        row, col = self.game.best_move()
        self.assertEqual((row, col), (1, 1))

    def test_make_move(self):
        """
        Test that the make_move method correctly places a mark on the board.
        """
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], "X")
        self.assertFalse(self.game.make_move(0, 0))  # Cell already occupied

if __name__ == "__main__":
    unittest.main()