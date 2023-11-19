import pandas as pd
import unittest
import sys, os
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from src.preprocessing import daily_to_monthly

class TestDailyToMonthly(unittest.TestCase):
    def setUp(self):
        # Sample test data
        self.sample_data = pd.DataFrame({
            'date': pd.to_datetime(['2023-01-01', '2023-01-05', '2023-02-01', '2023-02-10']),
            'CPI': [100, 102, 105, 107]
        })

    def test_output_columns(self):
        # Test if the output dataframe has the correct columns
        result = daily_to_monthly(self.sample_data)
        self.assertTrue('year_month' in result.columns, "Missing 'year_month' column")
        self.assertEqual(set(result.columns), {'date', 'CPI', 'year_month'}, "Incorrect columns in the output")

    def test_output_length(self):
        # Test if the output dataframe has the correct number of rows
        result = daily_to_monthly(self.sample_data)
        expected_rows = 2  # Two months in the sample data: January and February
        self.assertEqual(len(result), expected_rows, f"Expected {expected_rows} rows in the output")

    def test_date_column_type(self):
        # Test if the 'date' column is of datetime type in the output
        result = daily_to_monthly(self.sample_data)
        self.assertEqual(result['date'].dtype, 'datetime64[ns]', "The 'date' column is not of datetime type")

    def test_year_month_format(self):
        # Test if the 'year_month' column has the correct format (YYYY-MM)
        result = daily_to_monthly(self.sample_data)
        year_month_values = result['year_month'].unique()

        for value in year_month_values:
            self.assertTrue(pd.to_datetime(value, errors='coerce').strftime('%Y-%m') == value,
                            f"Value {value} in 'year_month' column doesn't represent a valid year-month format")

if __name__ == '__main__':
    unittest.main()
