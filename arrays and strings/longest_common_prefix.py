"""
Note on Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Another easy question that has multiple different solutions. Finding the
longest common prefix is simple, you have to compare character by character
and see where the prefix sequence breaks.

["hello",
 "help",
 "hell"]
  i=1

Initialize common prefix.
Get the first character of the first string.
At i=1, go through each string and compare to see if they match the first
character. If they match, then add that character to the common prefix, if they
don't, return the common prefix.

Time -> O(S) where S is the sum of all the characters.
Space -> O(S) where S is the sum of all the characters.

----
Another solution would be using a Trie.

You can create a Trie once and then traverse the tree using the other strings.
Generate the substring whenever you find a node for the character, then get
the shortest substring.

Time -> O(S) You still need to go through all the characters to build the trie.
Space -> O(S) building a trie from all the characters.
"""
import math

from typing import List


def longest_common_prefix(strings: List[str]) -> str:
    if not strings:
        return ""

    common_prefix = ""

    # This puts us at O(S) space unfortunately
    min_len = min([len(_str) for _str in strings])

    for i in range(min_len):
        last_letter = strings[0][i]

        for _str in strings[1:]:
            curr_letter = _str[i]
            if last_letter != curr_letter:
                return common_prefix
        common_prefix += last_letter

    return common_prefix


class TrieNode:
    def __init__(self):
        self.characters = [None] * 26
        self.end = False


def index(char: str) -> int:
    return ord(char) - ord('a')


def longest_common_prefix_trie(strings: List[str]) -> str:
    if not strings:
        return ""

    max_prefix_len = math.inf
    max_prefix = ""

    root = TrieNode()
    ptr = root

    # Build it once and then search later
    for char in strings[0]:
        node = TrieNode()
        ptr.characters[index(char)] = node

        ptr = node

    for string in strings:
        ptr = root
        common_prefix = ""
        common_prefix_len = 0

        for char in string:
            node = ptr.characters[index(char)]
            if node is None:
                break

            ptr = node
            common_prefix += char
            common_prefix_len += 1

        if common_prefix_len < max_prefix_len:
            max_prefix = common_prefix
            max_prefix_len = common_prefix_len

    return max_prefix