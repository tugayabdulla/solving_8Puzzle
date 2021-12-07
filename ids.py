from eight_puzzle import *


class IDS:
    def __init__(self, puzzle: EightPuzzle):
        self.puzzle = puzzle
        self.directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]


    def solve(self):
        depth = 0
        while True:
            if self.solve_iterative(depth):
                break
            depth += 1
    def solve_iterative(self, depth):
        visited = set()
        stack = [(self.puzzle, 0)]
        while stack:

            current_board, current_depth = stack.pop()
            if current_board.is_solved():
                current_board.print_solution()
                return True
            elif current_board.to_tuple() in visited:
                continue
            else:
                if current_depth == depth:
                    continue
                visited.add(current_board.to_tuple())
                for direction in self.directions:
                    new_board = current_board.move(direction)
                    if isinstance(new_board, bool):
                        continue
                    else:
                        stack.append((new_board, current_depth+1))
    def solve_recursive(self, depth):
        visited = {self.puzzle.to_tuple()}

        def helper(board: EightPuzzle, current_depth: int):

            if board in visited:
                return
            if current_depth == depth:
                return
            visited.add(board.to_tuple())
            if board.is_solved():
                board.print_solution()
                return True
            for direction in self.directions:
                new_board = board.move(direction)
                if isinstance(new_board, bool):
                    return
                helper(new_board, current_depth + 1)

        return helper(self.puzzle, 0)
