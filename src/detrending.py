import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_data(data, x_col, y_col, title, x_label, y_label):
    ''' 
    Plot the data.

    Parameters:
    - data (pd.DataFrame): Input data.
    - x_col (str): Column name for x-axis.
    - y_col (str): Column name for y-axis.
    - title (str): Title of the plot.
    - x_label (str): Label for the x-axis.
    - y_label (str): Label for the y-axis.

    Returns:
    - None

    Prints:
    - Plot of the data.
    '''
    plt.figure(figsize=(10, 5))
    plt.plot(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def fit_linear_trend(data):
    """
    Fit a linear trend to the data and return trend parameters.

    Parameters:
    - data (pd.DataFrame): Time series data with index 't' int and 'value' columns.

    Returns:
    - Tuple[float, float]: Trend parameters (alpha_1, alpha_0).
    """
    reg = LinearRegression()
    reg.fit(data[['t']], data['value'])

    alpha_1 = reg.coef_[0]
    alpha_0 = reg.intercept_

    return (alpha_1, alpha_0)
   

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

    # Subtract trend
    residuals = subtract_trend(cpi_train_monthly, trend_parameters)

    # Print maximum value of residuals
    print('Maximum value of residuals:', residuals['residuals'].max())

    # Plot residuals
    # plot_data(residuals, 't', 'residuals', 'Residuals', 'Time', 'Residuals')

    # Save residuals
    residuals.to_csv('data/processed/cpi_train_residuals.csv', index=False)