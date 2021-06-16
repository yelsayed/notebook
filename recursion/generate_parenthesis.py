"""
Note on the Generate Parenthesis question on LeetCode
https://leetcode.com/problems/generate-parentheses/solution/

We have to generate all the valid parenthesis for a number.
For example Input: n = 3
            Output: ["((()))","(()())","(())()","()(())","()()()"]

Initially when laying out all the strings for each level it actually threw me
off. I rabbit-holed.

For n = 3 I did this
n = 1
"()"

We either wrap
-> "(())"

Or we add another paranthesis between it and next complete

-> "()()"

n = 2
["(())", "()()"]

n = 3
Wrap
0->"((()))"
1->"(()())"

Add
0->"()(())"
0->"(())()"
1->"()()()"

res -> ["((()))","(()())","(())()","()(())","()()()"]

The problem is that I thought every answer is reliant on the previous answer
and that made me think in that context, all I have to do is either wrap an older
parenthesis or add to it, but it doesn't work with n >= 4. The problem is that
the parenthesis get deeply nested.

Another issue is that I didn't think of the brute force solution right away,
which is to generate all the parenthesis and get the valid ones.
"""

from typing import List


# First solution, works for n < 4
def generate_parenthesis_broken(n: int) -> List[str]:
    if n == 1:
        return ["()"]

    last_level = generate_parenthesis_broken(n - 1)
    all_parenthesis = set()

    for level in last_level:
        all_parenthesis.add(f"({level})")
        all_parenthesis.add(f"(){level}")
        all_parenthesis.add(f"{level}()")

    return list(all_parenthesis)


"""
The next approach that I had was more iterative, which reminded me of the
decode variations or 4-sum with recursion question.

Solution:
In the generation of each string keep track of how many parenthesis you have 
left (this is easy because you can start at n * 2 and subtract one everytime) 
and how many open parenthesis you have in the string.

Each time you iterate you add to the generated string, and you have one of two
options, you either add a "(" or a ")". But we need to make sure that whatever
we add will make for a valid string. 

If you have an open "(" somewhere in the past you have one of two options, you
either open another one (given that you haven't exceeded n) or you close.

If the open counter is 0 you're forced to open.

This solution is also so nice to implement. 
"""


def _generate_parenthesis(n: int, open_counter: int, string: str) -> List[str]:
    # This is the base case which essentially states that the amount of open
    # brackets have exceeded the level which it's at and we need to close it.
    # This is like saying you opened 3 and you have 3 left, so you just have to
    # close everything right now.
    if open_counter >= n:
        return [string + (")" * open_counter)]

    # If the open counter is greater than zero this means we don't have to open,
    # we can do either open or close, it's really up to us. Additionally, if
    # we're at this condition this means we still have brackets to spare.
    if open_counter > 0:
        return _generate_parenthesis(n - 1, open_counter + 1, string + "(") + \
               _generate_parenthesis(n - 1, open_counter - 1, string + ")")

    # We kinda have to open at this point because the counter is at 0.
    return _generate_parenthesis(n - 1, open_counter + 1, string + "(")


def generate_parenthesis(n):
    return _generate_parenthesis(n * 2, 0, "")
