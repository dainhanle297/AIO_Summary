# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calculation

def approx_sin(x, n):
    sum = 0
    for i in range(n):
        sum += (-1)**i * x**(2*i+1) / factorial(2*i+1)
    return sum

def approx_cos(x, n):
    sum = 0
    for i in range(n):
        sum += (-1)**i * x**(2*i) / factorial(2*i)
    return sum

def approx_sinh(x, n):
    sum = 0
    for i in range(n):
        sum += x**(2*i+1) / factorial(2*i+1)
    return sum

def approx_cosh(x, n):
    sum = 0
    for i in range(n):
        sum += x**(2*i) / factorial(2*i)
    return sum