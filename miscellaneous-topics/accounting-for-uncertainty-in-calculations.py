"""
Most measuring devices are not 100% accurate and instead are accurate up to a
certain amount, usually somewhere between 0 and 10%. For instance, a thermometer
might be accurate to 1%, while a pair of digital calipers might be accurate up
to 0.1%. The true value in both of these cases is unlikely to be exactly the
reported value, although it will be fairly close. Keeping track of the
uncertainty in a value is difficult, especially when you have multiple different
uncertainties combined in different ways. Rather than keeping track of this by
hand, it is much better to use a consistent library to do this for you. This is
what the uncertainties package does.

This module illustrates how to quantify the uncertainty of variables and see
how these uncertainties propagate through a calculation.
"""
import pint

from uncertainties import ufloat, umath

ureg = pint.UnitRegistry(system="mks")

seconds = ufloat(3.0, 0.4)
print(seconds) # 3.0+/-0.4

depth = 0.5*9.81*seconds*seconds
print(depth) # 44+/-12

other_depth = ufloat(44, 12)
time = umath.sqrt(2.0*other_depth/9.81)
print("Estimated time:", time)
# Estimated time 3.0+/-0.4

g = 9.81 * ureg.meters / ureg.seconds ** 2
seconds = ufloat(3.0, 0.4) * ureg.seconds

depth = 0.5 * g * seconds ** 2
print(depth)
