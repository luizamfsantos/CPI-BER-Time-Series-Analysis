import pandas as pd
from sklearn.metrics import mean_squared_error

def rsme(predicted, actual):
    """
    Calculate the root mean squared error (RSME) of the residuals.

    Parameters:
    - residuals (pd.Series): Residuals from model.

    Returns:
    - float: RSME of the residuals.
    """
    # Calculating the RSME
    rsme = mean_squared_error(actual, predicted)**0.5

    return rsme


if __name__ == '__main__':
    pass