from .utils.global_config import config
from .utils.rand import gen_permutation, evaluate_list, int_1bit
import random
from collections import defaultdict


class Edge:
    def __init__(self, u, v, weight_list: list = None):
        """
        Initialize an Edge object.

        Parameters:
            - `u` (int): Starting vertex of the edge.
            - `v` (int): Ending vertex of the edge.
            - `weight_list` (list, optional): List of weights for the edge (default is an empty list).
        """
        if weight_list is None:
            weight_list = []
        self.start = u
        self.end = v
        self.weight_list = weight_list

    def __str__(self):
        """
        Generate a string representation of the edge.

        Returns:
            - str: String representation of the edge.
        """
        return config.get("graph_seperator", " ").join(map(str, [self.start, self.end] + self.weight_list))

    def __repr__(self):
        """
        Generate a string representation of the edge for debugging.

        Returns:
            - str: String representation of the edge for debugging purposes.
        """
        return "(" + " ".join(map(str, [self.start, self.end] + self.weight_list)) + ")"


class Graph:
    def __init__(self, n, **kwargs):
        """
        Initialize a Graph object.

        Parameters:
            - `n` (int): The number of vertices in the graph.
            - `first_index` (int, optional): The minimum index for vertex numbering (default is 1).
            - `weighted` (list, optional): List of weight functions for edges (default is an empty list).
            - `shuffle` (bool, optional): Whether to shuffle the order of edges (default is True).
            - `directed` (bool, optional): Whether the graph is directed (default is False).
            - `graph_separator` (str, optional): Separator used for graph output (default is " ").
            - `adjacency_mat` (bool, optional): Whether to represent the graph as an adjacency matrix (default is False).
            - `self_loop` (bool, optional): Whether to allow self-loops (default is False).
            - `multi_edge` (bool, optional): Whether to allow multiple edges between the same vertices (default is False).
        """
        self.n = n
        self.__m = 0
        self.first_index = kwargs.get('first_index', 1)
        self.weight_func_list = kwargs.get('weighted', [])
        self.shuffle = kwargs.get('shuffle', True)
        self.directed = kwargs.get("directed", False)
        config['graph_seperator'] = kwargs.get('graph_seperator', " ")
        self.adjacency_mat = kwargs.get("adjacency_mat", False)
        self.self_loop = kwargs.get("self_loop", False)
        self.multi_edge = kwargs.get("multi_edge", False)
        if self.adjacency_mat:
            self.weight_func_list = []
        self.__edge_list = [defaultdict(list) for _ in range(n + 1)]

    def edge_num(self):
        """
        Get the number of edges in the graph.

        Returns:
            - int: The number of edges in the graph.
        """
        return self.__m

    def __iterator_edge(self):
        for start in range(1, self.n + 1):
            for end, edge_list in self.__edge_list[start].items():
                if start <= end or self.directed:
                    for edge in edge_list:
                        yield edge

    def add_edge(self, u, v):
        """
        Add an edge to the graph.

        Parameters:
            - `u` (int): Starting vertex of the edge.
            - `v` (int): Ending vertex of the edge.
        """
        if not self.self_loop and u == v:
            return
        elif not self.multi_edge and v in self.__edge_list[u].keys():
            return
        self.__m += 1
        w = evaluate_list(self.weight_func_list)
        self.__edge_list[u][v].append(Edge(u, v, w))
        if not self.directed and u != v:
            self.__edge_list[v][u].append(Edge(v, u, w))

    def __str__(self):
        """
        Generate a string representation of the graph.

        Returns:
            - str: String representation of the graph.
        """
        output_edge_list = list(self.__iterator_edge())
        if self.shuffle:
            random.shuffle(output_edge_list)
            permutation = gen_permutation(self.n)
            for e in output_edge_list:
                e.start = permutation[e.start - 1]
                e.end = permutation[e.end - 1]
                if not self.directed and int_1bit():
                    e.start, e.end = e.end, e.start
        for e in output_edge_list:
            e.start += self.first_index - 1
            e.end += self.first_index - 1

        if not self.adjacency_mat:
            return "\n".join(str(e) for e in output_edge_list)
        else:
            if self.n > 10000:
                print("n is too large. {}".format(self.n))
            mat = [[0 for _ in range(self.n)] for _ in range(self.n)]
            for e in output_edge_list:
                start, end = e.start - self.first_index, e.end - self.first_index
                mat[start][end] = 1
                if not self.directed:
                    mat[end][start] = 1
            return "\n".join("".join(str(v) for v in mat[i]) for i in range(self.n))

    def __repr__(self):
        """
        Generate a string representation of the graph for debugging.

        Returns:
            - str: String representation of the graph for debugging purposes.
        """
        return "edge_list: {}".format(list(self.__iterator_edge()))