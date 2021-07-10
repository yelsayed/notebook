"""
Note on Gold Mine Problem
https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1

This problem is a simplified problem of the "Path with Maximum Gold" problem.
You can find a note of that problem in the file `path_with_max_gold.py` in the
graphs directory.

Since you have a start point, end point and directionality, you can create a
dynamic programming array from the process of traversing the graph.

For every point in the graph, you know that the maximum value you can get
is the maximum you've collected from either left, left_up, or left_down.

For example:
[
    [1, 3, 3],
           x
    [2, 1, 4],
    [0, 6, 4]
]

For point x (4 in this case) you know that the max you can get is whatever the
max of 3, 1 or 6 is. And for 3, the max you can get is whatever the max of 1 and
2 is. We know that at that point, 1 and 2 are both starting points, so we choose
the max which is 2 in this case. so the path becomes 2 -> 3 -> 4 = 9. This isn't
the best path since there is another path 2 -> 6 -> 4 but that's the best path
for 3.

We can create a DP 2D array that creates a good data model for this. The initial
DP array can contain the last row (since it doesn't have a right, all those
points are the max they can be).

[
    [0, 0, 3],
    [0, 0, 4],
    [0, 0, 4]
]

We iterate column then for each column we go by rows. The reason it's not rows
then columns is because if you go to (0, 0) for example, you cannot know the
max because (0, 1) won't be filled.

For each column we check the right up, right down and right and get the max.
Then we add our current gold to it.

[
    [0, 3+4, 3],
    [0, 1+4, 4],
    [0, 6+4, 4]
]

Then we do that again.
[
    [1+7, 7, 3],
    [2+10, 5, 4],
    [0+10, 10, 4]
]

The first column is the one that has all the answers, you just check which one
is the max. This makes sense from the perspective of the question itself. If
you were a foraging for gold, you wanna know which starting point is the best.

And voila. Clean problem. Not an easy one for sure, it's a medium difficulty.
"""


def max_gold(n, m, gold):
    high = 0  # There are no negative values otherwise we'd put infinity here
    dp = [x[:] for x in gold]

    # We assume that there is at least two columns in the grid
    for j in range(m - 2, -1, -1):
        for i in range(n):
            # Get the values from the DP array
            right = dp[i][j + 1]
            right_up = dp[i - 1][j + 1] if i > 0 else 0
            right_down = dp[i + 1][j + 1] if i < n - 1 else 0

            # Get the max value
            dp[i][j] += max(right, right_up, right_down)

            # On the first row just get the highest value
            if j == 0:
                high = max(dp[i][j], high)

    return high

