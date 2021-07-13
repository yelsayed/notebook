# This note is to study the question of 2-sum.

from typing import List


# We have to find two numbers in an array that sum up to a target
# The numbers can be negative and the array is unsorted. The values of the
# numbers are not unique.

# Example is you have an array [2, 7, 11, 15] with target 22. The solution
# is 7 and 15 and return value would be [1,3]

# First solution
# The idea of the first solution is to sort it, which is already O(nlogn), and
# then look at the left most element (smallest) and right most element (largest)
# If the sum of these two elements is bigger than the target then move right
# index to the left, making the sum smaller. If the sum is too small then do
# the opposite. This is O(n) in terms of iteration.

# Little bit better than O(n2) solution
def two_sum_kinda_slow(nums: List[int], target: int) -> List[int]:
    # Because we want to return the indices not the actual values, we store
    # the indices with the values. This is still O(n).
    new_nums = []
    for index, value in enumerate(nums):
        new_nums.append((value, index,))

    # We then sort based on the value not the index and hence the use of the
    # `key=lambda...`. This is the most expensive operation.
    nums = sorted(new_nums, key=lambda x: x[0])
    length = len(nums)

    # Set the "handles" at each end
    left_index = 0
    right_index = length - 1

    # Keep going until one of the handles is out of bounds
    while left_index < length and right_index > 0:
        # Don't forget to access the first element because it contains our
        # values
        i = nums[left_index][0]
        j = nums[right_index][0]

        s = i + j

        # If the sum is the target then return the indices which is the second
        # element in the tuple
        if s == target:
            return [nums[left_index][1], nums[right_index][1]]

        # If the sum is too high then take it down a notch
        if s > target:
            right_index -= 1

        # If the sum is too low then move it up
        if s < target:
            left_index += 1


# Second solution
# This solution aims to be an O(n) solution. To iterate through this once it's
# better to think of the distance away from the target an element is. Meaning
# if your target is 8 and you're iterating through the list on element x.
# Whatever the second element has to be it must be exactly 8 - x. So simply
# create a dictionary with all the values mapped to the indices (having a
# dictionary makes it so that there is a constant time lookup and access).

# Initial solution
# Initially I created the entire hashtable from the values and indices

def two_sum_wrong(nums: List[int], target: int) -> List[int]:
    # Here I create a map from the values to their indices. The values will
    # make for an easy look up and make the requirement of saving the values
    # simple.
    value_index_store = {}
    for index, value in enumerate(nums):
        value_index_store[value] = index

    # Here I just iterate to see the distance between the solution and the
    # current value, if it exists in the good ol' dictionary then return that
    for index, value in enumerate(nums):
        distance = target - value
        if distance in value_index_store:
            return [index, value_index_store[distance]]


# This doesn't work on duplicate values, for example [3,2,4] with target 6 will
# return [0,0]... sad :'(

# A better approach is to look up the previous values inputted in the dictionary
# so that you don't have duplicates.

def two_sum(nums: List[int], target: int) -> List[int]:
    value_index_store = {}

    for index, value in enumerate(nums):
        distance = target - value
        if distance in value_index_store:
            return [value_index_store[distance], index]

        # Here you're building the dictionary so that you're not worried about
        # duplicates, it adds after considering the element.
        value_index_store[value] = index
