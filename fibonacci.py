# Calculating the nth Fibonacci number (using recursion and memoization):
def fib1(n, memo):
    if n in memo:
        return memo[n]
    
    else:
        memo[n] = fib1(n-1, memo) + fib1(n-2, memo)
        return memo[n]


def fib(n):
    memo = {0:1, 1:1}
    return fib1(n, memo)

print(fib(int(input("Enter the nth Fibonacci number: "))))



# Calculating the nth Fibonacci number (using a bottom-up approach):
def fibonacci(n):
    n = abs(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        
        for i in range(n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(int(input("Enter the nth Fibonacci number: "))))
