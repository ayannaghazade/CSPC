"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)

t = data[:, 0]
C_measured = data[:, 1]

C0 = C_measured[0]
def error(k):
    predicted = C0 * np.exp(-k[0] * t)
    return np.sum((C_measured - predicted)**2)
result = minimize(
    error,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 5)]
)

k = result.x[0]

print("Fitted rate constant:", k)
plt.scatter(t, C_measured, label="Measured data")

plt.plot(
    t,
    C0 * np.exp(-k * t),
    label="Fitted curve"
)

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.savefig("kinetics.png")
plt.show()
