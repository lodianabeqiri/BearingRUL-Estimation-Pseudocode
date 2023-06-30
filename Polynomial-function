'''
This script contains the pseudocode for implementing Polynomial Regression. 

'''

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt


"Fitting Polynomial Regression to data""
function poly_fit(x_data, y_data, deg)

    // Fit polynomial using linear regression
    poly = initialize
    PolynomialFeatures(degree=deg)
    x_poly = poly.fit_transform(x_data)
    model = initialize LinearRegression()
    model.fit(x_poly, y_data)

    // Predict
    pred = model.predict(poly.fit_transform(x_data))

    // Evaluate
    score = model.score(X_poly, y_data)
    display 'score: ' + score
    rmse = square_root(mean_squared_error(y_data, pred))
    display 'RMSE ' + rmse


"""Find the nearest value in array"""
function find_nearest(array, value):
    array = convert_to_array(array)
    idx = argmin(abs(array - value))
    return array[idx]

'''
  For a given y value (exp carpet values) the function find_x_from_y returns it's corresponding time, x values
  Steps: Subtract the y value, fit a polynomial, then find the roots of it.
  The roots are the values of x for which P(x) is equal to zero 
'''
function find_x_from_y(x, y, deg, value, max=1E-6, threshold=value):
    if value > threshold:
        value = threshold
    # calculate the roots
    r = roots(polyfit(x, y - value, deg))
    nearest = []
    for time in x:

    a = find_nearest(r.real,time)
    nearest.append(a)
    #convert list to value
    x1 = nearest[0]

    #otherwise it shall return value from the fitted fn
    if x1 < 0:
        #index = list(y[y == value].index)[1]
        index = y.index[y[:] == value].tolist()
        x1 = x.loc[index]
    return x1

