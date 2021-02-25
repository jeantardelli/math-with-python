"""
Descriptive statistics, or summary statistics, are simple values associated
with a set of data, such as the mean, median, standard deviation, minimum,
maximum, and quartile values. These values describe the location and spread of
a dataset in various ways. The mean and median are measures of the center
(location) of the data, and the other values measure the spread of the data
from the mean and median. These statistics are vital in understanding a
dataset and form the basis for many techniques for analysis.

This module illustrates how to generate descriptive statistics for each
column in a DataFrame.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng

rng = default_rng(12345)

uniform = rng.uniform(1, 5, size=100)
normal = rng.normal(1, 2.5, size=100)
bimodal = np.concatenate([rng.normal(0, 1, size=50),
                          rng.normal(6, 1, size=50)])

df = pd.DataFrame({
    "uniform": uniform,
    "normal": normal,
    "bimodal": bimodal
})

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, tight_layout=True)

df["uniform"].plot(kind="hist", title="Uniform", ax=ax1)
df["normal"].plot(kind="hist", title="Normal", ax=ax2)
df["bimodal"].plot(kind="hist", title="Bimodal", ax=ax3)

descriptive = df.describe()
descriptive.loc["kurtosis"] = df.kurtosis()

print(descriptive)
#             uniform      normal     bimodal
#count     100.000000  100.000000  100.000000
#mean        2.813878    1.087146    2.977682
#std         1.093795    2.435806    3.102760
#min         1.020089   -5.806040   -2.298388
#25%         1.966120   -0.498995    0.069838
#50%         2.599687    1.162897    3.100215
#75%         3.674468    2.904759    5.877905
#max         4.891319    6.375775    8.471313
#kurtosis   -1.055983    0.061679   -1.604305

uniform_mean = descriptive.loc["mean", "uniform"]
normal_mean = descriptive.loc["mean", "normal"]
bimodal_mean = descriptive.loc["mean", "bimodal"]

ax1.vlines(uniform_mean, 0, 20)
ax2.vlines(uniform_mean, 0, 25)
ax3.vlines(uniform_mean, 0, 12)

plt.show()
