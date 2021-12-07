from eight_puzzle import *


class DFS:
    def __init__(self, puzzle: EightPuzzle):
        self.puzzle = puzzle
        self.directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]

    def solve_iterative(self):
        visited = set()
        stack = [self.puzzle]

        while stack:
            current_board = stack.pop()
            if current_board.is_solved():
                current_board.print_solution()
                return
            elif current_board.to_tuple() in visited:
                continue
            else:
                visited.add(current_board.to_tuple())
                for direction in self.directions:
                    new_board = current_board.move(direction)
                    if isinstance(new_board, bool):
                        continue
                    else:
                        stack.append(new_board)

    def solve_recursive(self):
        visited = {self.puzzle.to_tuple()}

        def helper(board: EightPuzzle):
            if board in visited:
                return
            visited.add(board.to_tuple())
            if board.is_solved():
                board.print_solution()
                return
            for direction in self.directions:
                new_board = board.move(direction)
                if isinstance(new_board, bool):
                    return
                helper(new_board)

        helper(self.puzzle)
