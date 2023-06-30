'''
Pseudocode of the function for calculating remaining useful life 

'''

import  Polynomial as poly

'''
Calculate actual Rul 
'''
function actual_RUL(x, rul):
      return rul - x

'''
Calculate estiamted Rul 
'''
function estimate_RUL(x_data, y_data, estimated_life_time):
    est_RUL = create empty list
    // Get the values of y
    for key, value in enumerate(y_data)
        // Invoke function find_x_from_y
        x1 = poly.find_x_from_y(x_data, y_data, 3, value, max=1E-6)
        b = estimated_life_time - x1
        est_RUL.append(b)
return est_RUL

'''
Calculate the error (root mean square)
'''
function rmse_calc(predictions, targets):
    return square_root(mean((predictions - targets) ** 2))


'''
Calculate the estimated error  
'''
function calculate_error_est(est_RUL, actual_RUL):
    return absolute_value(actual_RUL - est_RUL) / actual_RUL




