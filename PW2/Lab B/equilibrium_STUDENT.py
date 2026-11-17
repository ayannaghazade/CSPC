"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6

def k_imbalance(x):
    return (2*x)**2 / ((1-x)*(1-x)) - K
def derivative(x):
    return 8*x / (1-x)**3

x_newton = newton(k_imbalance, x0=0.5, fprime=derivative)

print("Newton equilibrium x:", x_newton)
def objective(x):
    return k_imbalance(x[0])**2

result = minimize(
    objective,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 0.999)]
)

x_slsqp = result.x[0]

print("SLSQP equilibrium x:", x_slsqp)
n_H2 = 1 - x_newton
n_I2 = 1 - x_newton
n_HI = 2 * x_newton

print("H2:", n_H2)
print("I2:", n_I2)
print("HI:", n_HI)
x = np.linspace(0, 0.99, 100)

H2 = 1 - x
I2 = 1 - x
HI = 2*x

plt.plot(x, H2, label="H2")
plt.plot(x, I2, label="I2")
plt.plot(x, HI, label="HI")

plt.axvline(x_newton, linestyle="--", label="Equilibrium")

plt.xlabel("Reaction extent (x)")
plt.ylabel("Amount (mol)")
plt.legend()

plt.savefig("equilibrium.png")
plt.show()

