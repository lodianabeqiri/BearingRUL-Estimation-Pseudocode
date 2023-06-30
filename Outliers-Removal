""" This file includes the pseudocode function required for detecting and removing outliers.
"""

"""  Find outliers   """
function find_outliers(ts, perc=0.05, figsize=(15,5)):

    '''
    :param ts: is a series a column(and its index)
    :param perc: float - percentage of outliers to look for
    :param figsize: figure dimensions
    :return: a list with all outliers, just the indices of the series ts
    'outlier' is 1 if it is an outlier and is 0 if it's not an outlier, 1/0 (yes/no)
    '''
    ts_scaled = reshape_to_2D_array(ts)
    model = initialize OneClassSVM(nu=perc, kernel="rbf", gamma=0.01)
    model.fit(ts_scaled)

    dtf_outliers = ts.to_frame(name="ts")
    dtf_outliers["index"] = range(len(ts))
    dtf_outliers["outlier"] = model.predict(ts_scaled)
    dtf_outliers["outlier"] = dtf_outliers["outlier"].apply(lambda x: 1 if x == -1 else 0)

    return dtf_outliers[dtf_outliers["outlier"] == 1].index])

"""  Remove outliers   """
function remove_outliers(ts, outliers_idx = None):
    """
    :param ts:  is a series from which we want to eliminate outliers
    :param outliers_idx:  are indexes of outliers for this series
    :return: series with removed/replaced outliers
    Usage:
        remove_outliers(ts) - get outliers_index from inside function calling: find_outliers(ts)
        remove_outliers(ts, [3, 5, 7]) - enter the outliers_index as parameter
    """
    if outliers_idx == None:
        outliers_idx = find_outliers(ts)
    """ 
    To remove the outliers proceed as below:
        - replace all outliers with NaN values
        - use interpolate to replace nan values with a mean/median value
    """
    for i, val in enumerate(outliers_idx):
        ts.loc[val] = NaN

    # Replace the first value with the mean if it is NaN
    if isNaN(ts[0]):
        ts.loc[0] = calculate_mean(ts, skipna=True)

# Use Interpolate function to replace nan values with a mean/median value
    ts = ts.astype(float).interpolate(method='linear')
    #return series
    return ts

