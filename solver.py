import numpy as np

from dfs import DFS
from dls import DLS
from bfs import BFS
from ids import IDS
from bidirectional_search import BidirectionalSearch
from a_star import AStar
from eight_puzzle import EightPuzzle


puzzle = EightPuzzle()
print(puzzle)
astar = AStar(puzzle)
astar.solve('tiles')
