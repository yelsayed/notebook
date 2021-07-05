"""
Note on Redundant Connection
https://leetcode.com/problems/redundant-connection/

Initial Idea:

Use Union-Find

Build a for each node with parent of -1
That will be our set.

Iterate through all the edges
For every edge, FIND the parent.
If both nodes belong to the same parent
then this is a cycle and this is an answer.

If both nodes are in different sets: UNION.

Return the last cyclic edge.

Example
[[1,2],[2,3],[3,4],[1,4],[1,5]]
                    edge

disjointed = {1: -4, 2: 1, 3: 1, 4: 1, 5: -1}
              a.                  b

Complexity
Time -> O(V + E)
Space -> O(V)
"""

from typing import List


class Solution:
    def build_disjointed_set(self, edges):
        disjointed_set = {}

        for a, b in edges:
            disjointed_set[a] = -1
            disjointed_set[b] = -1

        return disjointed_set

    def find(self, disjointed_set, node):
        parent = disjointed_set[node]
        if parent < 0:
            return node

        return self.find(disjointed_set, parent)

    def union(self, a, b, disjointed_set):
        if disjointed_set[a] <= disjointed_set[b]:
            disjointed_set[a] += disjointed_set[b]
            disjointed_set[b] = a
        else:
            disjointed_set[b] += disjointed_set[a]
            disjointed_set[a] = b

    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        # Since they need the last edge in the question, we can just define
        # the variable here and define it in the loop, the last loop will be
        # the last cyclic edge
        cyclic_edge = None
        disjointed_set = self.build_disjointed_set(edges)

        for a, b in edges:
            parent_a = self.find(disjointed_set, a)
            parent_b = self.find(disjointed_set, b)

            if parent_a == parent_b:
                cyclic_edge = [a, b]
            else:
                self.union(parent_a, parent_b, disjointed_set)

        return cyclic_edge
