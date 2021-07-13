"""
Note on Reverse String
https://leetcode.com/problems/reverse-words-in-a-string-ii/

Initial Idea:
This is an interesting question to do in O(1) space.

Keep track of where is the last word you pushed and push behind it.
Initially it's at index n-1.

Go through the string, pop from the left, push to where the
last index is. When you encounter a space, update the stopper
and push the space.

stopper = -1
["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

push at -1, until you encounter a space

stopper = -1
counter = 1
["h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e","t"]

stopper = -1
counter = 2
["e"," ","s","k","y"," ","i","s"," ","b","l","u","e", "t","h"]

stopper = -1
counter = 3
[" ","s","k","y"," ","i","s"," ","b","l","u","e", "t","h","e"]

At this point you update the stopper to be stopper - counter
stopper = -4
counter = 1
["s","k","y"," ","i","s"," ","b","l","u","e"," ","t","h","e"]

You do the same for "s","k","y"
stopper = -4
counter = 3
[" ","i","s"," ","b","l","u","e","s","k","y"," ","t","h","e"]

This works well but there are two problems:
1) When it comes to working with indices and you're modifying the list as you're
   working on it, it's hard to get right: it's almost slippery.
2) This isn't an O(N) solution because inserting shifts all the elements and
   you're inserting N times.. So it's an O(N^2) solution.

A better solution which I might revisit later is by reversing the whole string
and then using two pointers to reverse each word. That's actually linear.
"""

from typing import List


def reverse_words(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    stopper = len(s)
    counter = 0

    while counter < len(s):
        counter += 1

        if s[0] == " ":
            stopper = len(s) - counter
            s.insert(stopper + 1, s[0])
        else:
            s.insert(stopper, s[0])

        s.pop(0)
