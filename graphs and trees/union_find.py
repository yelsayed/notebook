"""
Note on Union Find.

Union find is pretty cool.
The basic idea of Union Find is to create a spanning tree (essentially an
acyclic group of nodes) by identifying the parent of each.

At first, with no information given on the graph, you can assume that every
node in the graph belongs to it's own set i.e. it it's its own parent.

The algorithm goes as follows:
- Initialize the set with -1 for each vertex
- Go through every edge.
- Find the parent for every edge.
- If the edges belong to the same parent this means we have a cycle.
- If the edges belong to different parents join them.
* When joining always join the one with the smaller rank to the one with the
  higher rank. This way you're guaranteed to go back to the same parent in case
  of cycles.

Finding the parent is done in constant time plus the time it takes to go through
the edges O(V + E).

The space complexity of this is just the disjointed set that you store in the
end which at the worst is O(V).
"""

from typing import List


class UnionFind:
    def __init__(self):
        # Simple initialization
        self.disjointed_set = {}

    def build_disjointed_set(self, edges):
        # This is the way I used to build it, having it in a list is an easier
        # way for building the set in case you know how many nodes and the nodes
        # are consecutive and numbered.
        for a, b in edges:
            self.disjointed_set[a] = -1
            self.disjointed_set[b] = -1

    def find(self, node):
        parent = self.disjointed_set[node]
        # If it's negative we know the number
        if parent < 0:
            return node

        # If you don't find the ultimate parent try
        # again with the current parent
        return self.find(parent)

    def union(self, a, b):
        if self.disjointed_set[a] <= self.disjointed_set[b]:
            # When joining, make sure to keep track of how many vertices are in
            # my set specifically. You do this by adding the weight of the
            # set that is being joined to my set
            self.disjointed_set[a] += self.disjointed_set[b]
            self.disjointed_set[b] = a
        else:
            self.disjointed_set[b] += self.disjointed_set[a]
            self.disjointed_set[a] = b

    def is_cyclic(self, edges: List[List[int]]) -> bool:
        self.build_disjointed_set(edges)

        for a, b in edges:
            # Find both parents
            parent_a = self.find(a)
            parent_b = self.find(b)

            # If both parents belong to the same set, this means a cycle exists
            # You can think of a set here as a spanning tree
            if parent_a == parent_b:
                return True

            # Other wise just join the two parents
            self.union(parent_a, parent_b)

        return False
