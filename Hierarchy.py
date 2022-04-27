import numpy as np
import pandas as pd
from copy import deepcopy
from sklearn.metrics import pairwise_distances
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from ToolBox import *


def find_cluster(data, number):
    spanning_tree = linkage(data)
    # Get longest edges in graph
    indexes = largest_indices(spanning_tree, number)
    # Delete longest edges by setting zeros in spanning tree matrix
    spanning_tree[indexes] = 0

    graph = matrix_to_graph(range(len(spanning_tree)),
                            spanning_tree)
    # Find connected components
    comp = connected_componentsBFS(graph)
    return comp[1:]


def linkage(data):
    corr_matrix = data.corr()
    dist_matrix = get_dist_matrix(data, corr_matrix)

    # Minimal spanning tree from distance matrix by function from scipy package
    spanning_tree = minimum_spanning_tree(dist_matrix).toarray()

    return spanning_tree


def get_dist_matrix(data, *args):
    n = len(data)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            dist_matrix[i][j] = mahalanobis_metric(data.iloc[i], data.iloc[j],
                                                   args[0])

    return dist_matrix


def mahalanobis_metric(x, y, cov):
    """Mahalanobis metric for given x, y vectors and covariance matrix"""
    if not type(x).__module__ == np.__name__:
        x = np.array(x)
    if not type(y).__module__ == np.__name__:
        y = np.array(y)
    inv_cov = np.linalg.inv(cov)
    vec = x - y
    return np.sqrt(vec.T @ inv_cov @ vec)
