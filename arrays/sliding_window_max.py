"""
Note on Max of Sliding Window
https://leetcode.com/problems/sliding-window-maximum/

Initial idea:
Keep a Queue of size k. Keep a pointer of where the sliding window is in the
array.

The first max is max(nums[:k])
The pointer starts off at position nums[k] of the array, and everything
nums[:k] is in the queue that we create.
For now, to get the max call max().

We stop when k == len(nums).

Time -> O(K*N) since the big O of max is O(K) everytime, for N times
Space -> O(K)

Another solution is to make a max heap and keep pushing
and popping from it. But the problem is, we need to know the
index of each element in the heap. So one thing we could do
is have a dictionary with us that points to the locations
of the elements in the heap.

When we move through the array we see which element we're popping
and we find it in our heap using the dictionary, then we set it
to infinity.

Time -> O(N*LogK)
Space -> O(K)

While this is a good solution, there is a better solution on the tail
of this solution.

The issue here is that the heap solution is too complicated.

A better way is to keep the values in decreasing order without over
complicating the priority queue.

You know that if a value enters the queue that is bigger than all the
other values in the queue then this will be the returned value
until it encounters a new large value. So in the queue just make sure
that it's in decreasing order by popping everything that is smaller
than the current guy.

[1,3,-1,-3,5,3,6,7]
[1]
[3]
[3, -1]
[3,-1,-3]
full queue
pop 3
[5]
[5,3]
[6]

This is so close. The issue is that the maximum falls out
of the queue but the queue thinks it still exists.

The key here is to keep track of the indices and check if the
index of the max falls out of the list or not.
"""

from typing import List
from collections import deque


# Initial attempt was O(KN) and it was too slow, the problem is
# the use of max() is O(K) everytime.
def max_sliding_window_slow(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return [max(nums)]

    if k == 1:
        return nums

    q = deque(nums[:k], maxlen=k)
    max_window = [max(q)]

    while k < len(nums):
        q.popleft()
        q.append(nums[k])

        max_window.append(max(q))
        k += 1

    return max_window


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    if k == 1:
        return nums

    if k == len(nums):
        return [max(nums)]

    max_window = []
    deq = deque([])

    for i in range(len(nums)):
        # Remove all the elements smaller than
        # the current elem we're looking at
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()

        # Add the current elem to the queue
        # We know for sure that the queue is sorted
        # from biggest to smallest.
        deq.append(i)

        # If the current largest element is outside
        # the window, then pop it
        if deq[0] <= i - k:
            deq.popleft()

        # Then we know that this is the largest element
        # that is in the window
        if i + 1 >= k:
            max_window.append(nums[deq[0]])

    return max_window
