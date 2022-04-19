import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import os
from DataPreprocessing import *
import numpy as np
from matplotlib import pyplot as plt
# redukcja wymiarów zbioru - na potrzeby wizualizacji grup
from sklearn.decomposition import PCA
# skalowanie zmiennych - wskazane przy metodach korzystających z miar odległości
from sklearn.preprocessing import StandardScaler
# biblioteki do grupowania hierarchicznego: sklearn i scipy
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

if __name__ == "__main__":
    # os.chdir(os.path.dirname(__file__))
    data1 = pd.read_csv('input/StudentsPerformanceMuricanUniversity.csv', na_values='no data')
    # data2 = pd.read_csv('input/VideoGamesSales.csv')

    adjusted_data = adjust_students_data(data1)
    print(adjusted_data.dtypes)

    corrMatrix = adjusted_data.corr()
    sn.heatmap(corrMatrix, annot=True)
    plt.show()

    print(mahalanobis_metric(list(adjusted_data.loc[1, :]),
                             list(adjusted_data.loc[2, :]),
                             corrMatrix))

    # pd.set_option('display.expand_frame_repr', False)
    # print(data2.head())
    # print(data2.columns)
    # print(set(data2['Publisher']))
    # print(set(data2['Genre']))
    # print(set(data2['Platform']))
    # print(data2[['Rank', 'Publisher']].groupby('Publisher').count().sort_values(by=['Rank']))
    # print(data2.describe())
