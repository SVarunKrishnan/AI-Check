def verify_prime(number):
    if number <= 1:
        return False
        
    for candidate in range(2, int(number ** 0.5) + 1):
        if number % candidate == 0:
            return False
            
    return True

print(verify_prime(29))
