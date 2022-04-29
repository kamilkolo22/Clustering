from DataPreprocessing import *
from Hierarchy import *
from Visualisation import *
import seaborn as sns


if __name__ == "__main__":
    pd.set_option('display.expand_frame_repr', False)

    # data_raw = read_data('input/StudentsPerformanceMuricanUniversity.csv',
    #                      'school')
    # adjusted_data = adjust_students_data(data_raw)
    # clusters = find_cluster(adjusted_data)
    #
    # dfClusters = []
    # for cluster in clusters:
    #     dfClusters.append(data_raw.iloc[list(cluster)])
    #
    # dfClusters = arrange_clusters(dfClusters)
    #
    # plot_compare_clusters(dfClusters)

    data_raw = read_data('input/VideoGamesSales.csv', 'games')
    # adjusted_data = adjust_games_data(data_raw)
    # data_plot = adjust_to_plot(data_raw)
    # plot_games_sales(data_plot)

    print(data_raw)

    data = data_raw[['Platform', 'Genre', 'Publisher', 'NA_Sales',
                    'EU_Sales',  'JP_Sales', 'Other_Sales']]
    data = data.groupby(by=['Platform', 'Genre', 'Publisher'])
    sales_pred = data.describe()
    print(sales_pred)

    print(sales_pred.loc[('PC', 'Action', 'Electronic Arts'), :][(slice(None), 'mean')])

    sales_pred.to_excel('output/games_stats.xlsx')

    # sns.catplot(x='Region', y='Sales', data=data_plot,
    #             kind='box', row='Genre',
    #             col='Publisher')
    # plt.show()

    # sns.heatmap(corrMatrix, annot=True)
    # plt.show()
