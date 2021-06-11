# This note is to study how to validate a tree is a valid binary search tree
# https://leetcode.com/problems/validate-binary-search-tree/solution/.

import math
from typing import Tuple, Union, List


# Data structure we'll be working with, quite simple
class TreeNode:
    # Can't be changed
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Solution
###
# The recursive solution is the most obvious one. A binary tree is a BST if
# the left tree at each node is a BST and the right tree is a BST.
# You can verify that the left tree is a BST if none of the nodes are larger
# and that the right tree is a BST if none of the nodes are smaller. This means
# that we should keep a range as we're recursing through the tree.
def _is_valid_bst(current: TreeNode, high: Union[float, int],
                  low: Union[float, int]) -> bool:
    # Base case: If the current tree is empty means we've traversed everywhere
    #            or we're at an empty tree... both are BSTs
    if current is None:
        return True

    # Base case: If the current node goes out of range, that's a no-no
    #            `range` in this case is a tuple of (min, max)
    if high <= current.val <= low:
        return False

    # If we're checking the left tree, the max of the range becomes the min of
    # the last range and the current node (which has to be the current node
    # since the second base case checks if it's smaller already). Vise versa for
    # the other one. We just make sure that we're keeping track of the range

    return _is_valid_bst(current.left, low, current.val) and \
           _is_valid_bst(current.right, current.val, high)


def is_valid_bst(root: TreeNode) -> bool:
    return _is_valid_bst(root, -math.inf, math.inf)


# Note: It's important to mention that this is a DFS solution

# Iterative solution
###
# First we need to know how to iterate through a tree iteratively.
# We create a stack and add the left most element to the stack. When we reach
# the left most element (ie when the pointer that is going through the graph is
# null) we can just pop from the stack to get it's parent.

# Example with tracing:
#      2
#   3     4
# When the pointer is at 3 it's going to add three to the stack [3, 2] and
# assign the pointer to left of current, which is null.
# At this point the loop checks and finds that current is null, meaning we hit
# the left most node, and we pop it (ie we pop 3 from the stack) and assign
# the pointer to the right of 3, which is again null. Now we pop again, we pop
# 2, and we assign the pointer to the right of 2 which is 4. We add 4 to the
# stack and we assign the pointer to be the left of 4 which is null. Now we pop
# 4 in the next iteration and assign it to the right of 4 which is null. Then
# we stop looping as the pointer and the stack are both empty.

def traverse_tree(root: TreeNode) -> List[int]:
    # Stack has to be empty, on the first iteration is will append the root
    stack = []
    output = []
    current = root

    while current or stack:
        # Pointer is pointing to nothing means that we should check the
        # parent by popping from the stack
        if not current:
            current = stack.pop(0)
            # This append will keep things inline
            output.append(current.val)
            # Check the right, on the next iteration it should go to the left
            current = current.right
        else:
            stack.insert(0, current)
            current = current.left

    return output


# Given that we now know how to iterate over this tree. Note that
# left -> node -> right. We can run a small function over the output of this
# traversal. It's quite simple.

def is_valid_bst_inline(root: TreeNode) -> bool:
    inline_tree = traverse_tree(root)
    # The `all` function takes an iterable of `bool`s and returns the `and` of
    # them all. Also returns `True` for `[]` which works for the empty tree.
    return all(inline_tree[i] < inline_tree[i + 1] for i in
               range(len(inline_tree) - 1))

# So simble
