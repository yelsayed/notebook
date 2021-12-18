"""
Note on Maximum Area of a piece of cake problem
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/solution/

Initial Idea:

Create a 2d array and mark the cells with their appropriate cut.
Then later go through the 2d array and count the number of unique cuts that
you've made.

Problem with this is that it's too hard to code. And it was too slow to execute.
"""

from typing import List
from collections import defaultdict


def max_area_slow(
        h: int,
        w: int,
        horizontal_cuts: List[int],
        vertical_cuts: List[int]
) -> int:
    max_num = (10 ** 9) + 7
    high = 0
    horizontal_cuts = [0] + sorted(horizontal_cuts) + [h]
    vertical_cuts = [0] + sorted(vertical_cuts) + [w]

    cake = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(None)
        cake.append(row)

    cuts = defaultdict(int)

    for i in range(1, len(vertical_cuts)):
        vertical_mark = f"v{i}"
        for j in range(vertical_cuts[i - 1], vertical_cuts[i]):
            for i1 in range(h):
                cake[i1][j] = vertical_mark

    for i in range(1, len(horizontal_cuts)):
        mark = f"h{i}"
        for j in range(horizontal_cuts[i - 1], horizontal_cuts[i]):
            row = cake[j]
            for i1 in range(len(row)):
                row[i1] += mark
                cuts[cake[j][i1]] += 1
                high = max(cuts[cake[j][i1]], high)

    return high % max_num


def max_area(
        h: int,
        w: int,
        horizontal_cuts: List[int],
        vertical_cuts: List[int]
) -> int:
    max_num = (10 ** 9) + 7
    horizontal_cuts = [0] + sorted(horizontal_cuts) + [h]
    vertical_cuts = [0] + sorted(vertical_cuts) + [w]

    horizontal_gaps = [
        horizontal_cuts[i] - horizontal_cuts[i - 1] for i in
        range(1, len(horizontal_cuts))
    ]

    vertical_gaps = [
        vertical_cuts[i] - vertical_cuts[i - 1] for i in
        range(1, len(vertical_cuts))
    ]

    return max(horizontal_gaps) * max(vertical_gaps) % max_num
