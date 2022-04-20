import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import os
from DataPreprocessing import *
from Hierarchy import *
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets

if __name__ == "__main__":
    # os.chdir(os.path.dirname(__file__))
    data1 = pd.read_csv('input/StudentsPerformanceMuricanUniversity.csv', na_values='no data')
    data2 = pd.read_csv('input/VideoGamesSales.csv')

    data2 = adjust_games_data(data2)

    adjusted_data = adjust_students_data(data1)
    print(adjusted_data.head())
    # print(linkage(adjusted_data))
    corrMatrix = adjusted_data.corr()
    # print(get_dist_matrix(adjusted_data, corrMatrix))

    # corrMatrix = adjusted_data.corr()
    # sn.heatmap(corrMatrix, annot=True)
    # plt.show()

    # import scipy.cluster.hierarchy as hier
    #
    # Z = hier.linkage(adjusted_data, method='complete', metric='mahalanobis')
    #
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

    # pd.set_option('display.expand_frame_repr', False)
    # print(data2.head())
    # print(data2.columns)
    print(set(data2['Publisher']))
    print(set(data2['Genre']))
    l = list(set(data2['Platform']))
    l.sort()
    print(l)
    print(set(data2['Year']))
    print(data2['Zelda' in data2['Name']])
    # print(data2[['Rank', 'Publisher']].groupby('Publisher').count().sort_values(by=['Rank']))
    # print(data2.describe())
