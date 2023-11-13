import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_data(data, title):
    ''' 
    Plot the data.

    Parameters:
    - data (pd.DataFrame): Input data.
    - title (str): Title of the plot.

    Returns:
    - None

    Prints:
    - Plot of the data.
    '''
    plt.figure(figsize=(10, 5))
    plt.plot(data['date'], data['value'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

def fit_linear_trend(data):
    """
    Fit a linear trend to the data and return trend parameters.

    Parameters:
    - data (pd.DataFrame): Time series data with 'date' and 'value' columns.

    Returns:
    - Tuple[float, float]: Trend parameters (alpha_1, alpha_0).
    """
    # Ensure 'date' column is in datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Reshape the input data to 2D array
    X = data['date'].values.reshape(-1, 1)
    y = data['value'].values

    reg = LinearRegression()
    reg.fit(X, y)

    alpha_1 = reg.coef_[0]
    alpha_0 = reg.intercept_

    return (alpha_1, alpha_0)
   

def subtract_trend(data, trend_parameters):
    """
    Subtract the trend from the data.

    Parameters:
    - data (pd.Series): Time series data.
    - trend_parameters (Tuple[float, float]): Trend parameters (alpha_1, alpha_0).

    Returns:
    - pd.Series: Detrended data.
    """
    # Implementation goes here
    pass


if __name__ == '__main__':
    # Load data
    from preprocessing import load_data
    cpi_path = 'data/raw/CPI.csv'
    ber_path = 'data/raw/T10YIE.csv'
    cpi = load_data(cpi_path)
    ber = load_data(ber_path)
    print(cpi.head())
    print(ber.head())

    # # Plot data
    # plot_data(cpi, 'CPI')
    # plot_data(ber, 'BER')

    # Fit linear trend
    cpi_trend_parameters = fit_linear_trend(cpi)
    ber_trend_parameters = fit_linear_trend(ber)
    print(cpi_trend_parameters)
    print(ber_trend_parameters)