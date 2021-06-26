"""
Note on the Course Schedule Problem
https://leetcode.com/problems/course-schedule/

The question immediately smells like a graph problem, where you have to find
cycles in a graph.

Initial Idea:
Create a graph out of the prereqs (linear time) using defaultdict.
Go through the graph to detect cycles. For everytime you go through an edge,
check if you've visited the graph before. Reset the visited datastructure
every time you go through each edge.

Time -> O(E+V^2) in the case that it's all chained, you're going to have to go
                all the way to the end of the graph and then back track to the
                beginning. Then you have to do that for the next node, and the
                next. Quite slow.
Space -> O(E+V) you're making a copy of the graph :D
"""

from typing import List
from collections import defaultdict


# Works but too slow. This solution is a DFS solution
def build_graph(prereqs):
    # Lovely way for creating a graph, works very straight forwardly
    graph = defaultdict(list)
    for a, b in prereqs:
        graph[a].append(b)

    return graph


def is_cyclic(node, graph, visited):
    if node in visited:
        return True

    visited[node] = True

    for neighbour in graph[node]:
        # This is a smart way of doing back tracking, this way the visited
        # doesn't change with every input.
        visited_copy = visited.copy()
        if is_cyclic(neighbour, graph, visited_copy):
            return True

    # Another idea is to just set the visited of this Node to be False, when
    # each node is visited, and it's done with it's path, it's going to be set
    # as False. Same Same...
    # visited[node] = False
    return False


def can_finish_slow(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = build_graph(prerequisites)
    nodes = dict.fromkeys(graph.keys(), [])
    for node in nodes:
        # Now check if each node is cyclic by giving it a path (in this case a
        # dictionary).
        if is_cyclic(node, graph, {}):
            return False

    return True


"""
This solution is quite slow, and it doesn't pass the tests on LeetCode.
One point of optimization here is the fact that we're going through the same
node multiple times. One thing to observe is that if a node doesn't lead to 
cycles this means that that's it for this node, we ain't finding cycles by going
through it again. 

A simple way of doing this is my marking the nodes as we go along. As either
permanently done or still in the current path of finding. 

This improves Time complexity.

Time Comp. -> O(V + E). Since you're not re-doing nodes your code should 
                        visit every vertex once (technically twice).
Space Comp. -> O(V + E) You're storing the whole graph to convert it into a 
                        nice repr. Nothing changes here.
"""


def is_cyclic_markings(node, graph, visited):
    # We've already checked if this node has no cycles
    if visited.get(node, 0) == 2:
        return False

    # In this path we already visited this guy
    if visited.get(node, 0) == 1:
        return True

    visited[node] = 1  # temporary

    for neighbour in graph[node]:
        if is_cyclic(neighbour, graph, visited):
            return True

    visited[node] = 2  # permanent
    return False


def can_finish_faster(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = build_graph(prerequisites)
    nodes = graph.copy().keys()
    for node in nodes:
        if is_cyclic_markings(node, graph, {}):
            return False

    return True
