# This note is to study the missing number problem

from typing import List
from collections import defaultdict


# The problem goes, or as legends have it, that there is one number in an array
# that is missing, and we are tasked with finding it.
# The unsorted array goes from [0,n] and there exists an x that is missing.

# Dumb solution
# The dumb solution is to sort the array and just check. This is O(nlogn) time
# complexity.
# I won't even bother writing the code for this :D

# Hashtables solution
# This solution involves creating a hashtable with all the number from [0,n] and
# making the values all `False` initially, then later on iterating through the
# input and checking the hashtable to make it True. There will be one element
# that is False and that's the one that's missing.

# This is O(n) time but it's also O(n) space. So it's not the best solution.
def missing_numbers_hash(nums: List[int]) -> int:
    n = len(nums)
    d = {}

    # Create the hashtable
    for i in range(n + 1):
        d[i] = d.get(i, False)

    # Loop through array and set a dictionary value to True
    for i in nums:
        d[i] = True

    # Check if the value is not `True` (which means it's not seen) and return
    # the key.
    for key, value in d.items():
        if not value:
            return key


# This is a nice solution but we can do better

# Smart solution
# We know that if there is a missing number, the sum of the whole array
# should not equal the sum of all the numbers in the range [0,n]. The difference
# is the number that is missing.

def missing_numbers(nums: List[int]) -> int:
    current_sum = sum(nums)
    expected_sum = sum(range(len(nums) + 1))
    return expected_sum - current_sum

# Doesn't even need comments it's so clean.
