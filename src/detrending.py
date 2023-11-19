import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def train_linear_regression(X,y):
    model = LinearRegression().fit(X,y)
    return model

def get_linear_coefficients(model):
    coefficients = [model.coef_[0], model.intercept_]
    return coefficients

def print_linear_equation(coefficients):
    print(f'The linear trend is given by F(t) = {coefficients[0]:.2f} * t + {coefficients[1]:.2f}')

def predict_with_linear_model(model, X):
    return model.predict(X)
   

def subtract_trend(data, trend_parameters):
    """
    Subtract the trend from the data.

    Parameters:
    - data (pd.DataFrame): Time series data. 
        includes 't' and 'value' columns.
        't' is the time index.
        'value' is the value of the time series.
    - trend_parameters (Tuple[float, float]): Trend parameters (alpha_1, alpha_0).

    Returns:
    - pd.DataFrame: residuals.
        includes 't' and 'value' columns.
        't' is the time index.
        'value' is the value of the time series after subtracting the trend.
    """
    # Extracting trend parameters
    alpha_1, alpha_0 = trend_parameters
    
    # Subtracting the trend from the data
    data['residuals'] = data['value'] - (alpha_1 * data['t'] + alpha_0)
    
    # Creating a new DataFrame with time index and residuals
    residuals_data = data[['t', 'residuals']]
    
    return residuals_data



if __name__ == '__main__':
    # Load data
    from preprocessing import load_data, daily_to_monthly, create_index
    path_cpi_train = 'data/processed/cpi_train.csv'
    cpi_train = load_data(path_cpi_train)

    # Calculate monthly
    cpi_train_monthly = daily_to_monthly(cpi_train)

    # Create index
    cpi_train_monthly = create_index(cpi_train_monthly)
    
    # Plot data
    # plot_data(cpi_train_monthly, 'date', 'value', 'CPI', 'Time', 'CPI')

    # Fit linear trend
    trend_parameters = fit_linear_trend(cpi_train_monthly[['t','value']])
    print('Trend parameters:', trend_parameters)

    # # Save trend parameters
    # # uncouple tuple
    # alpha_1, alpha_0 = trend_parameters
    # trend_parameters_df = pd.DataFrame({'alpha_1': [alpha_1], 'alpha_0': [alpha_0]})
    # trend_parameters_df.to_csv('data/processed/trend_parameters.csv', index=False)

    # Subtract trend
    residuals = subtract_trend(cpi_train_monthly, trend_parameters)

    # Print maximum value of residuals
    print('Maximum value of residuals:', residuals['residuals'].max())

    # Plot residuals
    # plot_data(residuals, 't', 'residuals', 'Residuals', 'Time', 'Residuals')

    # Save residuals
    residuals.to_csv('data/processed/cpi_train_residuals.csv', index=False)