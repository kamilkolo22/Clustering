from scipy.sparse.csgraph import minimum_spanning_tree
from ToolBox import *


def arrange_clusters(df_clusters):
    """Order list of clusters by average score in math test"""
    avg_score = np.array([])
    for cluster in df_clusters:
        avg_score = np.append(avg_score, cluster['math score'].mean())
    df_clusters = [df_clusters[i] for i in avg_score.argsort()]

    return df_clusters


def find_cluster(data):
    """Return clusters as a list of row indexes for each cluster. User has to
    set number of clusters manually"""
    span_tree_matrix = linkage(data)
    # Get longest edges in graph
    indexes = largest_indices(span_tree_matrix, 10)

    print(f'Longest distance between elements: {span_tree_matrix[indexes]}')
    number = int(input('Chose number of clusters (int): '))
    new = (indexes[0][:number-1], indexes[1][:number-1])

    # Delete longest edges by setting zeros in spanning tree matrix
    span_tree_matrix[new] = 0

    graph = matrix_to_graph(range(len(span_tree_matrix)),
                            span_tree_matrix)
    # Find connected components
    comp = connected_componentsBFS(graph)
    return comp[1:]


def linkage(data):
    """Calculate minimal spanning tree and return
    distance matrix of this tree"""
    corr_matrix = data.corr()
    dist_matrix = get_dist_matrix(data, corr_matrix)

    # Minimal spanning tree from distance matrix by function from scipy package
    span_tree_matrix = minimum_spanning_tree(dist_matrix).toarray()

    return span_tree_matrix


def get_dist_matrix(data, *args):
    """Prepare distance matrix for given data using mahalanobis metric"""
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
