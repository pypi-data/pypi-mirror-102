import pandas as pd

def time_series(df, country, variable):
    
    """
    For a `country` and `variable`, creates a time series dataframe.
    
    Parameters
    -----
    df (pd.DataFrame) : A pandas dataframe with the columns `country` and `variable`.
    country (str) : An AQUASTAT country
    variable (str) : An AQUASTAT variable
    
    
    Returns
    -----
    series: a time series dataframe
    
    
    Notes
    -----
    Years with no data for the variable specified will be dropped.
    
    """

    if not isinstance(df, pd.DataFrame):
        log_error(msg = 'Check that you have the right input format: Pandas DataFrame!')
        raise TypeError("Provided argument `df` is not a Panda's DataFrame object")

    # Only take data for country/variable combo
    series = df[(df.country == country) & (df.variable == variable)]

    # Drop years with no data
    series = series.dropna()[['year_measured', 'value']]

    # Change years to int and set as index
    series.year_measured = series.year_measured.astype(int)
    series.set_index('year_measured', inplace=True)
    series.columns = [variable]

    return series
