"""
Simple linear regression, as seen in the previous recipe, is excellent for
producing simple models of a relationship between one response variable and one
predictor variable. Unfortunately, it is far more common to have a single
response variable that depends on many predictor variables. Moreover, we might
not know which variables from a collection make good predictor variables. For
this task, we need multilinear regression.

This module illustrates how to use multilinear regression to explore the
relationship between a response variable and several predictor variables.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

from numpy.random import default_rng

rng = default_rng(12345)
p_vars = pd.DataFrame({
    "const": np.ones((100,)),
    "X1": rng.uniform(0, 15, size=100),
    "X2": rng.uniform(0, 25, size=100),
    "X3": rng.uniform(5, 25, size=100)
})

residuals = rng.normal(0.0, 12.0, size=100)
Y = -10.0 + 5.0 * p_vars["X1"] - 2.0 * p_vars["X2"] + residuals

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, tight_layout=True)
ax1.scatter(p_vars["X1"], Y)
ax2.scatter(p_vars["X2"], Y)
ax3.scatter(p_vars["X3"], Y)

ax1.set_title("Y against X1")
ax1.set_xlabel("X1")
ax1.set_ylabel("Y")
ax2.set_title("Y against X2")
ax2.set_xlabel("X2")
ax3.set_title("Y against X3")
ax3.set_xlabel("X3")

plt.show()

model = sm.OLS(Y, p_vars).fit()
second_model = sm.OLS(Y, p_vars.loc[:, "const":"X2"]).fit()

print(model.summary())
print(second_model.summary())
