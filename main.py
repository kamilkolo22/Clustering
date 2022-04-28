from DataPreprocessing import *
from Hierarchy import *
from Visualisation import *


if __name__ == "__main__":
    # os.chdir(os.path.dirname(__file__))
    # pd.set_option('display.expand_frame_repr', False)

    data_raw = read_data('input/StudentsPerformanceMuricanUniversity.csv')
    adjusted_data = adjust_students_data(data_raw)
    clusters = find_cluster(adjusted_data)

    dfClusters = []
    for cluster in clusters:
        dfClusters.append(data_raw.iloc[list(cluster)])

    dfClusters = arrange_clusters(dfClusters)

    plot_compare_clusters(dfClusters)

    # data2 = pd.read_csv('input/VideoGamesSales.csv')
    # corrMatrix = adjusted_data.corr()
    # print(get_dist_matrix(adjusted_data, corrMatrix))

    # corrMatrix = adjusted_data.corr()
    # sn.heatmap(corrMatrix, annot=True)
    # plt.show()

    # import scipy.cluster.hierarchy as hier
    #
    # Z = hier.linkage(adjusted_data, method='complete', metric='mahalanobis')
    # print(Z)
    # plt.figure(figsize=(25, 10))
    # plt.title('Dendrogram')
    # plt.xlabel('sample index')
    # plt.ylabel('distance')
    # hier.dendrogram(
    #     Z,  # Macierz linkage
    #     leaf_rotation=90.,  # Zachęcam do pokombinowania z tym ;)
    #     leaf_font_size=15.,  # Rozmiar czcionki na osi X
    #     truncate_mode='level',  # A co by było, gdyby nie ucinać dendrogramu?
    #     p=5  # Poziom rozgałęzienia
    # )
    # max_d = 3.5
    # plt.axhline(y=max_d,
    #             c='k')  # Dorysowanie czarnej poziomej linii na wysokości max_d
    # plt.show()

    # print(data2.head())
    # print(data2.columns)
    # print(set(data2['Platform']))
    # print(set(data2['Genre']))
    # print(set(data2['Publisher']))
