import pandas as pd

def rsme(residuals):
    """
    Calculate the root mean squared error (RSME) of the residuals.

    Parameters:
    - residuals (pd.DataFrame): Time series data with index 't' int and 'residuals' columns.

    Returns:
    - float: RSME of the residuals.
    """
    # Calculating the RSME
    rsme = (residuals['residuals']**2).mean()**0.5

    return rsme

if __name__ == '__main__':
    # Load validation data
    from preprocessing import load_data, split_data, daily_to_monthly, create_index
    path_cpi_test = 'data/processed/cpi_test.csv'
    cpi_test = load_data(path_cpi_test)

    # Calculate monthly
    cpi_test_monthly = daily_to_monthly(cpi_test)

    # Create index
    cpi_test_monthly = create_index(cpi_test_monthly, start_date = '2008-07-01')

    # Detrend data
    from detrending import subtract_trend
    trend_parameters_df = pd.read_csv('data/processed/trend_parameters.csv')
    alpha_0 = trend_parameters_df['alpha_0'][0]
    alpha_1 = trend_parameters_df['alpha_1'][0]
    trend_parameters = (alpha_1, alpha_0)
    residuals = subtract_trend(cpi_test_monthly, trend_parameters)
    print(residuals.head())

    # Subtract AR model
    from time_series import subtract_ar
    ar_params_df = pd.read_csv('data/processed/arma_model_params.csv')
    phi_1 = ar_params_df['phi_1'][0]
    phi_2 = ar_params_df['phi_2'][0]
    ar_params = (phi_1, phi_2)
    residuals = subtract_ar(residuals, ar_params)
    print(residuals.head())

    # Calculate RSME
    rsme = rsme(residuals)
    print('RSME:', rsme)