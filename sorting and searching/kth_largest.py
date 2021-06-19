"""
Note on Kth largest element in an array.
https://leetcode.com/problems/kth-largest-element-in-an-array/

The simplest way of doing this question is just by sorting and then getting the
list[-k]. This is N*logN.

A better method that is more computationally efficient is maintaining a Max Heap
and keep popping from it.

This question is much simpler in python given the `heapq` library. HeapQ has one
downside however, that there is no functionality for Max Heap. An easy way to
mimic the functionality of Max Heap using Min Heap is to switch the polarity on
all the integers. This way your max is min and vise versa. When getting the max
just flip the signs again.

The complexity of this is N + K*logN since popping from a heap is logN and you
have to do that K times. You also need to map the array once so that's N.
"""

from heapq import heapify, heappop
from typing import List


# Simple but un-interesting way of solving this problem
def simple_find_kth_largest(numbers: List[int], k: int) -> int:
    return sorted(numbers)[-k]


# More interesting way,
def find_kth_largest(numbers: List[int], k: int) -> int:
    # Invert all the numbers
    heap = [-num for num in numbers]
    # Heapify (this is in O(N) time)
    heapify(heap)

    # Pop k times
    for i in range(k):
        max_heap = heappop(heap)

    # Invert one more time
    return -max_heap


# Small note, a great optimization to this problem is to keep a heap with size
# K, that way your complexity becomes logK on each pop. :D
