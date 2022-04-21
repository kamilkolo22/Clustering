import numpy as np
import pandas as pd
from copy import deepcopy
from sklearn.metrics import pairwise_distances
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree


def linkage(data):
    corr_matrix = data.corr()
    dist_matrix = get_dist_matrix(data, corr_matrix)

    # spanning_tree = {0: (0, 0)}
    # data_cut = deepcopy(data)
    # x_ind = 0
    #
    # for _ in range(len(data) - 1):
    #     x_row = data_cut.loc[x_ind]
    #     data_cut = data_cut.drop(x_ind)
    #     spanning_tree[x_ind] = find_closest(x_row, data_cut, corr_matrix)
    #     x_ind = spanning_tree[x_ind][0]

    return minimum_spanning_tree(dist_matrix)


def get_dist_matrix(data, *args):
    ## TODO implement mahalanobis metric
    # n = len(data)
    # dist_matrix = np.zeros((n, n))
    # for i in range(n):
    #     for j in range(n):
    #         if i == j:
    #             continue
    #         dist_matrix[i][j] = mahalanobis_metric(data.iloc[i], data.iloc[j], args[0])

    dist_matrix = pd.DataFrame(distance_matrix(data.values, data.values),
                               index=data.index, columns=data.index)
    return dist_matrix


def find_closest(x, data, *args):
    """Find closest point and return distance and vector index"""
    ## TODO check if funcktion returns row index name or index number
    dist_min = np.inf
    index_min = -1
    for index, row in data.iterrows():
        temp = mahalanobis_metric(x, row, args[0])
        if temp < dist_min:
            dist_min = temp
            index_min = index

    return index_min, dist_min


def mahalanobis_metric(x, y, cov):
    """Mahalanobis metric for given x, y vectors and covariance matrix"""
    if not type(x).__module__ == np.__name__:
        x = np.array(x)
    if not type(y).__module__ == np.__name__:
        y = np.array(y)
    inv_cov = np.linalg.inv(cov)
    vec = x - y
    return np.sqrt(vec.T @ inv_cov @ vec)
