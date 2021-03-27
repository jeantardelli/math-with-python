"""
Correctly keeping track of units in calculations can be very difficult,
particularly if there are places where different units can be used. For example,
it is very easy to forget to convert between different units – feet/inches into
meters – or metric prefixes – converting 1 km into 1,000 m, for instance.

This module illustrates how to use the Pint package to keep track of units of
measurement in calculations.
"""
import pint

ureg = pint.UnitRegistry(system="mks")

@ureg.wraps(ureg.meter, ureg.second)
def calc_depth(dropping_time):
    # s = u*t + 0.5*a*t*t
    # u = 0; a = 9.81
    return 0.5*9.81*dropping_time*dropping_time

distance = 5280 * ureg.feet

print(distance.to("miles"))
print(distance.to_base_units())
print(distance.to_base_units().to_compact())

depth = calc_depth(0.05 * ureg.minute)
print("Depth:", depth)
# Depth 44.144999999999996 meter
