import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import statsmodels.api as sm


def plot_acf_pacf(residuals):
    """
    Plot autocorrelation and partial autocorrelation functions of the residuals.

    Parameters:
    - residuals (pd.Series): Residuals from the ARMA model.
    """
    # Plot autocorrelation function
    plot_acf(residuals, lags=20, title='Autocorrelation Function (ACF)')
    plt.show()

    # Plot partial autocorrelation function
    plot_pacf(residuals, lags=20, title='Partial Autocorrelation Function (PACF)')
    plt.show()

def fit_arma_model(data, order):
    """
    Fit an ARMA model to the data and return model parameters.

    Parameters:
    - data (pd.Series): Time series data.
    - order (Tuple[int, int]): Order of the ARIMA model (p, d, q).

    Returns:
    - Model: Fitted ARIMA model.
    """
    model = sm.tsa.ARIMA(data, order=order)
    results = model.fit()

    return results


if __name__ == '__main__':
    # Load data
    from preprocessing import load_indexed_data
    path_cpi_train_residuals = 'data/processed/cpi_train_residuals.csv'
    cpi_train_residuals = load_indexed_data(path_cpi_train_residuals)
    
    # Plot ACF and PACF
    # plot_acf_pacf(cpi_train_residuals['residuals'])

    # Fit AR(2)
    order = (2, 0, 0)
    model = fit_arma_model(cpi_train_residuals['residuals'], order)

    # Return model summary
    print(model.summary())

    # Print model parameters
    print('Model parameters:', model.params)

    # Calculate RSME
    rmse = model.resid.std()
    print(rmse)