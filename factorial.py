# Finding the nth Factorial number (using recursion):
def factorial(n):
    if n > 1:
        return n * factorial(n-1)  
    return 1

print(factorial(int(input("Enter the nth Factorial number: "))))



# Finding the nth Factorial number (no recursion):
def fact(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

print(fact(int(input("Enter the nth Factorial number: "))))