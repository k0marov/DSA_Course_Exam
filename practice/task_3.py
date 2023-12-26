def fast_power(a, n):
    res = a
    i = 1
    while i < n:
        if i*2 < n:
            res *= res
            i *= 2
        else: 
            res *= a 
            i += 1
    return res

print(fast_power(int(input()), int(input())))