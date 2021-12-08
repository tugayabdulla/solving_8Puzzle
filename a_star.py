import heapq

from eight_puzzle import EightPuzzle, Direction


class AStar:

    def __init__(self, puzzle: EightPuzzle):
        self.puzzle = puzzle
        self.directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]

    def solve(self, heuristic: str = 'manhattan'):
        if heuristic == 'manhattan':
            h = self.manhattan_distance
        elif heuristic == 'tiles':
            h = self.mismatched_tiles
        else:
            raise ValueError('Invalid heuristic')
        visited = set()
        queue = [(h(self.puzzle), 0, self.puzzle)]
        while queue:
            current_f, current_distance, current_puzzle = heapq.heappop(queue)
            if current_puzzle.is_solved():
                current_puzzle.print_solution()
                return
            elif current_puzzle.to_tuple() in visited:
                continue
            else:
                for direction in self.directions:
                    new_puzzle = current_puzzle.move(direction)
                    if isinstance(new_puzzle, EightPuzzle):
                        f = h(new_puzzle) + current_distance + 1
                        heapq.heappush(queue, (f, current_distance + 1, new_puzzle))
                visited.add(current_puzzle.to_tuple())

    def manhattan_distance(self, puzzle: EightPuzzle) -> int:
        """
        Calculates the manhattan distance of the tiles from their goal positions.
        """
        distance = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if puzzle.board[i, j] != 0:
                    cur_val = puzzle.board[i, j]
                    correct_row, correct_col = (cur_val - 1) // 3, (cur_val % 3 - 1 if cur_val % 3 != 0 else 2)
                    distance += abs(i - correct_row) + abs(j - correct_col)

        return distance

    def mismatched_tiles(self, puzzle: EightPuzzle) -> int:
        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if puzzle.board[i, j] != 0:
                    cur_val = puzzle.board[i, j]
                    correct_row, correct_col = (cur_val - 1) // 3, (cur_val % 3 - 1 if cur_val % 3 != 0 else 2)
                    if i != correct_row or j != correct_col:
                        count += 1
        return count
