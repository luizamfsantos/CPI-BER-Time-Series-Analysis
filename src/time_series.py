import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
from statsmodels.tsa.api import AutoReg


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
    - order (Tuple[int, int]): Order of the ARMA model (p, q).

    Returns:
    - Model: Fitted ARMA model.
    """
    p, q = order

    # Fit ARMA model
    model = AutoReg(data, lags=p, trend='c')  # 'c' includes a constant term
    fitted_model = model.fit()

    return fitted_model



if __name__ == '__main__':
    # Load data
    from preprocessing import load_indexed_data
    path_cpi_train_residuals = 'data/processed/cpi_train_residuals.csv'
    cpi_train_residuals = load_indexed_data(path_cpi_train_residuals)
    
    # Plot ACF and PACF
    # plot_acf_pacf(cpi_train_residuals['residuals'])

    # Fit AR(2)
    order = (2, 0)
    model = fit_arma_model(cpi_train_residuals['residuals'], order)

    # Return model summary
    print(model.summary())

    # Print model parameters
    print('Model parameters:', model.params)

    # Decompose model parameters
    phi_1 = model.params[1]
    phi_2 = model.params[2]

    # Save model parameters
    model_parameters_df = pd.DataFrame({'phi_1': [phi_1], 'phi_2': [phi_2]})
    model_parameters_df.to_csv('data/processed/arma_model_params.csv', index=False)