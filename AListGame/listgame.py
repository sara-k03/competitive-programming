# PRIME FACTORIZATION

import math

def prime_factors(X): # had this alg from before
    k = 0
    while X % 2 == 0: # eliminates checking even factors 
        k += 1
        X = X // 2
    # checking rest
    i = 3
    max_factor = math.isqrt(X) + 1
    while i <= max_factor:
        while X % i == 0:
            k += 1
            X = X // i
            max_factor = math.isqrt(X) + 1
        i += 2
    if X > 1:
        k += 1
    return k

X = int(input())
print(prime_factors(X))