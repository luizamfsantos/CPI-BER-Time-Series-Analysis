import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def train_linear_regression(X, y):
    """
    Trains a linear regression model on the given input features X and target variable y.

    Parameters:
    X (array-like): Input features.
    y (array-like): Target variable.

    Returns:
    model: Trained linear regression model.
    """
    X_reshaped = np.array(X).reshape(-1, 1)
    model = LinearRegression().fit(X_reshaped, y)
    return model

def get_linear_coefficients(model):
    """
    Returns the coefficients of a linear regression model.

    Parameters:
    model (object): The linear regression model.

    Returns:
    list: A list containing the coefficients [slope, intercept].
    """
    coefficients = [model.coef_[0], model.intercept_]
    return coefficients

def print_linear_equation(coefficients):
    """
    Prints the linear equation representing the trend.

    Parameters:
    coefficients (list): A list of two coefficients representing the slope and intercept of the linear equation.

    Returns:
    None
    """
    print(f'The linear trend is given by F(t) = {coefficients[0]:.2f} * t + {coefficients[1]:.2f}')

def calculate_trend(X, y):
    """
    Calculates the trend using linear regression.

    Parameters:
    X (array-like): The independent variable.
    y (array-like): The dependent variable.

    Returns:
    coefficients (array-like): The coefficients of the linear regression model.
    """
    model = train_linear_regression(X, y)
    coefficients = get_linear_coefficients(model)
    print_linear_equation(coefficients)
    return coefficients

def predict_with_linear_model(model, X):
    """
    Predicts the output using a linear model.

    Parameters:
        model (object): The trained linear model.
        X (array-like): The input data.

    Returns:
        array-like: The predicted output.
    """
    return model.predict(X)
   
def predict_from_linear_coefficients(coefficients, X):
    """
    Predicts the values of Y based on the linear coefficients and input values X.

    Parameters:
        coefficients (list): A list of two coefficients [a, b], where a is the slope and b is the intercept.
        X (float or array-like): The input values.

    Returns:
        float or array-like: The predicted values of Y.

    """
    return coefficients[0] * X + coefficients[1]

def subtract_linear_trend(t,value, trend_parameters):
    """
    Subtract the trend from the data.

    Parameters:
    - t (pd.Series): Time index.
    - value (pd.Series): Data.
    - trend_parameters (Tuple[float, float]): Trend parameters (alpha_1, alpha_0).

    Returns:
    - residuals (pd.Series): Residuals.
        
    """
    # Calculate trend
    trend = predict_from_linear_coefficients(trend_parameters, t)

    # Subtracting the trend from the data
    residuals = value - trend
    
    return residuals



if __name__ == '__main__':
    pass