"""
Test statistics and numerical reasoning are good for systematically analyzing
sets of data. However, they don't really give us a good picture of the whole
set of data like a plot would. Numerical values are definitive but can be
difficult to understand, especially in statistics, whereas a plot instantly
illustrates differences between sets of data and trends. For this reason, there
is a large number of libraries for plotting data in ever more creative ways. One
particularly interesting package for producing plots of data is Bokeh, which
allows us to create interactive plots in the browser by leveraging JavaScript
libraries.

This module illustrates how to use Bokeh to create an interactive plot that can
be displayed in the browser.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng
from bokeh import plotting as bk

rng = default_rng(12345)
date_range = pd.date_range("2020-01-01", periods=50)
data = np.add.accumulate(rng.normal(0, 3, size=50))
series = pd.Series(data, index=date_range)

bk.output_file("data-and-statistics/sample.html")

fig = bk.figure(title="Time series data",
                x_axis_label="date",
                x_axis_type="datetime",
                y_axis_label="value")

fig.line(date_range, series)
bk.show(fig)
