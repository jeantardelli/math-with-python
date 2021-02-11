"""
The random module in NumPy provides several alternatives to the default PRNG,
which uses a 128-bit permutation congruential generator. While this is a good
general-purpose random number generator, it might not be sufficient some
particular needs. This module illustrates how to use other PSNG.
"""
from numpy import random

seed_seq = random.SeedSequence()
print(seed_seq)

bit_gen = random.MT19937(seed_seq)
rng = random.Generator(bit_gen)
