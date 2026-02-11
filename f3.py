def prime_status(n):
    if n <= 1:
        return False
        
    factors = [x for x in range(2, n) if n % x == 0]
    
    if len(factors) > 0:
        return False
    else:
        return True

print(prime_status(29))
