import random

from .graph import Graph


class GraphGen:
    @staticmethod
    def gen_cycle(n, **kwargs):
        """
        Generate a cycle graph with n vertices.

        Parameters:
            - `n` (int): Number of vertices in the cycle.
            - `**kwargs`: Additional arguments to pass to the Graph constructor.

        Returns:
            - Graph: The generated cycle graph.

        Examples:
            >>> cycle_graph = GraphGenerator.gen_cycle(5, directed=True, weighted=[lambda: 1])
        """
        g = Graph(n, **kwargs)
        for i in range(1, n):
            g.add_edge(i, i + 1)
        g.add_edge(n, 1)
        return g

    @staticmethod
    def gen_grid(r, c, **kwargs):
        """
        Generate a grid graph with r rows and c columns.

        Parameters:
            - `r` (int): Number of rows in the grid.
            - `c` (int): Number of columns in the grid.
            - `**kwargs`: Additional arguments to pass to the Graph constructor.

        Returns:
            - Graph: The generated grid graph.

        Examples:
            >>> grid_graph = GraphGenerator.gen_grid(3, 4)
        """
        g = Graph(r * c, **kwargs)
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                u = (i - 1) * c + j
                if j < c:
                    g.add_edge(u, u + 1)
                if i < c:
                    g.add_edge(u, u + c)
        return g

    @staticmethod
    def gen_wheel(n, **kwargs):
        """
        Generate a wheel graph with n spokes.

        Parameters:
            - `n` (int): Number of spokes in the wheel.
            - `**kwargs`: Additional arguments to pass to the Graph constructor.

        Returns:
            - Graph: The generated wheel graph.

        Examples:
            >>> wheel_graph = GraphGenerator.gen_wheel(6, weighted=[lambda: 2])

        Raises:
            - ValueError: If n is less than 4.
        """
        if n < 4:
            raise ValueError("A wheel graph has at least 4 nodes. The n you provided is: {}".format(n))
        g = Graph(n, **kwargs)
        for i in range(2, n + 1):
            g.add_edge(1, i)
        for i in range(3, n + 1):
            g.add_edge(i - 1, i)
        g.add_edge(2, n)
        return g

    @staticmethod
    def gen_chain(n, **kwargs):
        return GraphGen.gen_tree(n, chain_rate=1.0, **kwargs)

    @staticmethod
    def gen_star(n, **kwargs):
        return GraphGen.gen_tree(n, star_rate=1.0, **kwargs)

    @staticmethod
    def gen_tree(n, chain_rate: float = 0, star_rate: float = 0, **kwargs):
        if not 0 <= chain_rate <= 1 or not 0 <= star_rate <= 1 or not 0 <= chain_rate + star_rate <= 1:
            raise ValueError('''The parameters chain_rate and star_rate must meet the following conditions:
- 0 <= chain_rate <= 1
- 0 <= star_rate <= 1
- 0 <= chain_rate + star_rate <= 1
The chain_rate and star_rate you provided are {} and {} respectively.
            '''.format(chain_rate, star_rate))
        m = n - 1
        chain_edges = round(m * chain_rate)
        star_edges = round(m * star_rate)
        if chain_edges > m:
            chain_edges = m
        if chain_edges + star_edges > m:
            star_edges = m - chain_edges
        g = Graph(n, **kwargs)
        for i in range(star_edges):
            g.add_edge(1, i + 2)
        for i in range(chain_edges):
            g.add_edge(star_edges + i + 1, star_edges + i + 2)
        for i in range(chain_edges + star_edges + 1, n):
            g.add_edge(random.randint(1, i), i + 1)
        return g