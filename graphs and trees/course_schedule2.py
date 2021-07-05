"""
Initial Idea:
This is another use case for topological sort.
Any return for topsort will give you back a valid course to take.

Top sort is a little difficult to remember so I'm going to try to do it
from memory.

Algorithm:
Build the graph.
As you're building the graph make sure to record the in degrees and out edges
for each node.

Create a set of nodes that have in degree of zero.
Go through the set that has in degree zero.
    Add that element to the list
    Go through each neighbour and remove that edge.
    If the new in degree is zero add it to the set and remove it from the graph.
    Loop.

If at the end the graph has any edges left, return [].

[[1,0]]
{
    0 -> { outedges: [1], indeg: 0 }
    1 -> { outedges: [], indeg: 1 }
}

Time Complexity -> O(V + E)
Space Complexity -> O(V + E)
"""

from typing import List, Set, Tuple
from collections import defaultdict


def build_graph(prereqs: List[List[int]]):
    used = set()
    graph = defaultdict(lambda: {
        "out_edges": [],
        "in_deg": 0
    })

    for a, b in prereqs:
        graph[b]["out_edges"].append(a)
        graph[a]["in_deg"] += 1
        used.add(b)
        used.add(a)

    return graph, used


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    graph, used = build_graph(prerequisites)
    ordering = []
    zero_degree_nodes = set()
    all_courses = set([i for i in range(num_courses)])
    no_prereqs = all_courses - used

    for key, value in graph.items():
        if value["in_deg"] == 0:
            zero_degree_nodes.add(key)

    while len(zero_degree_nodes) > 0:
        node = zero_degree_nodes.pop()
        ordering.append(node)
        while len(graph[node]["out_edges"]) > 0:
            neighbour = graph[node]["out_edges"].pop()

            graph[neighbour]["in_deg"] -= 1
            if graph[neighbour]["in_deg"] == 0:
                zero_degree_nodes.add(neighbour)

        del graph[node]

    if len(graph.keys()):
        return []

    # Everything up to this point has been just top sort with an extra flavor.
    # There is a small twist to this problem where there are courses that have
    # no prereqs. The way this is done in the input is by giving `num_courses`.
    # The solution here is to subtract the used set from the actual set of
    # courses.
    return ordering + list(no_prereqs)
