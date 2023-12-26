def sum(a, b):
    c = 10 
    res = [] 
    if len(a) > len(b):
        a, b = b, a 
    n = len(b)
    a = [0]*(n-len(a)) + a

    res = [0]*n
    carry = 0 
    for i in range(n-1, -1, -1):
        s = a[i]+b[i]+carry
        if s >= c:
            carry = s // c
            s = s % c
        else:
            carry = 0 
        res[i] = s 
    if carry:
        res = [carry]+res
    return res

def p(a, k):
    c = 10
    res = [0]*len(a)
    carry = 0 
    for i in range(len(a)-1, -1, -1):
        elem = a[i]*k+carry
        if elem >= c:
            carry = elem // c 
            elem %= c  
        res[i] = elem
    if carry: 
        res = [carry]+res 
    return res

def product(a, b):
    a = list(map(int, a))
    b = list(map(int, b))
    if len(a) > len(b):
        a, b = b, a
    n = len(b)
    a = [0]*(n-len(a)) + a
    c = 10

    res = [] 
    power = 0
    for i in range(n-1, -1, -1):
        res = sum(res, p(a, b[i]) + [0]*power)
        power += 1
    for first_dig in range(len(res)):
        if res[first_dig] != 0:
            break
    return res[first_dig:]

print(product(input(), input()))