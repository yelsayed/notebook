"""
Note on the longest substring with non-repeating characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

The problem is to find the longest substring with non-repeating characters.

"abcabcbb"
-> 3

One of the issues that this problem has is that it makes you default to the
non-brute force solution.

The key observation here is that you can keep building a substr until you hit
a repeating character. The substring is built via head and tail (tale as old as
time). One thing to do is to keep track of all the characters in a hashmap and
once you encounter them on the head then you increment the tail.

My failure was not knowing when to increment the head and not tracing it on
paper first. This caused me to come up with the first dumb solution.

    |
"abcabcbb"
 |

At this point there is a duplicate, so we increment the tail by one and keep
track of that string "abc".

     |
"abcaccbb"
  |
Here c is duplicate, but it's not where the tail is. So that makes for a harder
problem to solve than just incrementing the tail by one, it needs to increment
until it has passed c.

Let's jump into the solutions.
"""

from collections import defaultdict


# The Dumb Solution
def length_of_longest_substring_dumb(s: str) -> int:
    character_dict = {}
    high = 0
    tail = 0
    head = 0

    while head < len(s):
        index = character_dict.get(s[head])
        substr = s[tail:head]

        if index is not None:
            high = max(high, len(substr))

            tail = index + 1
            head = tail + 1
            # This is where the trouble is, I'm resetting the whole array, it's
            # correct (!) but it's very slow because the head keeps going back
            # to the tail on each duplicate, the worst case is O(n**2)
            character_dict = {s[tail]: tail}
            continue
        else:
            character_dict[s[head]] = head
        head += 1

    # This is another issue with the solution because you can just find it from
    # the loop itself
    high = max(high, len(s[tail:head]))
    return high


"""
Better approach.

This is called the sliding window algorithm. The idea is to keep a window from
tail to head and keep incrementing the head and occasionally incrementing the
tail.

Since you're incrementing the head, you can keep track of all the number of 
unique characters. Once the character in the head is greater than one we know
that there is a duplicate. The tail should be incremented to try and get the 
duplicate out, and as you're incrementing the tail you're decrementing the 
unique characters that you've seen. 

Time Complexity: O(2N) -> O(N) because you can hit every character 
twice in the case that the duplicate is at the end of the string
---
Space Complexity: O(N) + O(1) because you're keeping track of two pointers and a
hashmap of unique characters  
"""


def length_of_longest_substring_sliding_window(s: str) -> int:
    characters = defaultdict(lambda: 0)
    head = 0
    tail = 0

    high = 0

    while head < len(s):
        head_char = s[head]
        characters[head_char] += 1

        # This means we have a duplicate in our current substr, so we should
        # kick it out, as we're trying to kick it out we should be keeping track
        # of the number of unique characters that we're losing when incrementing
        # the tail.
        while characters[head_char] > 1:
            tail_char = s[tail]
            # Remove unique characters
            characters[tail_char] -= 1
            # Move the substr by one
            tail += 1

        # Get the max
        high = max(high, head - tail + 1)
        head += 1

    return high


"""
We can optimize this a little more by storing the indices and then moving the
head up to the index of the repeated character. This is similar to what I was
doing earlier, but it's better because of the max(tail, new_index + 1).
Essentially it means that if the last repeated character is before the tail,
then we already took care of it.
"""


def length_of_longest_substring(s: str) -> int:
    characters = {}
    tail = 0

    high = 0

    for head, head_char in enumerate(s):
        if head_char in characters:
            new_index = characters[head_char]
            # The queen that unravels the problem
            tail = max(tail, new_index + 1)

        characters[head_char] = head
        high = max(high, head - tail + 1)

    return high
