# Worksheet 8

This worksheet shows some algorithms in Python.

main.py - contains:
* method solving equation: a * x + b * y + c = 0
* method implementing Monte Carlo method
* method implementing Heron's formula
* calculating the values of the function P (i, j) using dynamic programming.
P(0, 0) = 0.5,
P(i, 0) = 0.0 for i > 0,
P(0, j) = 1.0 for j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) for i > 0, j > 0


For a * x + b * y + c = 0 equation there are also:

README_1.txt - Problem specification and solution algorithm in the form of a list of steps [in polish]

schemat blokowy i drzewo.jpg - Block diagram and solution tree [in polish] 

## Run

In command line run:

```bash
python3 main.py
```
