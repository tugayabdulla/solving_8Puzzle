from collections import deque

from eight_puzzle import EightPuzzle, Direction


class BFS:
    def __init__(self, puzzle: EightPuzzle):
        self.puzzle = puzzle
        self.directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]

    def solve(self):
        visited = {self.puzzle}
        queue = deque([self.puzzle])

        while len(queue) > 0:
            current_board = queue.popleft()
            if current_board.is_solved():
                current_board.print_solution()
                return
            elif current_board.to_tuple() in visited:
                continue
            else:
                for direction in self.directions:
                    new_board = current_board.move(direction)
                    if not isinstance(new_board, bool):
                        queue.append(new_board)
