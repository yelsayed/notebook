"""
Note on the the k closest points to the origin question.
https://leetcode.com/problems/k-closest-points-to-origin/


Mistakes I made here were to forget about the cases with points that have the
same distance.

The approach here is to reduce this problem to the Kth largest problem. You
can create a Min Heap of the euclidean distances and get the K smallest
elements.

Time Complexity: O(K*logN) because you need to pop K times from a size N heap
Space Complexity: O(N) Size N heap and dictionary
"""

import math
from collections import defaultdict  # my love
from typing import List
from heapq import heapify, heappop


def euc(point):
    # Get the euclidian distance assuming the second point is (0,0)
    return math.sqrt(point[0] ** 2 + point[1] ** 2)


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = defaultdict(list)  # A cute way of getting empty lists
    closest_points = []

    # Edge case
    if not points:
        return closest_points

    # Map distances to points because there are some points that will have the
    # same distance and we need to return all of them
    for point in points:
        distances[euc(point)].append(point)

    # Make a list of the distances to retrieve them later
    heap = list(distances.keys())
    # Make a heap of the list :D
    heapify(heap)

    i = 0
    # Keep popping k times and store in the return array
    while i < k:
        min_distance = heappop(heap)
        min_point = distances.get(min_distance)
        closest_points += min_point
        i += len(min_point)

    return closest_points
