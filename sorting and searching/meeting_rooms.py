"""
Note on Meeting Rooms Problem
https://leetcode.com/problems/meeting-rooms/

The problem is to see

Initial Idea:
Find the overlap between the intervals after sorting them. This is a simple
O(N*logN) solution. Something that we can do that is simpler is compare the
end of last interval and the start of this interval, if the start is less
than the end then we know there is some overlap, and we cannot have someone
attend all the meetings if there is overlap.

Time -> O(N*logN)
Space -> O(N) since you're storing the array even though sorting is O(logN)
"""

from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    # Sort it
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Loop it
    for i in range(1, len(sorted_intervals)):
        interval = sorted_intervals[i]
        prev_interval = sorted_intervals[i - 1]

        # We don't check if it's >= because it's okay if it's equal
        if prev_interval[1] > interval[0]:
            return False

    # Bop it!
    return True
