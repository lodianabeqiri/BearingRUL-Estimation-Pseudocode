# BearingRUL-Estimation-Pseudocode
Project Overview:
Gearbox bearing are continuously exposed to challenging working conditions and therefore various maintenance strategies have been introduced over time to improve their operational efficiency. The project introduces a machine learning-based method for calculating the RUL of railway gearbox bearings. The method uses unlabeled mechanical vibration signals from gearbox bearings to detect patterns of increased bearing wear and predict the component's remaining useful life (RUL). It combines a data smoothing method, a change point algorithm to set thresholds, and regression models for prediction.

While our project's source code remains confidential, we have made an effort to share pseudocode that generalizes the basic notion in this GitHub repository.
The source code is written in Python, although the pseudocode is not bound to any computer language.

Organization of the Repository:
The repository contains many text files containing pseudocode for the following functions: Change-Point-algorithm, Main, Outliers-Removal, Polynomial-function, Preprocessing-function, and RUL-Calculation.
The main function computes the RUL for the provided gearbox data and employs all other functions, such as preprocessing to preprocess the data and outliers-removal to locate and handle outliers using one-class SVM. It uses the Change Point Technique to construct thresholds to identify if the signals are in a healthy state, and it trains the Polynomial Regression on the data and estimates the RUL. Each file is accompanied with comments describing its functioning. 

Project Requirements and Setup Instructions:
It is important to import the libraries required to implement and run the code inspired by the pseudocode.


Contact Information: lodiana.beqiri@mdu.se
