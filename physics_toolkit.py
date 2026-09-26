"""
Physics Research Computing Toolkit

A collection of simple computational tools for physics
and scientific data analysis.
"""

import math


def numerical_derivative(function, x, h=1e-5):
    """Calculate the numerical derivative of a function."""
    return (function(x + h) - function(x - h)) / (2 * h)


def numerical_integration(function, a, b, n=1000):
    """Calculate a definite integral using the trapezoidal rule."""
    dx = (b - a) / n
    total = 0.5 * (function(a) + function(b))

    for i in range(1, n):
        total += function(a + i * dx)

    return total * dx


def mean(values):
    """Calculate the arithmetic mean of a dataset."""
    return sum(values) / len(values)


def standard_deviation(values):
    """Calculate the population standard deviation."""
    average = mean(values)
    variance = sum((x - average) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


if __name__ == "__main__":

    # Example function: f(x) = x^2
    def f(x):
        return x**2

    print("Physics Research Computing Toolkit")
    print("----------------------------------")

    print("Derivative of x^2 at x=2:",
          numerical_derivative(f, 2))

    print("Integral of x^2 from 0 to 3:",
          numerical_integration(f, 0, 3))

    data = [10, 12, 11, 13, 14]

    print("Mean:", mean(data))
    print("Standard deviation:", standard_deviation(data))
