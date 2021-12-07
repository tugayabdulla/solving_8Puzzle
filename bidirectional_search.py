from collections import deque

import numpy as np

from eight_puzzle import EightPuzzle, Direction


class BidirectionalSearch:
    def __init__(self, puzzle: EightPuzzle):
        self.puzzle = puzzle
        self.directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]

    def solve(self):
        visited_up = {}
        solved_puzzle = EightPuzzle(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), [])
        visited_down = {}
        queue_up = deque([self.puzzle])
        queue_down = deque([solved_puzzle])

        while True:
            for _ in range(len(queue_up)):
                board_up = queue_up.popleft()
                if board_up.to_tuple() in visited_down:
                    print('up')
                    print(str(board_up))

                    down_puzzle = visited_down[board_up.to_tuple()]
                    full_path = board_up.path + [down_puzzle] + down_puzzle.path[::-1][:-1]
                    solved_puzzle_with_full_path = EightPuzzle(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), full_path)
                    solved_puzzle_with_full_path.print_solution()
                    return
                elif board_up.to_tuple() in visited_up:
                    continue
                else:
                    visited_up[board_up.to_tuple()] = board_up

                    for direction in self.directions:
                        new_board = board_up.move(direction)
                        if not isinstance(new_board, bool):
                            queue_up.append(new_board)
            for _ in range(len(queue_down)):
                board_down = queue_down.popleft()
                if board_down.to_tuple() in visited_up:
                    print('down')
                    up_puzzle = visited_up[board_down.to_tuple()]
                    print(str(board_down))
                    full_path = up_puzzle.path + [board_down] + board_down.path[::-1][:-1]
                    solved_puzzle_with_full_path = EightPuzzle(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), full_path)
                    solved_puzzle_with_full_path.print_solution()
                    return
                elif board_down.to_tuple() in visited_down:
                    continue
                else:
                    visited_down[board_down.to_tuple()] = board_down

                    for direction in self.directions:
                        new_board = board_down.move(direction)
                        if not isinstance(new_board, bool):
                            queue_down.append(new_board)
