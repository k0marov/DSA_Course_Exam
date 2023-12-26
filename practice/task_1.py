def sum(a, b, c):
    res = [] 
    carry = 0 
    while a or b:
        d1 = a % c
        d2 = b % c 
        a //= c
        b //= c

        s = d1+d2+carry
        if s >= c:
            carry = s // c
            s = s % c
        else:
            carry = 0 
        res.append(s)
    if carry: res.append(carry) 
    return res[::-1] 

print(sum(int(input()), int(input()), 2))