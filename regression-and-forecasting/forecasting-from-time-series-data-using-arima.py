"""
Unfortunately, ARMA models cannot accommodate time series that have some
underlying trend; that is, they are not stationary time series. We can often get
around this by differencing the observed time series one or more times until we
obtain a stationary time series that can be modeled using ARMA. The
incorporation of differencing into an ARMA model is called an ARIMA model, which
stands for Autoregressive (AR) Integrated (I) Moving Average (MA).

Differencing is the process of computing the difference of consecutive terms in
a sequence of data. So, applying first-order differencing amounts to subtracting
the value at the current step from the value at the next step (t_i+1 - t_i ).
This has the effect of removing the underlying upward or downward linear trend
from the data. This helps to reduce an arbitrary time series to a stationary
time series that can be modeled using ARMA. Higher-order differencing can
remove higher-order trends to achieve similar effects

An ARIMA model is usually written as ARIMA (p, d, q), The p and q order
parameters are the order of the autoregressive component and the moving average
component, respectively. The third order parameter, d, is the order of
differencing to be applied.

This module illustrates how to fit an ARIMA model to a non-stationary time
series and use this model to make forecasts about future values.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

from tsdata import generate_sample_data

sample_ts, test_ts = generate_sample_data(trend=0.2, undiff=True)

ts_fig, ts_ax = plt.subplots(tight_layout=True)
sample_ts.plot(ax=ts_ax, c="b", label="Observed")
ts_ax.set_title("Training time series data")
ts_ax.set_xlabel("Date")
ts_ax.set_ylabel("Value")

diffs = sample_ts.diff().dropna()

ap_fig, (acf_ax, pacf_ax) = plt.subplots(2, 1, tight_layout=True, sharex=True)
sm.graphics.tsa.plot_acf(diffs, ax=acf_ax)
sm.graphics.tsa.plot_pacf(diffs, ax=pacf_ax)
acf_ax.set_ylabel("Value")
pacf_ax.set_xlabel("Lag")
pacf_ax.set_ylabel("Value")

model = sm.tsa.ARIMA(sample_ts, order=(1, 1, 1))
fitted = model.fit(trend="c")
print(fitted.summary())

forecast, std_err, fc_ci = fitted.forecast(steps=50)
forecast_dates = pd.date_range("2021-01-01", periods=50)
forecast = pd.Series(forecast, index=forecast_dates)
forecast.plot(ax=ts_ax, c="g", label="Forecast")
ts_ax.fill_between(forecast_dates, fc_ci[:, 0], fc_ci[:, 1], color="r", alpha=0.4)

test_ts.plot(ax=ts_ax, c="k", label="Actual")
ts_ax.legend()

plt.show()
