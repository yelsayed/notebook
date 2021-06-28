"""
Note on Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Initial Solution
[[0,30],[5,10],[15,20]]

[0,30] overlaps [5,10] and [15,20] so that's two for each
[5,10] doesn't overlap [15,20] so it will stay the same answer

We can keep a score array
ex: [[0,30],[5,10],[7,17],[15,20]]
[1, 2, 3, 2]

Time -> N^2
Space -> N


0 ------------------ 30
   5 --- 10
     7 ------- 17
       8 --- 16
         15 ----- 20

ex: [[1,8],[6,20],[9,16],[13,17]]
            tail          head
1 ----------- 8
         6 ---------------------- 20 | score 2
                 9 ------ 16 | score 1
                    13 ------ 17 | score 2

"""

from typing import List


# Works but too slow
def is_overlapping(interval1, interval2):
    s1 = interval1[0]
    e1 = interval1[1]

    s2 = interval2[0]
    e2 = interval2[1]

    return s1 < e2 and s2 < e1


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    intervals = sorted(intervals, key=lambda x: x[0])

    n = len(intervals)
    scores = [1] * n

    for i in range(n):
        curr_interval = intervals[i]
        for j in range(i + 1, n):
            next_interval = intervals[j]
            if is_overlapping(curr_interval, next_interval):
                scores[j] += 1

    return max(scores)


"""
After much trial, I just realized that this question has either a 
really cool trick or a heap implementation.

I didn't understand how the heap solution works at all honestly.
So instead I'm going to go with the other solution.

The really interesting observation about this problem is that
instead of jumping into the solution directly, an easier method
of solving it is by visualizing the real life implications of
this problem.

Observation: It doesn't matter what the duration of a meeting is,
             it matters IF a meeting ended.

If the start times and end times are sorted, and the end times
are getting lined up in terms of how soon they end, then until the
first time has passed, no meeting has ended, right? Which means
for every starting time that is less then the first end time, 
a meeting room has to be allocated.

Okay let's do this. Simple implementation.

[[0,30],[5,10],[15,20]]

 e
[10,20,30]
[0,5,15]
 s
At this point we know that there is a meeting that starts at 0
and ends at 10. Which means we need at least 1 room.

 e
[10,20,30]
[0,5,15]
   s
At this point we know that there is another meeting that started
while the same meeting still ends at 10. So we need 2 rooms.

 e
[10,20,30]
[0,5,15]
     s
At this point we know a meeting starts at 15, but the meeting at
10 has ended (whatever it was) which means that we can reuse that
room that just got free. So we need 1 room at this point.

    e
[10,20,30]
[0,5,15]
     s
Here we know a meeting is ongoing until 20 meaning we need another 
meeting room and we're done because no new meeting starts. So 
meaning for the final interval we will need 2 rooms.

The max number is 2
"""


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    start_times, end_times = zip(*intervals)
    start_times = sorted(list(start_times))
    end_times = sorted(list(end_times))

    s_ptr = 0
    e_ptr = 0
    rooms = 0
    max_rooms = rooms

    while s_ptr < len(start_times) and \
            e_ptr < len(end_times):
        start_time = start_times[s_ptr]
        end_time = end_times[e_ptr]

        # a meeting has started and one of the end times
        # is still there
        if start_time < end_time:
            rooms += 1
            s_ptr += 1

        # a meeting has ended
        else:
            rooms -= 1
            e_ptr += 1

        max_rooms = max(max_rooms, rooms)

    return max_rooms
