"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)

V = data[:, 0]
pH = data[:, 1]

slope = np.gradient(pH, V)

index = np.argmax(slope)

equivalence_volume = V[index]

print("Equivalence point:", equivalence_volume, "mL")


fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(V, pH)
ax[0].set_xlabel("Volume of base (mL)")
ax[0].set_ylabel("pH")
ax[0].set_title("Titration Curve")

ax[1].plot(V, slope)
ax[1].axvline(equivalence_volume, linestyle="--")
ax[1].set_xlabel("Volume of base (mL)")
ax[1].set_ylabel("dpH/dV")
ax[1].set_title("Slope of Titration Curve")

plt.tight_layout()
plt.savefig("titration.png")
plt.show()
