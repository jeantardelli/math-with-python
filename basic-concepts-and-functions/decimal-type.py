"""
This module illustrates the Decimal object, that is useful for accurate
arithmetic operations.
"""
from decimal import Decimal
from decimal import getcontext
from decimal import localcontext

num1 = Decimal('1.1')
num2 = Decimal('1.563')

print(num1 + num2) # Decimal('2.663')

ctx = getcontext()
num = Decimal('1.1')

print(num ** 4) # Decimal('1.4641')
ctx.prec = 4
print(num ** 4) # Decimal('1.464')

num = Decimal('1.1')
with localcontext() as ctx:
    ctx.prec = 2
    print(num ** 4) # Decimal('1.5')
print(num ** 4) # Decimal('1.4641')
