"""
Note on the Largest Container problem.
https://leetcode.com/problems/container-with-most-water/

Given heights on a graph, get the two heights that will create a maximum
container size. I explained that terribly, go read the question.
This is a simple question with a tough observation to make.

The simple solution is try each one with each one. This works but is O(N^2).
"""
from typing import List


def max_area_slow(heights: List[int]) -> int:
    high = 0

    for i in range(len(heights)):
        current = heights[i]
        for j in range(i + 1, len(heights)):
            high = max(high, min(current, heights[j]) * (j - i))

    return high


"""
Whenever there is a question that is N^2 because you're trying each value with
each other value I question if one way to optimize is either using a sliding
window or a two pointer approach. For this one I couldn't think of how a two
pointer approach helps at all. 

The hints given in the question made it a lot more clear, which is since you're
maximizing on two aspects, distance and height, first maximize distance and then
get the best height you can get.

This means that you have one pointer at one end of the array, and another in the
beginning. This means that the distance is at a max, at this point you can 
iterate by either moving the head or the tail pointer. The question is based on
what do you iterate?

You iterate based on which is the minimum height, since you cannot increase the
size of the container if the minimum height does not change.

Given this array [1,2,4,3] and you start off at 

[1,2,4,3]
 t     h
 
With the high = 3. If you move only the head to maximize the height, it won't
do anything since t at `1` does not change. So you need to move the minimum.

This works.
"""


def max_area(heights: List[int]) -> int:
    high = 0

    tail = 0
    head = len(heights) - 1

    # We don't want them to pass each other
    while tail < head:
        high = max(high, min(heights[head], heights[tail]) * (head - tail))

        # Quite simple
        if heights[tail] <= heights[head]:
            tail += 1
        else:
            head -= 1

    return high
