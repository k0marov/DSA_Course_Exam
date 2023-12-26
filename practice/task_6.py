def is_prime(a):
    for d in range(2, int(a**0.5)+1):
        if a % d == 0:
            return False 
    return True

print(is_prime(int(input())))