# BearingRUL-Estimation-Pseudocode
Project Overview:
Gearbox bearing are continuously exposed to challenging working conditions and therefore various maintenance strategies have been introduced over time to improve their operational efficiency. The project introduces a machine learning-based method for calculating the RUL of railway gearbox bearings. The method uses unlabeled mechanical vibration signals from gearbox bearings to detect patterns of increased bearing wear and predict the component's remaining useful life. It combines a data smoothing method, a change point algorithm to set thresholds, and regression models for prediction.

While the source code of our project remains proprietary, we have made the effort to provide pseudocode to generalize the main idea in this GitHub repository.
The course code in implemented in python, and but the pseudocode is not tied to any specific programming language.

Organization of the Repository:
The repository contains many text files containing pseudocode for the following functions: Change-Point-algorithm, Main, Outliers-Removal, Polynomial-function, Preprocessing-function, and RUL-Calculation.
The main function calculates the remaining useful life for provided gearbox data and makes use of all other functions such as preprocessing to preprocess the data and outliers-removal to find and handle outliers using one-class SVM. It uses the Change point technique to construct thresholds to identify if the signals provided are in a healthy state, and then it trains the polynomial regression on the data and estimates the remaining useful life using the RUL-Calculations routines. Each file is accompanied by remarks about the file's functionality. 


Pseudocode Examples:
Include specific examples of pseudocode from your project in the README file. You can use code blocks or indentation to format and present the pseudocode clearly. For each example, provide a brief explanation of the logic or algorithm it represents. Consider including annotations or comments to clarify any complex parts or assumptions made in the pseudocode.

Project Requirements and Setup Instructions:
It is important to import the libraries required to implement and run the code inspired by the pseudocode.


Contact Information: lodiana.beqiri@mdu.se
