"""
loveleetcode
 i

{
l -> {count: 1, index: 0}
e -> {count: 2, index: 1}
t -> {count: 1, index: 3}
c ->
}

Time -> O(2N)
Space -> O(N)

Simple question, really.
"""

from collections import defaultdict


def first_unique_char(s: str) -> int:
    min_index = len(s)
    count_dict = defaultdict(lambda: (0, 0))

    for i, c in enumerate(s):
        count, index = count_dict[c]
        count_dict[c] = (count + 1, i)

    for key, value in count_dict.items():
        if value[0] == 1:
            min_index = min(min_index, value[1])

    return min_index if min_index < len(s) else -1
