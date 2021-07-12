"""
Note on Is Isomorphic
https://leetcode.com/problems/isomorphic-strings/

I wanted an easy question because I was curious to see how deep people can go.
This is an easy question, basically you want to know if a string matches
another string if you replace every unique character to match the other string.

Initial Idea:
This is pretty simple, just check the index at each character in one string
and see if it matches the index of each character in another string.

This will lead to you creating two strings that are replacements of their
indices.

Example: s = "title", t = "paper"
You can create two mappings
{
    t -> 0
    i -> 1
    l -> 3
    e -> 4
}
{
    p -> 0
    a -> 1
    e -> 3
    r -> 4
}

This could be transformed to "01034" for both, and if they're equal we know
they are isomorphic.

Simple :D
"""


def is_isomorphic(s: str, t: str) -> bool:
    smap = {}
    tmap = {}

    if s == t:
        return True

    for i in range(len(s)):
        smap[s[i]] = smap.get(s[i], i)
        tmap[t[i]] = tmap.get(t[i], i)

        # At this point you've encountered a character that broke the mapping
        if smap[s[i]] != tmap[t[i]]:
            return False

    return True


"""
Brilliant Solution:
It's worth mentioning a brilliant solution I found in the discussion section.

We can notice that the characters map to each other in our other solution.
One thing we can do is zip the characters, so that they're mapping to each 
other and create a set of unique mappings. Then we check if the number of the
unique mappings is the same as the number of unique characters, if they are
that means they're isomorphic.

Essentially it means if we have 3 unique mappings, and 3 unique characters in
both s and t, then we can effectively replace each character in s to make t.

So genius!!!
"""


def is_isomorphic_brilliant(s: str, t: str) -> bool:
    return len(set(s)) == len(set(zip(s, t))) == len(set(t))
