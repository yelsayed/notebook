"""
Note on Merge Intervals
https://leetcode.com/problems/merge-intervals/

Initial Idea:
We know we should merge two intervals iff
S1 <= E2 & S2 <= E1

This can be proven by taking case by case
S1    E1
   S2    E2
T & T
---
   S1    E1
S2    E2
T & T
---
        S1    E1
S2    E2
F & T
---
S1    E1
         S2    E2
T & F
...

This works well I feel.

Sort the array by the first element and see if there is a merge,
if there is merge the two intervals and continue with current interval.
Otherwise get a new interval.

Time  -> O(N Log N) for the sorting worst case
Space -> depends on the sort, but since we're storing sorted it's O(N)

I overthought this, if it's sorted, you can easily tell if an overlap exists.
Look at the "Meeting Rooms" note.
"""

from typing import List


def is_overlapping(interval1, interval2):
    s1 = interval1[0]
    e1 = interval1[1]

    s2 = interval2[0]
    e2 = interval2[1]

    return s1 <= e2 and s2 <= e1


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    # We append this one since we know it won't overlap with the last interval
    # that way we append it in the loop
    sorted_intervals.append([-1, -1])
    non_overlapping = []

    # start with the first one
    current_interval = sorted_intervals[0]
    for i in range(1, len(sorted_intervals)):
        interval = sorted_intervals[i]

        overlapping = is_overlapping(current_interval, interval)
        if overlapping:
            # If there is an overlap, get the max of the interval and the
            # current merged interval
            max_end = max(current_interval[1], interval[1])
            current_interval = [current_interval[0], max_end]
        else:
            non_overlapping.append(current_interval)
            current_interval = interval

    return non_overlapping
