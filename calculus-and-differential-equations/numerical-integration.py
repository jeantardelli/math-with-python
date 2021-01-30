"""
This module contains code that computes numerical integrals with Scipy
"""
import numpy as np

from scipy import integrate

def erf_integrand(t):
    """Represents the integrand of a Gaussian Error Function."""
    return np.exp(-t**2)

val_quad, err_quad = integrate.quad(erf_integrand, -1., 1.) # Using QUADPACK
val_quar, err_quar = integrate.quadrature(erf_integrand, -1., 1.) # Using Quadrature

print(val_quad, err_quad)
print(val_quar, err_quar)
