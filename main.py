from DataPreprocessing import *
from Hierarchy import *
from Visualisation import *
from ClusterQuality import *
from Kmeans import *


def analyse_school_data(plot=True):
    """Prepare analysis of Students Performance data"""
    data_raw = read_data('input/StudentsPerformanceMuricanUniversity.csv',
                         'school')
    # Prepare data to analysis
    adjusted_data = adjust_students_data(data_raw)
    # Find clusters
    clusters, dist_matrix = find_cluster(adjusted_data)
    df_clusters = []
    for cluster in clusters:
        df_clusters.append(data_raw.iloc[list(cluster)])
    df_clusters = arrange_clusters(df_clusters)
    # Prepare plots for all clusters
    if plot:
        plot_compare_clusters(df_clusters)

    # Quality of clusters using GDI index
    # print(f'GDI value: {gdi(clusters, dist_matrix)}')
    # print(f'BHI value: {bhi(clusters, dist_matrix)}')

    return df_clusters


def analyse_games_data(make_plot=True, stats=True):
    """Prepare analysis of Video Games Sales data"""
    data_raw = read_data('input/VideoGamesSales.csv', 'games')
    adjusted_data = adjust_games_data(data_raw)
    clustered_data = find_cluster_kmean(adjusted_data)

    # Make bar plots for sales in different regions
    if make_plot:
        data_plot = adjust_to_plot(data_raw)
        plot_games_sales(data_plot)

    if stats:
        # Create table with sales statistics for different
        # Platform, Genre and Publisher
        data_stats = data_raw[['Platform', 'Genre', 'Publisher', 'NA_Sales',
                               'EU_Sales', 'JP_Sales', 'Other_Sales']]
        data_stats = data_stats.groupby(by=['Platform', 'Genre', 'Publisher'])
        data_stats = data_stats.describe()
        data_stats.to_excel('output/games_stats.xlsx')
    return clustered_data


def predict_sales(platform, genre, publisher):
    """Show stats of games sales for given Platform, Genre and Publisher"""
    data_stats = read_excel('output/games_stats.xlsx')

    idx = pd.IndexSlice
    pred = data_stats.loc[(platform, genre, publisher),
                          idx[:, ['count', 'mean', 'std']]]
    pred_mean = pred.loc[(slice(None), 'mean')]
    pred_std = pred.loc[(slice(None), 'std')]
    pred_count = pred.loc[('NA_Sales', 'count')]

    print(f'Total sold games: {int(pred_count)}\n'
          f'Region \t mean \t std')
    for i, v in pred_mean.items():
        print(f'{i[:-6]},  {round(v, 4)},  {round(pred_std.loc[i], 4)}')

    return pred


if __name__ == "__main__":
    pd.set_option('display.expand_frame_repr', False)

    analyse_school_data(plot=True)

    # analyse_games_data(make_plot=False, stats=False)
    # predict_sales('PC', 'Action', 'Electronic Arts')
