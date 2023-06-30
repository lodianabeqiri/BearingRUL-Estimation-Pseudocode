""" this file contains the pseudocode for the data preparation functions"""

# Fill the dataframe NaN values by the mean of each column
function fill_nan(df):
    df = fill_nan_with_mean(df)
    return df

# Normalization of the dataframe df using MinMaxScaler from sklearn library
function normalize_df(df):
     scaler = MinMaxScaler(feature_range=(0, 1))
     names = df.columns
     d = scaler.fit_transform(df)
     df = DataFrame(d, columns=names)
     return df

"Apply savgol_filter"
function filter_signal(df, window_size =51, order= 3):
    '''
    This function filters the signal using savgol_filter
    :param df: series
    :param window_size: the length of the filter window, must be a positive odd integer
    :param order: the order of the polynomial used to fit the samples
    :return: the filtered data with same shape as df in a form of ndarray
    '''
    yhat = savgol_filter(df, window_size, order)  # window size 51, polynomial order 3
    df = create_series(yhat)
    return df


function detect_state(df, degradation_threshold = 3, fail_threshold=17):
    '''
    The signals are in their original values, not normalized, and the function displays if a signal has
    entered the deterioration phase by comparing it to a predefined threshold.
    The degradation threshold is set to amplitude 3 and for failure is set up to 17.

    :param df: pandas series
    :param degradation_threshold: predefined parameter to define degradation state
    :param fail_threshold: pre-defined parameter to define the failure state
    :return: an integer related to the state: 0 if the signal has already failed
                                            1 if the signal has entered the degradation state
                                            and 2 if the signal is healthy

    Steps:
        -filter the signal with savgol_filter
        -compare the maximum of signal with the thresholds to find its state
        -print the signal state
    '''

    if df.max() > fail_threshold:
        display'The signal has already FAILED!'
        return 0
    elif df.max() > degradation_threshold:
        display'ALERT: The signal has entered the DEGRADATION state'
        return 1
    else:
        display 'The bearing is in good operating condition as the signal is contained inside the HEALTHY zone.'
        return 2




