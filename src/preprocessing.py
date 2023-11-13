import pandas as pd

def load_data(file_path):
    """
    Load csv data from a given path.

    Parameters:
    - file_path (str): Path to the data file.

    Returns:
    - pd.DataFrame: Loaded data.
        Correctly formatted data should have two columns:
        - date: Date of the observation
        - value: Value of the observation
    """
    data = pd.read_csv(file_path)
    data = update_dtypes(data)
    return data

def update_dtypes(data):
    '''
    Update the data types of the columns.
    Each dataset should have a data column and a float column.

    Parameters:
    - data (pd.DataFrame): Input data.

    Returns:
    - pd.DataFrame: Updated data.
    '''
    data.columns = ['date', 'value']
    data['date'] = pd.to_datetime(data['date'])
    data['value'] = pd.to_numeric(data['value'])
    return data


def calculate_yearly_average(data):
    """
    Calculate the yearly average of a given variable.

    Parameters:
    - data (pd.DataFrame): Input data.

    Returns:
    - pd.Series: Yearly averages.
    """
    # Implementation goes here
    pass

def subset_data(data, start_date, end_date):
    """
    Subset data based on specified date ranges.

    Parameters:
    - data (pd.DataFrame): Input data.
    - start_date (str): Start date for the subset.
    - end_date (str): End date for the subset.

    Returns:
    - pd.DataFrame: Subset of the data.
    """
    # Implementation goes here
    pass

if __name__ == '__main__':
    # Load data
    cpi_path = 'data/raw/CPI.csv'
    ber_path = 'data/raw/T10YIE.csv'
    cpi = load_data(cpi_path)
    ber = load_data(ber_path)
    print(cpi.head())
    print(ber.head())