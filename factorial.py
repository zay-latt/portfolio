from time import perf_counter
import sys

# Calculating the nth Factorial number (using recursion):
def factorial(n):
    sys.setrecursionlimit(10_000)
    if n > 1:
        return n * factorial(n-1)
    return 1

f1 = int(input("Enter the nth Factorial number: "))
start_time = perf_counter()
print(factorial(f1))
end_time = perf_counter()
print("Time taken for Recursive computation: ", end_time - start_time, "seconds")


# Calculating the nth Factorial number (no recursion):
def fact(n):
    sys.setrecursionlimit(10_000)
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

f2 = int(input("Enter the nth Factorial number: "))
start_time = perf_counter()
print(fact(f2))
end_time = perf_counter()
print("Time taken for Non-Recursive computation: ", end_time - start_time, "seconds")