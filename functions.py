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

def generate_lcm_steps(numbers):
    steps = []
    
    steps.append(f"**โจทย์:** หา ค.ร.น. ของ {', '.join(str(num) for num in numbers)}")
    
    all_prime_factors = {}
    for num in numbers:
        factors = get_prime_factors(num)
        all_prime_factors[num] = factors
        steps.append(f"- {num} = {' x '.join(str(f) for f in factors)}")
        
    max_prime_powers = {}
    for num, factors in all_prime_factors.items():
        for factor in factors:
            count = factors.count(factor)
            if factor not in max_prime_powers or count > max_prime_powers[factor]:
                max_prime_powers[factor] = count
                
    lcm_components = []
    for prime, count in max_prime_powers.items():
        component = f"{prime}^{count}" if count > 1 else str(prime)
        lcm_components.append(component)
        
    
    return "\n".join(steps)
