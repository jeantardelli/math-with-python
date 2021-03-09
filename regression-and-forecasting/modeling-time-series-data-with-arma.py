"""
Time series, as the name suggests, tracks a value over a sequence of distinct
time intervals. They are particularly important in the finance industry, where
stock values are tracked over time and used to make predictions – known as
forecasting – of the value at some future time. Good predictions coming from
such data can be used to make better investments. Time series also appear in
many other common situations, such as weather monitoring, medicine, and any
places where data is derived from sensors over time.

Time series, unlike other types of data, do not usually have independent data
points. This means that the methods that we use for modeling independent data
will not be particularly effective. Thus, we need to use alternative techniques
to model data with this property. There are two ways in which a value in a time
series can depend on previous values. The first is where there is a direct
relationship between the value and one or more previous values. This is the
autocorrelation property and is modeled by an autoregressive model. The second
is where the noise that's added to the value depends on one or more previous
noise terms. This is modeled by a moving average model. The number of terms
involved in either of these models is called the order of the model.

This module illustrates how to create a model for stationary time series data
with ARMA terms
"""
import matplotlib.pyplot as plt
import statsmodels.api as sm

from tsdata import generate_sample_data

sample_ts, _ = generate_sample_data()

ts_fig, ts_ax = plt.subplots(tight_layout=True)
sample_ts.plot(ax=ts_ax, label="Observed")
ts_ax.set_title("Time series data")
ts_ax.set_xlabel("Date")
ts_ax.set_ylabel("Value")

adf_results = sm.tsa.adfuller(sample_ts)
adf_pvalue = adf_results[1]
print(f"Augmented Dickey-Fuller test:\nP-value: {adf_pvalue}")

ap_fig, (acf_ax, pacf_ax) = plt.subplots(2, 1, sharex=True, tight_layout=True)
sm.graphics.tsa.plot_acf(sample_ts, ax=acf_ax,
                         title="Observed autocorrelation")
sm.graphics.tsa.plot_pacf(sample_ts, ax=pacf_ax,
                          title="Observed partial autocorrelation")
pacf_ax.set_xlabel("Lags")
pacf_ax.set_ylabel("Value")
acf_ax.set_ylabel("Value")

arma_model = sm.tsa.ARMA(sample_ts, order=(1, 1))
arma_results = arma_model.fit()

print(arma_results.summary())

residuals = arma_results.resid
rap_fig, (racf_ax, rpacf_ax) = plt.subplots(2, 1, sharex=True,
                                            tight_layout=True)
sm.graphics.tsa.plot_acf(residuals, ax=racf_ax,
                         title="Residual autocorrelation")
sm.graphics.tsa.plot_pacf(residuals, ax=rpacf_ax,
                          title="Residual partial autocorrelation")
rpacf_ax.set_xlabel("Lags")
rpacf_ax.set_ylabel("Value")
racf_ax.set_ylabel("Value")

fitted = arma_results.fittedvalues
fitted.plot(c="r", ax=ts_ax, label="Fitted")
ts_ax.legend()

plt.show()
