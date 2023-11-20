from src.preprocessing import load_data 

# load data
path_cpi = 'data/raw/CPI.csv'
cpi = load_data(path_cpi)

# create monthly data
from src.preprocessing import daily_to_monthly
monthly_cpi = daily_to_monthly(cpi)

# create index
from src.preprocessing import create_index
monthly_cpi['t'] = create_index(monthly_cpi, date_col='year_month',start_date=monthly_cpi['date'].min())

# split data
from src.preprocessing import split_data
split_date = '2013-09'
cpi_train, cpi_test = split_data(monthly_cpi, split_date=split_date, date_col='year_month')

# visualize data
# from src.utils_plot import plot_time_series
# plot_time_series(cpi_train['date'], cpi_train['value'], title='CPI Time Series', label='CPI', ylabel='CPI')

# calculate trend
from src.detrending import calculate_trend
trend_parameters = calculate_trend(cpi_train['t'], cpi_train['value'])

# visualize trend on top of data
# from src.utils_plot import plot_time_series
# from src.detrending import predict_from_linear_coefficients
# trend = predict_from_linear_coefficients(trend_parameters, cpi_train['t'])
# plot_time_series(cpi_train['date'], [cpi_train['value'], trend],color=['navy', 'orange'], title='CPI Time Series', label=['Original Data', 'Linear Trend'], ylabel='CPI')

# subtract trend from data
from src.detrending import subtract_linear_trend
residuals = subtract_linear_trend(cpi_train['t'], cpi_train['value'], trend_parameters)

# plot ACF and PACF
# from src.time_series import plot_acf_pacf
# plot_acf_pacf(residuals)

# fit AR model for multiple lags
rmse_train = []

for n in range(1,8):
    # fit AR model
    from src.time_series import fit_arma_model
    model = fit_arma_model(residuals, order=(n,0))
    
    # predict residuals
    predictions = model.predict(start=n, end=len(residuals)-1)

    # calculate RMSE
    from src.validation import rsme
    rmse = rsme(predictions, residuals[n:])
    rmse_train.append((n,rmse))

# plot RMSE against number of lags
from src.time_series import plot_ar_rmse
plot_ar_rmse(rmse_train)
