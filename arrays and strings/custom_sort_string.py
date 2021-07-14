"""
Note on Custom Sort String
https://leetcode.com/problems/custom-sort-string/

Initial Idea:
This seems like a simple question that can be done in O(N) time.
If the whole idea is to preserve the order, then we can just move
all the strings that occur in order to the beginning.

order = "cba"
str = "aadebfgcjclc"

Then a valid order would be
"cccbaadefgjl"
Notice how we're moving everything to the beginning.
Should be simple to implement.

Time -> O(N)
Space -> O(N)

Yup, we're done
"""

from collections import Counter


def custom_sort_string(order: str, string: str) -> str:
    order_count = Counter(order)
    suffix = ""
    prefix = ""

    for c in string:
        if c in order_count:
            order_count[c] += 1
        else:
            suffix += c

    for key, value in order_count.items():
        prefix += key * (value - 1)

    return prefix + suffix
