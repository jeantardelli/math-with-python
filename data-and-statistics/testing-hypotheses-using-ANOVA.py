"""
Suppose we have designed an experiment that tests two new processes against the
current process and we want to test whether the results of these new processes
are different from the current process. In this case, we can use Analysis of
Variance (ANOVA) to help us determine whether there are any differences between
the mean values of the three sets of results (for this, we need to assume that
each sample is drawn from a normal distribution with a common variance).

This module illustrates how to use ANOVA to compare multiple samples with one
another.
"""
from scipy import stats
from numpy.random import default_rng

rng = default_rng(12345)

current = rng.normal(4.0, 2.0, size=40)
process_a = rng.normal(6.2, 2.0, size=45)
process_b = rng.normal(4.5, 2.0, size=64)

significance = 0.05
f_stat, p_value = stats.f_oneway(current, process_a, process_b)

print(f"F-stat: {f_stat}, p-value: {p_value}")
# F-stat: 9.949052026027028, p-value: 9.732322721019206e-05

if p_value <= significance:
    print("Reject H0: there is a difference between means")
else:
    print("Accept H0: all means are equal")
# Reject H0: there is a difference between means
