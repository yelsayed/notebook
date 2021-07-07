"""
Note on Merge Sort

The idea in merge sort is that you take an array apart until it's smallest
pieces. There is one base case in the recursion, that len(array) == 1 is sorted.
When you merge two sorted arrays you can go through both once and just
interweave the two arrays. This is done in linear time.

Merging two sorted arrays
   i
[1,5]
[4,8,9]
   j

[1,4,...]

Time -> O(N*logN)
Space -> O(N) as you're creating a ton of new arrays but the max is N

Note after coding it: Wow... I got it first time. This makes me happy.
"""

import math


def merge(left, right):
    """ Assumes both left and right are sorted """
    final_array = []
    i = 0
    j = 0
    n = len(left)
    m = len(right)

    # This is an additional thing that I did from my own brain.
    # When going through the lists, instead of checking if the pointer at each
    # list is beyond the limit, just set infinity so that the other pointer
    # stops and waits until the other one finishes. By the time the other
    # pointer reaches the limit the while loop would've exited
    left.append(math.inf)
    right.append(math.inf)

    while i < n or j < m:
        # This part is straightforward
        if left[i] <= right[j]:
            final_array.append(left[i])
            i += 1
        else:
            final_array.append(right[j])
            j += 1

    return final_array


def merge_sort(array):
    if len(array) == 1:
        # We know for sure that it's sorted at this point
        return array

    mid_point = len(array) // 2

    # Break it into left and right
    left = array[:mid_point]
    right = array[mid_point:]

    # Sort the left and the right
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge the left and the right
    return merge(sorted_left, sorted_right)


print(merge_sort([-1, 3, -5, 87, 2, 57, 2, 8]))
