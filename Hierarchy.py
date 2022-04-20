import numpy as np
import pandas as pd
from copy import deepcopy


def linkage(data):
    corr_matrix = data.corr()
    spanning_tree = {0: (0, 0)}
    data_cut = deepcopy(data)
    x_ind = 0

    for _ in range(len(data) - 1):
        x_row = data_cut.loc[x_ind]
        data_cut = data_cut.drop(x_ind)
        spanning_tree[x_ind] = find_closest(x_row, data_cut, corr_matrix)
        x_ind = spanning_tree[x_ind][0]

    return spanning_tree


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