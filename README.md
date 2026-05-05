# Sparse Linear Systems Solver – Toy Problem

This project demonstrates the verification of a numerical solver for sparse linear systems.

## Method

1. Generate a random sparse matrix (CSR format)
2. Generate a random solution vector x_true
3. Compute right-hand side:
   b = A * x_true
4. Solve:
   A * x = b
5. Compare x with x_true

## Result

The error obtained is on the order of 1e-15, confirming correctness.

## Technologies

- Python
- NumPy
- SciPy
- Google Colab

## Future work

- GPU acceleration (cuDSS)
- Performance benchmarking
- HPC cloud deployment
