import math

def f(x):
    return x**2

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    return s * h / 2

a = 0
b = 1
n = 100

approx = trapezoidal(f, a, b, n)
exact = 1 / 3

print(approx)
print(exact)
print(abs(approx - exact))
