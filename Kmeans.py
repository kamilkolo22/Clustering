import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def find_cluster_kmean(data):
    """Test different k parameter, show results and ask user for param"""
    # Values scaling
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Test different parameters
    dist = []
    for i in range(2, 50):
        model = KMeans(n_clusters=i)
        model.fit(scaled_data)
        # Sum of squared distances of samples to their closest cluster center
        dist.append(model.inertia_)

    # Show results for different parameter
    plt.plot(range(2, 50), dist, 'o--')
    plt.xlabel("K Value")
    plt.ylabel("Sum of Squared Distances")
    plt.show()
    plt.bar(range(2, 50), pd.Series(dist).diff())
    plt.show()

    # Ask user for k param and return final split into clusters
    k = int(input("Chose number of clusters: "))
    model = KMeans(n_clusters=k)
    cluster_labels = model.fit_predict(scaled_data)
    data['Cluster'] = cluster_labels

    # PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(scaled_data)
    plt.figure(figsize=(8, 6))
    plt.scatter(principal_components[:, 0], principal_components[:, 1],
                c=data['Cluster'])
    plt.xlabel('First principal component')
    plt.ylabel('Second Principal Component')
    plt.show()

    return data
