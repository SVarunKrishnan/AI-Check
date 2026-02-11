def is_prime_number(value):
    if value < 2:
        return False
        
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
        
    return True

print(is_prime_number(29))
