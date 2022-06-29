"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

from random import random
from math import sqrt

def solution(n):
    hits = 0
    for q in range(n):
        x = random()
        y = random()
        hits += 1 if sqrt(x**2+y**2) < 1 else 0
    pi = hits / n * 4.0
    print(f"{n,hits,pi=}")
    return pi

decimals = 2
iterations = 10_000_000
assert round(solution(iterations), decimals) == round(3.14159, decimals)

