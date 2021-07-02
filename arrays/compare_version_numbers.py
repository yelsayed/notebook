"""
Note on Comparing version numbers
https://leetcode.com/problems/compare-version-numbers/

This is an easy problem. Basically just go through both versions in parallel
and check the version numbers.

7.2.1
7.2.1.3
    ^

When you encounter a blank just put 0 instead. It will be the same

Time -> O(max(N, M) + N + M) because we're also doing a split.
Space -> O(N + M) we're storing the arrays after splitting.
"""


def compare_version(version1: str, version2: str) -> int:
    # Split em
    version1 = version1.split('.')
    version2 = version2.split('.')

    # Go for the max
    for i in range(max(len(version1), len(version2))):
        # Get the current revision by the index if it's less
        if i < len(version1):
            curr_v1 = int(version1[i])
        else:
            curr_v1 = 0

        # Same same
        if i < len(version2):
            curr_v2 = int(version2[i])
        else:
            curr_v2 = 0

        # Return according to the question
        if curr_v1 < curr_v2:
            return -1

        if curr_v1 > curr_v2:
            return 1

    return 0
