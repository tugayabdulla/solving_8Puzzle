from enum import Enum

import numpy as np
from numpy.random import choice


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class EightPuzzle:

    def __init__(self, board: np.array = None, path: list = None):
        if board is None:
            while True:
                self.board1d = choice(9, 9, replace=False)
                if self.is_solvable():
                    break
            self.board = self.board1d.reshape(3, 3)
            self.path = []
        else:
            self.board = board
            self.board1d = board.reshape(9)
            self.path = path

    def __str__(self):
        return ' ' + str(self.board).replace('0', ' ').replace('[', '').replace(']', '')

    def find_zero(self):
        """Finds indices of the zero"""
        for row in range(3):
            for col in range(3):
                if self.board[row, col] == 0:
                    return row, col

    def _move_right(self):
        """Move right"""
        row, col = self.find_zero()
        board = np.copy(self.board)
        path = self.path.copy()
        if col == 0:
            return False

        board[row, col] = board[row, col - 1]
        board[row, col - 1] = 0
        return EightPuzzle(board, path + [self])

    def _move_down(self):
        """Move down"""
        row, col = self.find_zero()
        board = np.copy(self.board)
        path = self.path.copy()
        if row == 0:
            return False

        board[row, col] = board[row - 1, col]
        board[row - 1, col] = 0
        return EightPuzzle(board, path + [self])

    def _move_left(self):
        """Move left"""
        row, col = self.find_zero()
        board = np.copy(self.board)
        path = self.path.copy()
        num_cols = self.board.shape[1]
        if col == num_cols - 1:
            return False

        board[row, col] = board[row, col + 1]
        board[row, col + 1] = 0
        return EightPuzzle(board, path + [self])

    def _move_up(self):
        """Move up"""
        row, col = self.find_zero()

        board = np.copy(self.board)
        path = self.path.copy()
        num_rows = self.board.shape[0]
        if row == num_rows - 1:
            return False

        board[row, col] = board[row + 1, col]
        board[row + 1, col] = 0
        return EightPuzzle(board, path + [self])

    def move(self, direction):
        """Move to the direction"""
        if direction == Direction.UP:
            return self._move_up()
        elif direction == Direction.RIGHT:
            return self._move_right()
        elif direction == Direction.DOWN:
            return self._move_down()
        elif direction == Direction.LEFT:
            return self._move_left()
        else:
            raise ValueError('Invalid direction')

    def is_solvable(self):
        """Checking if generated puzzle is solvable by computing inversions"""
        inversion_count = 0
        for i in range(0, 8):
            for j in range(i + 1, 9):
                inversion_count += self.board1d[i] > self.board1d[j] and self.board1d[i] * self.board1d[j] != 0

        return inversion_count % 2 == 0

    def is_solved(self):
        """Checking if the puzzle is solved"""
        return all(self.board1d == [1, 2, 3, 4, 5, 6, 7, 8, 0])

    def to_tuple(self):
        """Convertion to tuple for hashing"""
        return tuple(self.board1d)

    def print_solution(self):
        for p in self.path:
            print(str(p))
            print('=========================')
        print(self)

        pass
