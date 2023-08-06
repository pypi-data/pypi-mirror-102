import pandas as pd

def time_slice(df, time_period):
    """For a `time_period`, creates a dataframe with a row for each country and a column for each AQUASTAT variable.

    Args:
        df: :obj:`pandas.DataFrame` with the columns, `country`, `variable`, `value`, and `time period`
        time_period: time period for filtering the data set and pivoting

    Returns:
        df (:obj:`pandas.DataFrame`): Pivoted dataframe

    """
    if not isinstance(df, pd.DataFrame):
        log_error(msg = 'Check that you have the right input format: Pandas DataFrame!')
        raise TypeError("Provided argument `df` is not a Panda's DataFrame object")
        
    # Only take data for time period of interest
    df = df[df.time_period == time_period]

    # Pivot table
    df = df.pivot(index='country', columns='variable', values='value')

    df.columns.name = time_period

    return df
  
  
def country_slice(df, country):

    """For a `country`, creates a dataframe with a row for each AQUASTAT variable and a column for each time period."""
    
    if not isinstance(df, pd.DataFrame):
        log_error(msg = 'Check that you have the right input format: Pandas DataFrame!')
        raise TypeError("Provided argument `df` is not a Panda's DataFrame object")

    # Only take data for country of interest
    df = df[df.country == country]

    # Pivot table
    df = df.pivot(index='variable', columns='time_period', values='value')
    df.index.name = country
    return df
  
  
  
def variable_slice(df, variable):
    
    """For a `variable`, creates a dataframe with a row for each country and a column for each time period."""

    if not isinstance(df, pd.DataFrame):
        log_error(msg = 'Check that you have the right input format: Pandas DataFrame!')
        raise TypeError("Provided argument `df` is not a Panda's DataFrame object")
        
    df = df[df.variable == variable]
    df = df.pivot(index='country', columns='time_period', values='value')
    return df
