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
    data = remove_missing_values(data)
    return data

def load_indexed_data(file_path):
    """
    Load csv data from a given path.

    Parameters:
    - file_path (str): Path to the data file.

    Returns:
    - pd.DataFrame: Loaded data.
        Correctly formatted data should have two columns:
        - t: Time index of the observation
        - value: Value of the observation
    """
    data = pd.read_csv(file_path)
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

def remove_missing_values(data):
    ''' 
    Handle missing values in the data.
    Remove the rows with missing values.

    Parameters:
    - data (pd.DataFrame): Input data.

    Returns:
    - pd.DataFrame: Updated data.
    '''
    # Check if there are NaN in the 'values' column
    if data['value'].isnull().values.any():
        # Remove rows with NaN
        data = data.dropna()
    # Check if there are NaN in the 'date' column
    if data['date'].isnull().values.any():
        # Remove rows with NaN
        data = data.dropna()
    return data

def daily_to_monthly(data):
    ''' 
    Take the first observation of each month.
    Consider that some months don't have observation for day 1,
    in which case the first observation of the month is the first
    observation of the month with an observation.
    For example, January has no observation for day 1 until day 24,
    in which case the first observation of January is the observation
    of day 24.

    Parameters:
    - data (pd.DataFrame): Input data.

    Returns:
    - pd.DataFrame: Data with only the first observation of each month.
    '''
    # Ensure that the 'date' column is of datetime type
    assert data['date'].dtype == 'datetime64[ns]', "The 'date' column must be of datetime64[ns] type."
    
    # Group by month and find the minimum date for each month
    monthly_data = data.sort_values('date').groupby(data['date'].dt.to_period("M")).first().reset_index(drop=True)

    # Alter the date to be the first day of the month
    monthly_data['date'] = monthly_data['date'].dt.to_period('M').dt.to_timestamp()

    return monthly_data


def create_index(data, start_date=None):
    '''
    Create an index column for the data based on date. 
    It increases by 1 each month.
    If start_date is not specified, the first date of the data is used.

    Parameters:
    - data (pd.DataFrame): Input data.

    Returns:
    - pd.DataFrame: Data with an index column.
    '''
    # Ensure that there is only one entry per month
    unique_month_count = len(data['date'].dt.to_period('M').dt.to_timestamp().unique())
    assert len(data['date']) == unique_month_count, "There should be only one entry per month."

    # Ensure that the 'date' column is sorted, if not, sort it
    if not data['date'].is_monotonic_increasing:
        data = data.sort_values('date').reset_index(drop=True)
    
    # If not specified, use the first date of the data at time 0
    if start_date is None:
        start_date = data['date'].min() 
    
    # Convert dates without a day to the first day of the month
    data['date'] = data['date'].apply(lambda x: x + pd.offsets.MonthBegin(0))
    
    # Create the index column called 't'
    data['t'] = (data['date'].dt.to_period('M') - start_date.to_period('M')).apply(lambda x: x.n)

    return data

def split_data(data, split_date):
    ''' 
    Split the data into two parts based on a given date.

    Parameters:
    - data (pd.DataFrame): Input data.
    - split_date (str): Date to split the data.

    Returns:
    - Tuple[pd.DataFrame, pd.DataFrame]: The two parts of the data.
    '''
    # Assuming the DataFrame has a datetime column named 'date'
    data['date'] = pd.to_datetime(data['date'])

    # Split the data into two parts based on the given date
    train = data[data['date'] < split_date]
    test = data[data['date'] >= split_date]

    return train, test

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


if __name__ == '__main__':
    # Load data
    path_cpi_train = 'data/processed/cpi_train.csv'
    cpi_train = load_data(path_cpi_train)
    path_cpi_test = 'data/processed/cpi_test.csv'
    cpi_test = load_data(path_cpi_test)

    # Calculate monthly
    cpi_train_monthly = daily_to_monthly(cpi_train)
    cpi_test_monthly = daily_to_monthly(cpi_test)

    # Create index
    cpi_train_monthly = create_index(cpi_train_monthly)
    cpi_test_monthly = create_index(cpi_test_monthly, start_date=cpi_train_monthly['date'].min())

    # # Print data
    # print(cpi_train_monthly.head())
    # print(cpi_train_monthly.tail())
    # print(cpi_test_monthly.head())
    # print(cpi_test_monthly.tail())

    # Save indexed data, but only keep the 't' and 'value' columns
    cpi_train_monthly[['t', 'value']].to_csv('data/processed/cpi_train_indexed.csv', index=False)
    cpi_test_monthly[['t', 'value']].to_csv('data/processed/cpi_test_indexed.csv', index=False)