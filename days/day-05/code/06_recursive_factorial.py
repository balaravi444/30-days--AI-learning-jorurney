# Problem 6 - Recursive Factorial
# Day 05 - Advanced Functions & Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial =", factorial(5))
