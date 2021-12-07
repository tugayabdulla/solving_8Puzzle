from eight_puzzle import *


class DLS:
    def __init__(self, puzzle: EightPuzzle, depth: int):
        self.puzzle = puzzle
        self.directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]
        self.depth = depth

    def solve_iterative(self):
        visited = set()
        stack = [(self.puzzle, 0)]

        while stack:
            current_board, current_depth = stack.pop()
            if current_board.is_solved():
                current_board.print_solution()
                return
            elif current_board.to_tuple() in visited:
                continue
            else:
                if current_depth == self.depth:
                    continue
                visited.add(current_board.to_tuple())
                for direction in self.directions:
                    new_board = current_board.move(direction)
                    if isinstance(new_board, bool):
                        continue
                    else:
                        stack.append((new_board, current_depth+1))
        print(len(visited))
        print('No solution found')

    def solve_recursive(self):
        visited = {self.puzzle.to_tuple()}

        def helper(board: EightPuzzle, depth: int):

            if board in visited:
                return
            if depth == self.depth:
                return
            visited.add(board.to_tuple())
            if board.is_solved():
                board.print_solution()
                return True
            for direction in self.directions:
                new_board = board.move(direction)
                if isinstance(new_board, bool):
                    return
                helper(new_board, depth + 1)

        if helper(self.puzzle, 0):
            pass
        else:
            print('No solution found')
