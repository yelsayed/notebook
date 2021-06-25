"""
Note on Binary Tree Diameter
https://leetcode.com/problems/diameter-of-binary-tree/

The problem is to find the longest path between any two nodes.

Initial idea:
Get the maximum level on the right, and the maximum level on the left for any
subtree, and the distance would be the sum of those two levels.

            1
        2
    3       4
  2   2   2   4

We can just get the depth of left and right at every level, sum them and the
max with all the sums.

This is pretty simple to do in a dumb way, which for each subtree which you
access recursively, get the height of the left tree (in a different recursive
function) and the height of the right tree and then get the sum of both. Then
add all the sums to a list and get the max of that list.

This is terribly inefficient it could N^2 when you're repeating a lot of comp.
but it works well

Time -> N^2 since for each subtree you traverse the graph to get the depth
Space -> N since you're keeping a list of all the diameters for all subtrees
"""


class TreeNode:
    """ Can't be changed """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree_slow(root: TreeNode) -> int:
    all_vals = []

    def _get_max_height(root, height):
        if not root:
            return height

        return max(_get_max_height(root.left, height + 1),
                   _get_max_height(root.right, height + 1))

    def get_max_height(root, height):
        if not root:
            return height

        max_height_left = _get_max_height(root.left, 0)
        max_height_right = _get_max_height(root.right, 0)

        all_vals.append(max_height_left + max_height_right)

        get_max_height(root.left, height + 1)
        get_max_height(root.right, height + 1)

    get_max_height(root, 0)

    return max(all_vals)


"""
There is a cleaner way to do this. I'm not sure how.

After trying it out (and looking at the solution a little) one great idea is to
keep the return value outside the main loop, that way ANY execution of the 
recursive function is going to update the max by adding up the left and the 
right.

That way, our recursive function can do two things, keep track of the max and
get the depth of the tree by adding one to each iteration. The addition is done
in the end not in the function itself, so it will only get +1 at the end of 
the recursion.

The time and space complexity for this solution is much nicer.
Time -> O(N)
Space -> O(1)

Yay!
"""


def diameter_of_binary_tree(root: TreeNode) -> int:
    diameter = 0

    def get_max_height(root):
        # This is a cool thing if you're not using classes
        nonlocal diameter
        if not root:
            return 0

        # Keep going until you reach the child node, and at each step we'll
        # also be calculating the diameter
        left_height = get_max_height(root.left)
        right_height = get_max_height(root.right)

        # The diameter at each step will be calculated with a max function
        diameter = max(diameter, left_height + right_height)

        # Here we add +1 to the height the max height, indicating that we
        # are at a higher level
        return max(left_height, right_height) + 1

    get_max_height(root)

    return diameter
