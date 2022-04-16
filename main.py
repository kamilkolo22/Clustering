import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import os
from DataPreprocessing import *


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

    # print(data2)
    # print(data2.columns)
    # print(set(data2['Publisher']))
    # print(set(data2['Genre']))

    # map_race = {'group B': 1, 'group C': 2, 'group E': 3, 'group D': 4, 'group A': 5}
    # data1['race/ethnicity'] = data1['race/ethnicity'].map(map_race)
    # print(data1.head())
