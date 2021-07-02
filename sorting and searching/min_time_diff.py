"""
Note on Minimum time difference
https://leetcode.com/problems/minimum-time-difference/

My initial idea for this question was to keep things in a heap and then compare
them. I would compare the largest and smallest, the smallest and smallest,
the largest and largest. But this is a terrible idea.

This is a bad idea because there might be two points on this list that
are in the middle that have a difference of zero.

Note from when I was angry at myself:
Using heaps is a dumb idea... use your brain ffs
Here's the lesson from this question, before using heaps
try to sort first. Think about the difference between 
heaps and sorting. Heaps are useful bas mesh lekol 7aga.

Anyways, the solution has the following complexity:
Time -> O(N*logN) for sorting.
Space -> O(N) to store the sorted array
"""

from typing import List


def diff(point1, point2):
    # The diff was the tricky part, because you want to make sure that if
    # something has more than 12 hour difference, then it's actually
    # 12 - (difference % 12).
    d = abs(point2 - point1)
    return 720 - (d % 720) if d >= 720 else d


def find_min_difference(time_points: List[str]) -> int:
    min_diff = 1441
    time_in_minutes = sorted(
        [(int(point[:2]) * 60) + int(point[3:]) for point in time_points]
    )

    for i in range(len(time_in_minutes)):
        # Notice how I didn't start i from 1, because the smallest time
        # and the largest time should be compared.
        current_time = time_in_minutes[i]
        prev_time = time_in_minutes[i - 1]

        d = diff(current_time, prev_time)

        # Zero is the smallest it can be, this cuts computing time by a lot.
        if d == 0:
            return d

        min_diff = min(min_diff, d)

    return min_diff
