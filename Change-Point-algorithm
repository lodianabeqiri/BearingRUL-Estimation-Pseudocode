'''
This file contains a pseudocode of the function used to detect the changing points of a damaged bearing signal
 and establish a threshold to differentiate the three states the signal travels through before failure: healthy, degradation, and failure.

'''
import ruptures as rpt

function detect_change_points(df, pen=10, result='index')

    algorithm = initialize rpt.Pelt(model="rbf").fit(df)
    predict = algorithm.predict(pen=pen)
    n_bkps = 2
    draw_bkps(length(df), n_bkps)
    rpt.display(df, pred, pred)

    if result is 'index' then
         return predict
    else
        val = initialize empty list
    for ind in range length(pred) - 1
         val.append(df[pred[ind]])
    return val

