"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# Function
def f(x):
    return (x - 3)**2 + 1

# First derivative
def df(x):
    return 2 * (x - 3)

# Second derivative
def ddf(x):
    return 2


# 1. Gradient Descent
x = 0
alpha = 0.1

for i in range(100):
    x = x - alpha * df(x)

print("Gradient Descent:", x)


# 2. Newton's Method
x_newton = newton(df, x0=0, fprime=ddf)

print("Newton's Method:", x_newton)


# 3. SLSQP
result = minimize(f, x0=[0], method="SLSQP")

print("SLSQP:", result.x[0])

def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def ddg(x):
    return 12*x**2 - 6


for x0 in [0, 2]:

    # Gradient Descent
    x = x0
    alpha = 0.001

    for i in range(20000):
        x = x - alpha * dg(x)

    print("\nStarting point:", x0)
    print("Gradient Descent:", x)

    # Newton's Method
    x_newton = newton(dg, x0=x0, fprime=ddg)

    print("Newton's Method:", x_newton)
    print("Second derivative:", ddg(x_newton))

    # SLSQP
    result = minimize(g, x0=[x0], method="SLSQP")

    print("SLSQP:", result.x[0])