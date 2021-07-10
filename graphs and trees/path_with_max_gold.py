"""
Note on Path with Maximum Gold
https://leetcode.com/problems/path-with-maximum-gold/

You can take every point in the graph and say
that this point is the maximum of a point that
is next to it, plus this point.

[
  [0, 6, 0],
  [5, 8, 7],
  [0, 9, 0]
]
The correct path for this is 9 -> 8 -> 7.

max_gold(7) == 7 + max_gold(8)

max_gold(8) == max(max_gold(6), max_gold(5), max_gold(9)) + 8.

The only issue with this solution is that you're going to be
going to be repeating steps. One easy way of fixing this is by
marking the point we visited as 0 (or negative).

We have to clone the grid every time.
^ Instead of cloning, revert the value once you're done
  with it, this is like DFS with back tracking.

This is DFS with backtracking :D

Time -> O(3^(M+N)*(M+N))
Space -> O(1)
"""

from typing import List


def get_maximum_for_cell(self, grid, i, j):
    if i >= len(grid) or j >= len(grid[0]) or \
            i < 0 or j < 0 or grid[i][j] == 0:
        return 0

    # Mine the treasure
    current_treasure = grid[i][j]

    # Mark this spot as visited
    grid[i][j] = 0

    directions = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    max_treasure = 0

    for ii, jj in directions:
        last_treasure = self.get_maximum_for_cell(grid, ii, jj)
        max_treasure = max(max_treasure, last_treasure)

    # When you're done mining, revert this spot for other iterations
    grid[i][j] = current_treasure
    return current_treasure + max_treasure


def get_maximum_gold(self, grid: List[List[int]]) -> int:
    high = 0
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            cell_max = self.get_maximum_for_cell(grid, i, j)
            high = max(high, cell_max)

    return high
