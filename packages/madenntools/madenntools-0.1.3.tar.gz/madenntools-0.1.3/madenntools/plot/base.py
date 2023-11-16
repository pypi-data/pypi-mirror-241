import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

def _get_combined_df(input_path):
    
    """
    Create a combined DataFrame by reading multiple CSV files in a directory.

    Parameters:
    input_path (str): Path to the directory containing CSV files.

    Returns:
    combined_df (pandas.DataFrame): A single DataFrame combining data from all CSV files.
    """

    dataframes = []
    labels = []

    # Iterate over files in the directory
    for filename in os.listdir(input_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_path, filename)
            df = pd.read_csv(file_path)
            dataframes.append(df)
            labels.append(filename)  # Store labels for differentiation

    # Concatenate the DataFrames into a single DataFrame
    combined_df = pd.concat(dataframes, keys=labels, names=['CSV File'])

    return combined_df

def boxplot_from_csv_dir(input_path, metric, output=None):
    """
    Create a boxplot to visualize a specific metric from a combined DataFrame.

    Parameters:
    input_path (str): Path to the directory containing CSV files.
    metric (str): The metric to be plotted.
    output (str): Name to save the boxplot.

    Returns:
    None
    """

    input_df = _get_combined_df(input_path)
    
    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 6))  

    sns.boxplot(data=input_df, x=metric, y='CSV File', orient='h')
    plt.xlabel(metric)
    plt.ylabel('File name')
    plt.title(f'Boxplot for {metric}')

    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=300)
    else:
        plt.show()

def histogram_from_df(df, metric_name, bin_width, output=None, title=None):

    """
    Create a histogram from a CSV file, visualizing a specific metric.

    Parameters:
    df (pandas dataframe): a Pandas dataframe containing the data for at least 1 metric (or any category name)
    metric_name (str): The name of the metric to be plotted.
    bin_width (float): Width of the bins for the histogram.
    output (str): Path to save the histogram plot. If None, the plot will not be saved, but shown.

    Returns:
    None
    """
    
    df.dropna()

    scores = df[metric_name].values

    max_score = max(scores)
    bins = np.arange(0, max_score + 0.1, bin_width)
                     
    hist, _= np.histogram(scores,bins=bins)

    plt.figure(figsize=(10,6))
    plt.hist(scores, bins, edgecolor='k')

    plt.xlabel(metric_name)
    plt.ylabel('Frequency')
    if title:
        plt.title(f'{metric_name} for {title}')
    else:
        plt.title(f'{metric_name}')

     # Display y values on top of each bin
    for i in range(len(hist)):
        plt.text(bins[i] + (bins[i+1] - bins[i]) / 2, hist[i], str(hist[i]), ha='center', va='bottom')

    if output:
        plt.savefig(output, dpi=300)
    else:
        plt.show()

def violin_plot_from_df_pair(dataframes, metric, output=None, labels=None):
    """
    Create a violin plot comparing two datasets from CSV files.

    Parameters:
    dataframes (list): List of pandas DataFrames.
    metric (str): The column to use for the violin plot. Ex: ALL_Score
    output (str): Path to save the plot. If None, the plot will not be saved, but shown.
    labels (list): List of labels for the two datasets. if None, the labels will be 'Dataset 1' and 'Dataset 2'.

    Returns:
    None -> saves the plot figure 
    """

    assert len(dataframes) == 2, 'This function is designed to compare two datasets only.'
    
    if labels is None:
        labels = ['Dataset 1', 'Dataset 2']
    else:
        assert len(labels) == 2, 'Please provide two labels for the two datasets.'

    # Create a single violin plot
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

    # Loop through the DataFrames and plot violin plots
    for df, label in zip(dataframes, labels):
        sns.violinplot(y=df[metric], label=label, inner='quart',orient='v')
    
    # Customize the plot (e.g., labels, titles, etc.)
    plt.xlabel('Files')
    plt.ylabel(metric)
    plt.title( labels[0]+ 'vs' + labels[1])
    plt.legend()

    if output:
        plt.savefig(output, dpi=300)
    else:
        plt.show()
