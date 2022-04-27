import numpy as np


def matrix_to_graph(vertices, matrix):
    """Convert distance matrix to weighted graph"""
    n = len(matrix)
    if len(vertices) < n:
        raise ValueError('lista wierzchołków jest za krótka!')
    graph = {x: [] for x in vertices}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                graph[vertices[i]].append((vertices[j], matrix[i][j]))
                graph[vertices[j]].append((vertices[i], matrix[i][j]))
    return graph


def largest_indices(ary, n):
    """Returns the n largest indices from a numpy array."""
    flat = ary.flatten()
    indices = np.argpartition(flat, -n)[-n:]
    indices = indices[np.argsort(-flat[indices])]
    return np.unravel_index(indices, ary.shape)


def connected_componentsBFS(graph):
    def BFS(v):
        queue.append(v)
        while len(queue) > 0:
            v = queue.pop(0)
            VT[-1].add(v)
            for u, w in graph[v]:
                if u in VT[0]:
                    continue
                queue.append(u)
                VT[0].add(u)

    VT = [set([])]
    queue = []
    for v in graph:
        if v not in VT[0]:
            VT[0].add(v)
            VT.append({v})
            BFS(v)
    return VT
