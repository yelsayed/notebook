"""
Note on Index Pairs of a String.
https://leetcode.com/problems/index-pairs-of-a-string/

This problem is to find the words in a string. It's actually an easy problem
to solve using a hashmap. Not much to this problem at all.

However I did this problem to learn about Tries and how they work. I made a
separate note about tries.

This problem has a small variation from just basic tries. One thing that you
need to do is return all the strings even if they're overlapping. The way I did
that is: even if there is a stop node, don't just stop, try to keep going
through the array.

Complexities are also interesting for this problem:
M = Number of words
N = Number of characters in the input string
Time -> O(N*M + M) because we're going through the tree N times, at the worst
                   case, and M more times to build the tree
Space -> O(26M) because for every node in the tree you store 26 at the worst
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    @staticmethod
    def get_index(char):
        return ord(char) - ord('a')

    def insert(self, string):
        ptr = self.trie

        for char in string:
            index = Trie.get_index(char)
            if ptr.children[index] is None:
                ptr.children[index] = TrieNode()

            ptr = ptr.children[index]

        ptr.end = True

    def search(self, string, count):
        ptr = self.trie

        for char in string:
            index = Trie.get_index(char)
            node = ptr.children[index]

            if node is None:
                return False, count

            count += 1
            ptr = node

            # Just one end, we can have more ends
            if node.end:
                yield True, count

        return ptr.end, count


def index_pairs(text: str, words: List[str]) -> List[List[int]]:
    pairs = []
    trie = Trie()

    for word in words:
        trie.insert(word)

    i = 0
    while i < len(text):
        # Everytime we loop we try a different value of the string
        substring = text[i:]

        # We need a generator here because we're just making sure that we
        # get all the overlaps
        for exists, count in trie.search(substring, 0):
            # Sometimes the search will return None
            if exists:
                pairs.append([i, i + count - 1])

        i += 1
    return pairs
