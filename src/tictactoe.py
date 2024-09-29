import random

class TicTacToe:
    """
    A class to represent a Tic-Tac-Toe game.
    """

    def __init__(self):
        """
        Initialize the Tic-Tac-Toe board and set the current player to 'X'.
        """
        self.board = self.initialize_board()
        self.current_player = "X"

    def initialize_board(self):
        """
        Initialize the Tic-Tac-Toe board as a 3x3 grid filled with spaces.

        Returns:
            list: A 3x3 grid filled with spaces.
        """
        return [[" " for _ in range(3)] for _ in range(3)]

    def display_board(self):
        """
        Display the current state of the Tic-Tac-Toe board.
        """
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def check_winner(self, player):
        """
        Check if the given player has won the game.

        Args:
            player (str): The player to check ('X' or 'O').

        Returns:
            bool: True if the player has won, False otherwise.
        """
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]):
            return True
        if all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def check_tie(self):
        """
        Check if the game is a tie.

        Returns:
            bool: True if the game is a tie, False otherwise.
        """
        return all([cell != " " for row in self.board for cell in row])

    def switch_player(self):
        """
        Switch the current player from 'X' to 'O' or from 'O' to 'X'.
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self, row, col):
        """
        Make a move on the board at the specified row and column.

        Args:
            row (int): The row index (0, 1, or 2).
            col (int): The column index (0, 1, or 2).

        Returns:
            bool: True if the move was successful, False if the cell is already occupied.
        """
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def minimax(self, is_maximizing):
        """
        The Minimax algorithm to determine the best move for the computer.

        Args:
            is_maximizing (bool): True if the algorithm is maximizing, False if minimizing.

        Returns:
            int: The score of the best move.
        """
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if self.check_tie():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == " ":
                        self.board[row][col] = "O"
                        score = self.minimax(False)
                        self.board[row][col] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == " ":
                        self.board[row][col] = "X"
                        score = self.minimax(True)
                        self.board[row][col] = " "
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        """
        Determine the best move for the computer using the Minimax algorithm.

        Returns:
            tuple: The row and column indices of the best move.
        """
        best_score = -float('inf')
        move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    self.board[row][col] = "O"
                    score = self.minimax(False)
                    self.board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move

    def play(self):
        """
        Start the Tic-Tac-Toe game and handle the game loop.
        """
        mode = input("Select game mode (1: Player vs Player, 2: Player vs Computer): ")

        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn")

            if mode == "2" and self.current_player == "O":
                row, col = self.best_move()
                print(f"The computer selected row {row} and column {col}")
            else:
                try:
                    row = int(input("Select a row (0, 1, 2): "))
                    col = int(input("Select a column (0, 1, 2): "))
                    if row not in range(3) or col not in range(3):
                        raise ValueError
                except ValueError:
                    print("Invalid input. Please enter numbers between 0 and 2.")
                    continue

            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.display_board()
                    print(f"Player {self.current_player} has won!")
                    break

                if self.check_tie():
                    self.display_board()
                    print("It's a tie!")
                    break

                self.switch_player()
            else:
                print("Cell occupied, choose another.")