"""
Note on K Frequency
https://leetcode.com/problems/top-k-frequent-elements/

Initial idea:
Make a dictionary of the elements and their frequencies (N Time and Space).
Reverse the hash map (linear still).
In case of clashes append to list (use defaultdict).
Make a Max Heap. Pop K times and get the value of the list and push into result.

Time -> K logN
Space -> N
"""
from typing import List
from collections import defaultdict
from heapq import heapify, heappop


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    result = []

    # return zero on access
    frequencies = defaultdict(lambda: 0)

    for num in nums:
        # we'll use a min heap of negative to
        # make it max heap
        frequencies[num] -= 1

    # Reverse the dictionary and append all the keys in a list in case of
    # clashes
    reversed_freq = defaultdict(list)

    for key, val in frequencies.items():
        reversed_freq[val].append(key)

    i = 0
    all_keys = list(reversed_freq.keys())
    heapify(all_keys)

    while i < k:
        key = heappop(all_keys)
        val = reversed_freq[key]
        result.extend(val)

        # I was appending by 1 initially, that's wrong since one freq could
        # return multiple keys, so we should pop and check how many we need
        # to pop
        i += len(val)
        
    return result
