# Note on Heaps
# Heaps can be used to implement priority queues and kth largest/smallest

import math
from heapq import heappop, heappush, heapify


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining heap invariant
# heapify - transform list into heap, in place, in linear time

# Heaps generally are a great way to implement priority queues in real systems

class MinHeap:
    def __init__(self):
        # [4,3,1,2]
        #  0 1 2 3
        # 4 -> 3,1
        # 3 -> 2
        # Children are at (i * 2 + 1, i * 2 + 2)
        # Parent is at (i - 1 // 2)
        self.heap = []

    def insert(self, key):
        return heappush(self.heap, key)

    def get_min(self):
        return heappop(self.heap)

    def get_parent_index(self, index):
        """ Index of the parent for the current array """
        return (index - 1) // 2

    def sift_up(self, index):
        if index == 0 or index >= len(self.heap):
            return

        parent_index = self.get_parent_index(index)
        child = self.heap[index]
        parent = self.heap[parent_index]

        if child < parent:
            self.heap[parent_index] = child
            self.heap[index] = parent
            self.sift_up(parent_index)

    def set_key(self, index, new_val):
        self.heap[index] = new_val
        self.sift_up(index)

    def delete_key(self, index):
        self.set_key(index, -math.inf)
        self.get_min()


# A class for Max Heap
class MaxHeap(MinHeap):
    def insert(self, key):
        """ Insert into the heap """
        super(MaxHeap, self).insert(-key)

    def set_key(self, index, new_val):
        super(MaxHeap, self).set_key(-new_val)

    def get_max(self):
        return -super(MaxHeap, self).get_min()

    def __str__(self):
        return str(self.heap)


"""
Another thing that is interesting about this is how you can do heap sorting.
Heap sorting is very simple, just heapify and get the smallest element n times.
This will give you the acsending order of the elements.

Time -> O(N*LogN), popping is LogN and you're doing that N times
Space -> O(N), heapify is done in place, so it's actually O(1) in terms of aux
"""


def heap_sort(array):
    heapify(array)
    return [heappop(array) for i in range(len(array))]
