# CSPC — Computer Science for Physics and Chemistry

My coursework repository for the course.
Each practical lives under `PW<n>/Lab <X>/`.

## Setup

Create and activate the environment for a given lab:

```bash
conda env create -f "PW<n>/Lab <X>/environment.yml"
conda activate cspc
```

Run the tests for a lab from inside its folder:

```bash
cd "PW<n>/Lab <X>"
pytest -v
```

---

## PW1 — Lab A: Reproducible Foundations

**What I built:**
- I built tests for decay and speed.py file for comparison of pure python and numPy version.

**Speed comparison (loop vs NumPy):**

| version | time (s) |
|---------|----------|
| pure-Python loop | 0.17314654307902015 |
| NumPy (vectorised) | 0.00011300942475463967 |

- Speed-up: **1525.63  × faster**

**Tests:** all passing? YES

**Conclusion:**
- Tests passed correctly, simulation gives close values to scientific formula.
- I have observed that
using numpy makes the simulation 1526.52 times faster rather using pure python code with loop.

---

---

# PW2 — Lab A: Motion from Tracking Data

## What I Built
I developed a Python script called `analysis.py` to analyze free-fall motion using time and position data. The program calculates velocity and acceleration from the given measurements and plots the results, allowing us to compare noisy data with smoother results.

## Derivative Noise Problem
First, the data from `freefall.csv` was imported into two arrays, `t` and `y`, representing time and position. The `np.gradient()` function was then used to calculate velocity by differentiating position with respect to time. Acceleration was obtained by applying the same method to the velocity values.

The calculated mean acceleration was **-8.5796875 m/s²**, which differs from the theoretical gravitational acceleration of -9.81 m/s². Furthermore, the standard deviation was **28.71**, indicating significant variations in the calculated acceleration.

These results demonstrate that applying differentiation twice can amplify noise in the original measurements. This happens because numerical differentiation involves subtracting nearby values and dividing the difference by a small time interval, which can magnify even minor measurement errors.

## Noise Comparison (Differentiation and Integration)
In the next step, the acceleration data was integrated to reconstruct velocity. The reconstructed velocity was then integrated again to obtain position.

By comparing the resulting graphs, we can observe that the reconstructed velocity and position curves are smoother than the original results obtained through repeated differentiation.

This comparison illustrates how numerical integration can reduce the effect of rapid fluctuations in the data and produce smoother curves.

## Conclusion
Differentiation is sensitive to noise in measured data because small variations between consecutive values can lead to significant changes in the calculated derivatives. When differentiation is performed twice, these fluctuations may become even more pronounced, resulting in inaccurate acceleration values.

Integration can help reconstruct smoother velocity and position curves from acceleration data. In this experiment, integrating acceleration to obtain velocity and then integrating velocity to recover position produced smoother graphs. However, integration does not always eliminate noise completely; its effectiveness depends on the data and the numerical method used.

Overall, this experiment demonstrates the limitations of numerical differentiation when working with noisy measurements and shows how integration can be useful for reconstructing motion data.

---