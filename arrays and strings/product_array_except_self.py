"""
Note on Product Array Except Self problem
https://leetcode.com/problems/product-of-array-except-self/

We have to find the product of the whole array except for that point in the
array. We have to do this in O(N) time. We can't use division.

Initial idea:
Build all the prefix products and all the suffix products
iteratively and store the products in a list.

[1,2,3,4]
prefixes are [], [1], [1,2], [1,2,3]
suffixes are [2,3,4], [3,4], [4], []

Final array should have the product of
the prefix and suffix.

Time -> O(3N) since we're going through the list three times
Space -> O(3N)

There is a followup, can we do this in O(N) Time and O(1) **Extra** Space.
O(1) space just entails that we're coming up with the prefix product and the
suffix product on the fly.

Note: We can actually use the output array.

I was able to solve this by going through the array once and calculating the
prefix product. Then going through it on the way back and keeping track of
the prefix product (without using the array).

Time -> O(2N) since we're going through the list twice
Space -> O(1) since we're not using any extra space
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    product = []

    suffix_array = [1] * n
    prefix_array = [1] * n

    # Build prefixes
    for i in range(1, n):
        prefix_array[i] = nums[i - 1] * prefix_array[i - 1]

    # Build suffixes
    for i in range(n - 2, -1, -1):
        suffix_array[i] = nums[i + 1] * suffix_array[i + 1]

    # Multiple suffix and prefix to get the output at each node
    for i in range(n):
        product.append(suffix_array[i] * prefix_array[i])

    return product


def product_except_self_space_efficient(nums: List[int]) -> List[int]:
    n = len(nums)
    product = [1] * n

    # Build prefixes
    for i in range(1, n):
        product[i] = product[i - 1] * nums[i - 1]

    # Build suffixes by keeping track of just one
    # element.
    suffix_prod = 1
    for i in range(n - 2, -1, -1):
        suffix_prod *= nums[i + 1]
        product[i] = suffix_prod * product[i]

    return product
