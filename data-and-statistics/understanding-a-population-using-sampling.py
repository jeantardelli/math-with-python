"""
One of the central problems in statistics is to make estimations — and quantify
how good these estimations are — of the distribution of an entire population
given only a small (random) sample. A classic example is to estimate the average
height of all the people in a country when measuring the height of a randomly
selected sample of people. These kinds of problems are particularly interesting
when the true population distribution, by which we usually mean the mean of the
whole population, cannot feasibly be measured. In this case, we must rely on our
knowledge of statistics and a (usually much smaller) randomly selected sample to
estimate the true population mean and standard deviation, and also quantify how
good our estimations are. It is the latter that is the source of confusion,
misunderstanding, and misrepresentation of statistics in the wider world.

This module illustrates how to estimate the population mean and give a
confidence interval fo these estimates.
"""
import math
import pandas as pd

from scipy import stats

sample_data = pd.Series([
    172.3, 171.3, 164.7, 162.9, 172.5, 176.3, 174.8, 171.9,
    176.8, 167.8, 164.5, 179.7, 157.8, 170.6, 189.9, 185. ,
    172.7, 165.5, 174.5, 171.5])

sample_mean = sample_data.mean()
sample_std = sample_data.std()

print(f"Mean: {sample_mean}, st. dev: {sample_std}")
# Mean: 172.15, st. dev: 7.473778724383846

N = sample_data.count()
std_err = sample_std/math.sqrt(N)

cv_95, cv_99 = stats.t.ppf([0.975, 0.995], df=N-1)

pm_95 = cv_95 * std_err
pm_99 = cv_99 * std_err
conf_interval_95 = [sample_mean - pm_95, sample_mean + pm_95] 
conf_interval_99 = [sample_mean - pm_99, sample_mean + pm_99]

print(f"95% confidence: {conf_interval_95}")
print(f"99% confidence: {conf_interval_99}")
# 95% confidence: [168.65216388659374, 175.64783611340627]
# 99% confidence: [167.36884119608774, 176.93115880391227]
