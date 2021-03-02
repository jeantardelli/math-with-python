"""
One of the most common tasks in statistics is to test the validity of a
hypothesis about the mean of a normally distributed population given that you
have collected sample data from that population. For example, in quality
control, we might wish to test that the thickness of a sheet produced at a mill
is 2 mm. To test this, we would randomly select sample sheets and measure the
thickness to obtain our sample data. Then, we can use a t-test to test our null
hypothesis, H_0 , that the mean paper thickness is 2 mm, against the alternative
hypothesis, H_1 , that the mean paper thickness is not 2 mm.

This module illustrates how to use a t-test to test whether the assumed population
mean is valide given a sample.
"""
import pandas as pd
from scipy import stats

sample = pd.Series([
    2.4, 2.4, 2.9, 2.6, 1.8, 2.7, 2.6, 2.4, 2.8, 2.4, 2.4,
    2.4, 2.7, 2.7, 2.3, 2.4, 2.4, 3.2, 2.2, 2.5, 2.1, 1.8,
    2.9, 2.5, 2.5, 3.2, 2. , 2.3, 3. , 1.5, 3.1, 2.5, 3.1,
    2.4, 3. , 2.5, 2.7, 2.1, 2.3, 2.2, 2.5, 2.6, 2.5, 2.8,
    2.5, 2.9, 2.1, 2.8, 2.1, 2.3
])

mu0, significance = 2.0, 0.05
t_statistic, p_value = stats.ttest_1samp(sample, mu0)

print(f"t stat: {t_statistic}, p-value: {p_value}")
# t stat: 9.752368720068665, p-value: 4.596949515944238e-13

if p_value <= significance:
    print("Reject H0 in favour of H1: mu != 2.0")
else:
    print("Accept H0: mu = 2.0")
# Reject H0 in favour of H1: mu != 2.0
