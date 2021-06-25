"""
Note on Letter combinations of a phone number.
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

The letter combinations for the digits on the phone could be a permutation of a
number of things.
For Example:
"23"
Can be any of the following ["ad","ae","af","bd","be","bf","cd","ce","cf"].

This is because '2' -> "abc" and '3' -> "def".

Our goal is to find all the combinations given this.

The solution is quite simple to think about recursively. You take one character
and you get the the letters for that digit. Then you iteratively add it to a
return list. Initially you'll have an empty list so for 2 it will return
['a', 'b', 'c']. On the second character you will get another set of characters
and you'll add it to the existing characters.

For 23 this will look like

    a         b         c
 ad ae af  bd be bf  cd ce cf

Time complexity: 4^N in the worst case since it's a tree with 4 nodes on every
                 level for N levels.
Space complexity: N not including the output
"""

from typing import List


class Solution:
    ret_list = []

    digit_letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    @staticmethod
    def _generate_combinations(res, all_letters):
        ret = []

        if len(res) == 0:
            res = ['']
        for letter in all_letters:
            for char in res:
                ret.append(char + letter)

        return ret

    def letter_combinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.ret_list

        # Here we're stripping it off from the the end since we want to start
        # from the beginning after the stripping is done. This made the most
        # sense to me.
        last_digit = digits[-1]
        all_letters = self.digit_letters[last_digit]
        self.letter_combinations(digits[:-1])

        # Here we iteratively add the letters to the return list which will
        # be updated on every recursive call
        self.ret_list = self._generate_combinations(self.ret_list, all_letters)

        return self.ret_list
