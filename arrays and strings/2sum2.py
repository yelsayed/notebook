# Note on 2 sum II
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


# This is similar to the last problem but with a sorted array. When you have a
# sorted array you can solve the problem using two pointers. The first pointer
# would be in the beginning of the array and the other would be at the end.
# Since it's sorted, the highest element is in the right of the array, and the
# smallest is in the opposite end. Add the result of the two pointers, if it's
# higher than the target move it backwards from the right, if it's too low move
# it upwards from the left. w bas

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    head = len(numbers) - 1
    tail = 0

    while head >= 0 and tail < len(numbers):
        if tail == head:
            break  # no duplicates

        tail_number = numbers[tail]
        head_number = numbers[head]

        if tail_number + head_number == target:
            return [tail + 1, head + 1]

        if tail_number + head_number > target:
            head -= 1

        if tail_number + head_number < target:
            tail += 1

    return []

# Another solution someone mentioned is binary search
