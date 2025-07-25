def prime_factors(num):
    factors = []
    factor = 2
    print("Num:", num)
    while num > 1:
        if num % factor == 0:
            factors.append(factor)
            num /= factor
        else:
            factor += 1
    return factors

print(prime_factors(int(input("Which number to Prime Factorise? "))))