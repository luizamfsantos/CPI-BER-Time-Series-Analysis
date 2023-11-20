import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
from statsmodels.tsa.api import AutoReg
import numpy as np

def plot_acf_pacf(residuals):
    """
    Plot autocorrelation and partial autocorrelation functions of the residuals.

    Parameters:
    - residuals (pd.Series): Residuals from the ARMA model.
    """
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

    # Plot autocorrelation function
    plot_acf(residuals, lags=20, title='Autocorrelation Function (ACF)', ax=ax[0])

    # Plot partial autocorrelation function
    plot_pacf(residuals, lags=20, title='Partial Autocorrelation Function (PACF)', ax=ax[1])

    plt.tight_layout()
    plt.show()

def fit_arma_model(data, order):
    """
    Fit an ARMA model to the data and return model parameters.

    Parameters:
    - data (pd.Series): Time series data.
    - order (Tuple[int, int]): Order of the ARMA model (p, q).

    Returns:
    - Model: Fitted ARMA model.
    """
    p, q = order

    # Fit ARMA model
    model = AutoReg(data, lags=p, trend='c')  # 'c' includes a constant term
    fitted_model = model.fit()

    return fitted_model

def subtract_ar(data, ar_params):
    ''' 
    Subtract the AR model from the data.

    Parameters:
    - data (pd.DataFrame): Time series data with a column named 't'.
    - ar_params (Tuple[float]): Tuple of AR model parameters.

    Returns:
    - pd.DataFrame: DataFrame with original 't' and residuals from the AR model.
    '''
    # Extract the time series values from the 't' column
    time_series = data

    # Calculate the residuals using the AR model
    residuals = np.zeros_like(time_series)

    for i in range(len(ar_params), len(time_series)):
        for j in range(len(ar_params)):
            residuals[i] += ar_params[j] * time_series[i - j - 1]

    return residuals



if __name__ == '__main__':
    pass