import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df,
               title='',
               xlabel=None,
               ylabel=None,
               label_size=20,
               tick_label_size=16,
               cmap=None,
               xticklabels=None,
               yticklabels=None,
               figsize=None,
               xrotation=90,
               yrotation=0,
               **kwargs):
  
    """
    Plots heatmap of variable_slice dataframe given across all countries and time periods.
    
    Parameters
    ----------
    df (pd.Dataframe) : a variable_slice dataframe
    title (str) : title of heatmap
    xlabel (str) : x-axis label
    ylabel (str) : y-axis label
    label_size (int) : label text size
    tick_label_size (int) : tick text size
    cmap (str) : colormap for heatmap
    xticklabels (str) : labels of x-axis ticks
    yticklabels (str) : labels of y-axis ticks
    figsize (int) : heatmap output figure size
    xrotation (int) : rotate x-axis tick labels by given number of degrees
    yrotation (int) : rotate y-axis tick labels by given number of degrees
    
    Other Parameters
    ----------------
    **kwargs : `-matplotlib.collections.LineCollection` properties
    
    
    Returns
    -------
    Matplotlib heatmap plot
     
    """
    
    
    if figsize is None:
        figsize = (16, 8)
    fig, ax = plt.subplots(figsize=figsize)

    if xlabel is None:
        xlabel = ' '.join(df.columns.name.split('_')).capitalize()
    if ylabel is None:
        ylabel = ' '.join(df.index.name.split('_')).capitalize()

    yticklabels = df.index.tolist() if yticklabels is None else yticklabels
    xticklabels = df.columns.tolist() if xticklabels is None else xticklabels

    if cmap is None:
        cmap = sns.cubehelix_palette(8, start=.5, rot=-.75)

    ax = sns.heatmap(df, cmap=cmap, **kwargs)
    ax.set_xticklabels(xticklabels, rotation=xrotation, size=tick_label_size)
    ax.set_yticklabels(yticklabels, rotation=yrotation, size=tick_label_size)

    ax.set_title(title, size=label_size)
    ax.set_xlabel(xlabel, size=label_size)
    ax.set_ylabel(ylabel, size=label_size)

    ax.set_ylim([0, len(df)])

    log_info(msg = "Plot generated for this variable!")
    return fig
  
  

def plot_histogram(df,
                 column,
                 title='',
                 xlabel=None,
                 ylabel=None,
                 label_size=20,
                 color='#0085ca',
                 alpha=0.8,
                 figsize=None,
                 **kwargs):
    """
    Plots histogram of time_slice dataframe given across all countries and time periods.

    Parameters
    ----------
    df (pd.Dataframe) : a time_slice dataframe
    column (str) : column of time_slice dataframe to view in histogram
    title (str) : title of histogram
    xlabel (str) : x-axis label
    ylabel (str) : y-axis label
    label_size (int) : label text size
    color (str) : color of histogram bars
    alpha (dbl) : transparency of histogram bars
    figsize (int) : histogram output figure size

    Other Parameters
    ----------------
    **kwargs : `-matplotlib.collections.LineCollection` properties


    Returns
    -------
    Matplotlib histogram plot

    """
  
    if figsize is None:
        figsize = (12, 8)
    fig, ax = plt.subplots(figsize=figsize)

    if xlabel is None:
        xlabel = ' '.join(column.split('_')).capitalize()
    if ylabel is None:
        ylabel = 'Count'

    ax.hist(df[column], color=color, alpha=alpha, **kwargs)

    ax.set_title(title, size=label_size)
    ax.set_xlabel(xlabel, size=label_size)
    ax.set_ylabel(ylabel, size=label_size)

    #log_info(msg = "Plot generated for this time frame!")
    return fig
