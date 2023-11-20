import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
from statsmodels.tsa.api import AutoReg
import numpy as np
from src.validation import rsme

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


def plot_ar_rmse(data):
    """
    Create a scatter plot of RMSE values against the number of lags.

    Args:
    - data (list of tuples): A list of tuples where each tuple contains
                             an integer representing the number of lags
                             and a float representing the RMSE value.

    Returns:
    - None
    
    Prints:
    - A scatter plot of RMSE values against the number of lags.
    """

    # Unpack tuples into separate lists for n_values and rmse_values
    n_values, rmse_values = zip(*data)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title("RMSE of AR Models of order n")

    # Scatter plot
    scatter = ax.scatter(n_values, rmse_values, s=150, marker="s", color="orange", alpha=0.5, label="RMSE")

    # Set labels for x and y axes
    ax.set_xlabel('n')
    ax.set_ylabel('RMSE')

    # Show legend
    ax.legend(loc='upper right')

    # Show plot
    plt.show()

def fit_AR_model(residuals, num_lags):
    rmse_train = []

    for n in range(1, num_lags + 1):
        # fit AR model
        model = fit_arma_model(residuals, order=(n, 0))

        # predict residuals
        predictions = model.predict(start=n, end=len(residuals) - 1)

        # calculate RMSE
        rmse = rsme(predictions, residuals[n:])
        rmse_train.append((n, rmse))

    return rmse_train


if __name__ == '__main__':
    pass