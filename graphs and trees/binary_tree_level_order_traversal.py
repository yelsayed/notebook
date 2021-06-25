"""
Note on Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

The problem here is to get the level of a binary tree in order.
Example:
    5
 2     6
    4     8

Needs to return [[5], [2,6], [4,8]]

This is a simple problem to do recursively, where at each level you go down
all you have to do is just keep track of the level and append it to a dictionary
with that level, then later on you just iterate through the ordered dictionary.

Time Complexity: O(N) you're touching each node at least once
Space Complexity: O(N) because you're storing each node at least once
"""

from collections import defaultdict
from typing import List


class TreeNode:
    """
    Definition for a binary tree node (cannot be changed).
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_level_order(self, root: TreeNode, level: int, node_dict) -> None:
    # In case we reached the end
    if root is None:
        return

    # We could just do root.val, that works fine too
    node_dict[level].append(root.left.val) if root.left else None
    node_dict[level].append(root.right.val) if root.right else None

    # We recurse on the left and the right, this will maintain the order.
    self.recursive_level_order(root.left, level + 1, node_dict)
    self.recursive_level_order(root.right, level + 1, node_dict)


def level_order(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    # We do default dict and only add to it once there is a Node, this makes it
    # so we don't have to check if we've instatiated the level or not
    node_dict = defaultdict(list)

    # Start off with the root
    ret_list = [[root.val]]

    # Recursive step
    self.recursive_level_order(root, 1, node_dict)

    # This would be better if it's an OrderedDict, but it works fine because
    # when using indices, the order is maintained
    for _, val in node_dict.items():
        ret_list.append(val)

    return ret_list

# One thing to mention here is that you could actually solve this problem
# iteratively keeping a stack and keeping track of the level as you're building
# the stack. This is something I do in Binary Tree Zigzag level traversal
