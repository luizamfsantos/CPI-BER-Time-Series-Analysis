import pandas as pd

def rsme(residuals):
    """
    Calculate the root mean squared error (RSME) of the residuals.

    Parameters:
    - residuals (pd.Series): Residuals from model.

    Returns:
    - float: RSME of the residuals.
    """
    # Calculating the RSME
    rsme = (residuals**2).mean()**0.5

    return rsme

if __name__ == '__main__':
    pass