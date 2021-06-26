"""
Note on topological sort and how it works.

The reason why it's called topological ordering is because you want to take a
DAG (directed acyclic graph) and line all the nodes from left to right so that
left always points to right. This makes sense, it's like an in order traversal
of a binary tree.

If there is no topological order for a Cyclic Graphs. This is why it's a great
way to find if a DAG is actually cyclic or not.

The idea is to keep track of all the nodes that have an in degree of 0. Start
iterating from there and removing edges from the graph. Whenever you remove an
edge, you check if that node has now an in-degree of 0, if it does you make
sure to iterate over it again. Whenever you iterate over a new node that has
0 in degree, print it :D.

The general algorithm can be summed in the following if you get lost
L = Empty list that will contain the sorted elements
S = Set of all nodes with no incoming edge

while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S

if graph has edges then
    return error   (graph has at least one cycle)
else
    return L   (a topologically sorted order)

"""

from collections import defaultdict
from typing import List


class Node:
    """ Special node to keep track of in-degrees """

    def __init__(self):
        self.out_nodes = []  # Out Nodes
        self.in_deg = 0  # In Degrees


def build_graph(adjacency_list):
    """
    This function will not just return the graph, but also the initial set
    of nodes that have an in-degree of 0.
    """
    # We use our special Node to initialize the default dictionary
    graph = defaultdict(Node)
    degree_zero_nodes = set()

    for a, b in adjacency_list:
        # Same as before
        graph[a].out_nodes.append(b)
        graph[b].in_deg += 1

        # Here we get the nodes with degree zero
        if b in degree_zero_nodes:
            degree_zero_nodes.remove(b)

        # Here we check if the in degree of this node is 0 and add it to the set
        if graph[a].in_deg == 0:
            degree_zero_nodes.add(a)

    return graph, degree_zero_nodes


def topological_sort(adjacency_list: List[List[int]]) -> List:
    # Create a graph from an adjacency list
    graph, degree_zero_nodes = build_graph(adjacency_list)
    top_sort = []

    while len(degree_zero_nodes) > 0:
        # Pop a random element :D
        node = degree_zero_nodes.pop()
        top_sort.append(node)

        nodes = graph[node].out_nodes
        # We keep track of the elements we need to remove
        # and then remove them later
        to_be_removed = []

        for ind, val in enumerate(nodes):
            to_be_removed.append(ind)

            # Remove the neighbouring node
            neighbour = graph[val]
            neighbour.in_deg -= 1

            # If we know that this neighbour has no incoming nodes
            # then we add it to the while iteration
            if neighbour.in_deg == 0:
                degree_zero_nodes.add(val)

        # Remove them in the opposite order so as to not
        # cause an index error when popping
        for i in to_be_removed[::-1]:
            nodes.pop(i)

        # If it's empty and there are no more nodes,
        # just remove it and we'll check `graph` later
        if not nodes:
            del graph[node]

    # If all the edges are removed then we will return the sorted list
    if not graph.keys():
        return top_sort

    # Else we get to yell at the user!
    raise Exception("Graph passed in isn't cyclic")
