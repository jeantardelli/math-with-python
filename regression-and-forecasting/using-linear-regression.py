"""
Linear regression is a tool for modeling the dependence between two sets of
data so that we can eventually use this model to make predictions. The name
comes from the fact that we form a linear model (straight line) of one set of
data based on a second. In the literature, the variable that we wish to model
is frequently called the response variable, and the variable that we are
using in this model is the predictor variable.

This module illustrates how to use the statsmodels package to perform a simple
linear regression to model the relationship between two sets of data.
"""
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

from numpy.random import default_rng

rng = default_rng(12345)

x = np.linspace(0, 5, 25)
rng.shuffle(x)

trend = 2.0
shift = 5.0

y1 = trend * x + shift + rng.normal(0, 0.5, size=25)
y2 = trend * x + shift + rng.normal(0, 5, size=25)

fig, ax = plt.subplots()
ax.scatter(x, y1, c="b", label="Good correlation")
ax.scatter(x, y2, c="r", label="Bad correlation")
ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Scatter plot of data with best fit lines")

pred_x = sm.add_constant(x)

model1 = sm.OLS(y1, pred_x).fit()
model2 = sm.OLS(y2, pred_x).fit()

print(model1.summary())
print(model2.summary())

model_x = sm.add_constant(np.linspace(0, 5))
model_y1 = model1.predict(model_x)
model_y2 = model2.predict(model_x)

ax.plot(model_x[:, 1], model_y1, 'b')
ax.plot(model_x[:, 1], model_y2, 'r')

plt.show()
