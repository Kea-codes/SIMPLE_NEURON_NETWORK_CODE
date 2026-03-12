# Single Neuron from Scratch

A minimal, educational Python implementation of a single artificial neuron (perceptron-style) using only NumPy — no frameworks, no classes, just raw math.

Perfect for beginners learning the fundamentals of neural networks.

## What this code does

Computes the output of a single neuron with:

- 3 input features
- 3 corresponding weights
- 1 bias term

**Formula used:**


## Code Example

```python
import numpy as np

# ─── Unique inputs ────────────────────────────────
inputs = [1.2, 5.1, 2.1]

# ─── Weights ───────────────────────────────────────
weights = [3.1, 2.1, 8.7]

# ─── Bias (unique per neuron) ─────────────────────
bias = 3

# ─── Forward pass ──────────────────────────────────
output = (inputs[0] * weights[0] +
          inputs[1] * weights[1] +
          inputs[2] * weights[2] + bias)

print(f"Output: {output}")
