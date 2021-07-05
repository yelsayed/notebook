"""
Note on Tries

Tries are used for retrieving data that is in a small finite set of elements
that are related to each other somehow. One of the main things that people
use tries for is to fetch strings. To see if a string matches, for example,
as you're typing. Fun stuff.

Tries look something like this
       root
    /   \    \
    t   a     b
    |   |     |
    h   n     y
    |   |  \  |
    e   s  y  e
 /  |   |
 i  r   w
 |  |   |
 r  e   e
        |
        r

The reason this works so well is that for any string the search is linear. BAM!

The space complexity for this is obviously the size of the alphabet * M where
M is the length of the longest word.
"""


class TrieNode:
    def __init__(self):
        # A better way that I saw later was to use a
        # default dict that returns None
        self.children = [None] * 26

        # End here means that this is the end of a string
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def get_index(char):
        return ord(char) - ord('a')

    def insert(self, string):
        ptr = self.root

        # For every character insert into a level in our Trie.
        for char in string:
            index = Trie.get_index(char)

            # The `or TrieNode()` here is to create a new node if the one we
            # accessed is None. This means that we're adding a new level to
            # our Trie.
            node = ptr.children[index] or TrieNode()

            ptr = node

        ptr.end = True

    def search(self, string, count):
        # Search for the string in the trie
        ptr = self.root

        for char in string:
            index = Trie.get_index(char)
            node = ptr.children[index]

            # It reached the end of the Trie for this string,
            # so we can stop here
            if node is None:
                return False, count

            count += 1
            ptr = node

        # This indicates that the word is in the Trie
        return ptr.end, count
