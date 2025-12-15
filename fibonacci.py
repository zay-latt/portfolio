from time import perf_counter
import sys

# Calculating the nth Fibonacci number (using memoization):
def fib1(n, memo):
    sys.setrecursionlimit(10_000)
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib1(n-1, memo) + fib1(n-2, memo)
        return memo[n]

def fib(n):
    return fib1(n, {0:0, 1:1})

f1 = int(input("Enter the nth Fibonacci number: "))
start_time = perf_counter()
print(fib(f1))
end_time = perf_counter()
print("Time taken for Memoization computation: ", end_time - start_time, "seconds")


# Calculating the nth Fibonacci number (using tabulation):
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c
    return a

f2 = int(input("Enter the nth Fibonacci number: "))
start_time = perf_counter()
print(fibonacci(f2))
end_time = perf_counter()
print("Time taken for Tabulation computation: ", end_time - start_time, "seconds")
