"""
Note on Flood Fill
https://leetcode.com/problems/flood-fill/solution/

DFS... and voila!

Complexity
Time: O(N) you touch each element once
Space: O(N) the call stack on recursion
"""
from typing import List


def visit_pixel(
        image: List[List[int]],
        i: int,
        j: int,
        new_color: int,
        original_color: int
) -> None:
    if image[i][j] != original_color:
        return

    image[i][j] = new_color

    for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        try:
            if ii >= 0 and jj >= 0:
                visit_pixel(image, ii, jj, new_color, original_color)
        except IndexError:
            pass


def flood_fill(
        image: List[List[int]],
        sr: int,
        sc: int,
        new_color: int
) -> List[List[int]]:
    initial_color = image[sr][sc]
    if initial_color == new_color:
        return image

    visit_pixel(image, sr, sc, new_color, initial_color)
    return image


"""
I did it again 10 days later to see if I still got it, and yup I got it.
I was wondering if I could do this in a more complicated or interesting way.
But DFS just fits well for this problem. The other problem for island count is
more interesting as it can be solved in multiple ways.
"""


def flood_fill_again(
        image: List[List[int]],
        sr: int,
        sc: int,
        original_color: int
) -> List[List[int]]:
    original_color = image[sr][sc]

    if original_color == original_color:
        return image

    def fill_nodes(i, j):

        try:
            if image[i][j] != original_color:
                return
            image[i][j] = original_color
        except IndexError:
            return

        for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if ii >= 0 and jj >= 0:
                # This recursion is DFS plain and simple
                fill_nodes(ii, jj)

    fill_nodes(sr, sc)

    return image
