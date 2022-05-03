import numpy as np
from itertools import combinations, product
from time import time


def bhi(clusters, dist_matrix):
    """Function calculate Baker Hubert gamma index"""
    dist_matrix = dist_matrix + dist_matrix.T - np.diag(np.diag(dist_matrix))

    # Find all pairs of point from same cluster
    same_cluster_index = set()
    for cluster in clusters:
        same_cluster_index = same_cluster_index.union(
            set(combinations(cluster, r=2)))

    # Find all pairs of point from two different clusters
    diff_cluster_index = set()
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            list1 = clusters[i]
            list2 = clusters[j]
            diff_cluster_index = diff_cluster_index.union(set(product(list1,
                                                                      list2)))

    # Calculate index value
    time_start = time()
    dist_matrix = dist_matrix.tolist()
    s = [1 if dist_matrix[i][j] > dist_matrix[p][q] else 0
         for i, j in diff_cluster_index for p, q in same_cluster_index]
    print(f'time calc: {time() - time_start}')
    s_plus = sum(s)
    s_minus = len(s) - s_plus

    return (s_plus - s_minus) / (s_plus + s_minus)


def gdi(clusters, dist_matrix):
    """Function calculate General Dunna index for given clusters and previously
    calculated distance matrix"""
    dist_matrix = dist_matrix + dist_matrix.T - np.diag(np.diag(dist_matrix))

    clusters_diameter = set()
    for cluster in clusters:
        ind = list(cluster)
        temp_matrix = dist_matrix[np.ix_(ind, ind)]
        clusters_diameter.add(diameter(temp_matrix))

    cluster_dist = set()
    for cluster_a in clusters:
        for cluster_b in clusters:
            if cluster_a != cluster_b:
                cluster_dist.add(clusters_distance(cluster_a, cluster_b,
                                                   dist_matrix))
    return min(cluster_dist) / max(clusters_diameter)


def diameter(matrix):
    """Diameter of cluster calculated by its distance matrix"""
    n = len(matrix)
    dist = [matrix[i][j] for i in range(n) for j in range((i+1), n)]
    return sum(dist) / len(dist)


def clusters_distance(cluster_a, cluster_b, dist_matrix):
    """Distance between two clusters based in distance matrix"""
    dist = set()
    for a in cluster_a:
        for b in cluster_b:
            dist.add(dist_matrix[a][b])
    return sum(dist) / len(dist)
