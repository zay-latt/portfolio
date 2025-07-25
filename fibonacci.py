# Calculating the nth Fibonacci number (using memoization):
def fib1(n, memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib1(n-1, memo) + fib1(n-2, memo)
        return memo[n]

def fib(n):
    return fib1(n, {0:1, 1:1})

print(fib(int(input("Enter the nth Fibonacci number: "))))



# Calculating the nth Fibonacci number (using tabulation):
def fibonacci(n):
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
