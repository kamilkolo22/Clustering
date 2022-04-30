import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_compare_clusters(df_clusters):
    """Create and write to a file violin plot for each cluster"""
    i = 1
    for cluster in df_clusters:
        plt.figure(figsize=(12, 6))
        sns.violinplot(x='parental level of education', y='math score',
                       data=cluster,
                       hue='gender', split=True)
        plt.savefig(f'output/comparison/ViolinPlot_cluster{i}.png')
        i += 1
    return


def plot_games_sales(data_plot):
    """Bar plots for sales and different Publisher, Platform and Genre"""
    plt.figure(figsize=(20, 6), dpi=100)
    sns.barplot(x='Publisher', y='Sales', estimator=np.sum,
                data=data_plot, hue='Region')
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.savefig('output/games/Publisher.png')

    plt.figure(figsize=(12, 6), dpi=100)
    sns.barplot(x='Platform', y='Sales', estimator=np.sum,
                data=data_plot, hue='Region')
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.savefig('output/games/Platform.png')

    plt.figure(figsize=(12, 6), dpi=100)
    sns.barplot(x='Genre', y='Sales', estimator=np.sum,
                data=data_plot, hue='Region')
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.savefig('output/games/Genre.png')
    return
