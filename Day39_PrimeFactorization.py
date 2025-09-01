
def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:   
            factors.append(divisor)
            n //= divisor      
        else:
            divisor += 1       
    return factors


print(prime_factors(60))   # [2, 2, 3, 5]
print(prime_factors(97))   # [97] (since 97 is prime)
