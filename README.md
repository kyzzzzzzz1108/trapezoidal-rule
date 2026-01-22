# Numerical Integration with the Trapezoidal Rule

This project implements the trapezoidal rule to approximate a definite integral and compares the numerical result with the exact value.

## Description

The trapezoidal rule divides an interval into equal subintervals and approximates the area under a curve by summing trapezoids. As the number of subintervals increases, the approximation becomes more accurate.

## Files

- `trapezoidal_rule.py`: Python script for numerical integration using the trapezoidal rule.

## Example

The script evaluates the integral of \( x^2 \) over the interval \([0, 1]\), whose exact value is \( 1/3 \). By changing the value of `n`, the accuracy of the approximation can be observed.

## How to run

```bash
python3 trapezoidal_rule.py
