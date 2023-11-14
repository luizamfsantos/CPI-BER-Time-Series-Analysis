def plot_acf_pacf(residuals):
    """
    Plot autocorrelation and partial autocorrelation functions of the residuals.

    Parameters:
    - residuals (pd.Series): Residuals from the ARMA model.
    """
    # Implementation goes here
    pass

def fit_arma_model(data, order):
    """
    Fit an ARMA model to the data and return model parameters.

    Parameters:
    - data (pd.Series): Time series data.
    - order (Tuple[int, int]): Order of the ARMA model (p, q).

    Returns:
    - Model: Fitted ARMA model.
    """
    # Implementation goes here
    pass

if __name__ == '__main__':
    # Load data
    from preprocessing import load_indexed_data
    path_cpi_train_residuals = 'data/processed/cpi_train_residuals.csv'
    cpi_train_residuals = load_indexed_data(path_cpi_train_residuals)
    print(cpi_train_residuals.head())