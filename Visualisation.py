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
