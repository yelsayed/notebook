# This note is to study finding cycles in a graph and the efficiency of doing
# that.

# There are two algorithms you can find cycles in an undirected
# graph: Union Find & DFS

from collections import defaultdict  # dictionary but returns a default value


# DFS
# The idea is to start at each node and traverse the graph to see if there are
# any sort of cycles

# Firstly we have to create a graph
# One simple way to represent a graph is by making a dictionary where the key
# is a vertex and the adjacent vertices are a list

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, adjacent):
        self.graph[vertex].append(adjacent)

        # Since it's an undirected graph, we have to do the opposite as well
        self.graph[adjacent].append(vertex)

    def _find_cycles(self, current_vertex, visited, parent):
        """
        Recursive helper function that traverses the graph

        :param current_vertex: vertex that we're traversing
        :param visited: list of visited vertices in a bit array (so to speak)
        :param parent: the initial vertex that this traversal started from

        :return: Boolean
        """
        visited[current_vertex] = True
        for adjacent_vertex in self.graph[current_vertex]:
            # Only do this cycle if the parent isn't the adjacent, since this
            # is an undirected graph
            if parent != adjacent_vertex:
                # If the adjacent vertex was visited and it's not the parent
                # that means there is a cycle
                if visited[adjacent_vertex]:
                    return True

                # Else then check the next adjacent vertex, the recursion should
                # have a depth-first traversal effect :D
                elif self._find_cycles(adjacent_vertex, visited, current_vertex):
                    return True

        return False

    def is_cyclic(self):
        """
        Returns if the graph is cyclic or not by traversing the graph from
        each node to discover a cycle

        :return: Boolean
        """

        # Initialize the visited bit array that should look like:
        # [False, False, ..., False] of length n
        n = len(self.graph.keys())
        visited = [False] * n

        # Now for each one of the vertices we traverse the graph
        for vertex in self.graph.keys():
            # If this vertex has been visited then there is no need to check
            if visited[vertex]:
                continue

            # We start off with parent being -1 just so the comparison fails
            # with the first parent.
            if self._find_cycles(vertex, [False] * n, -1):
                return True

        return False

    def __str__(self):
        ret_str = ""
        for vertex in self.graph:
            ret_str += f"{vertex} -> {self.graph[vertex]}\n"
        return ret_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 3)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(3, 4)

    is_cyclic = graph.is_cyclic()

    print(f"Graph {graph} {'is' if is_cyclic else 'is not'} cyclic")

    graph = Graph()
    graph.add_edge(0, 3)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)

    is_cyclic = graph.is_cyclic()

    print(f"Graph {graph} {'is' if is_cyclic else 'is not'} cyclic")
