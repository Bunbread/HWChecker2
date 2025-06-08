def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True  

    if n % 2 == 0 or n % 3 == 0:
        return False  

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def get_prime_factors(n):
    factors = []
    d = 2
    temp_n = n
    while d * d <= temp_n:
        if temp_n % d == 0:
            factors.append(d)
            temp_n //= d
        else:
            d += 1
    if temp_n > 1:
        factors.append(temp_n)
    return factors
