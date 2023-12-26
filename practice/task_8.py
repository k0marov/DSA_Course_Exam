def erat(n):
    e = [1]*(n+1)
    e[0] = e[1] = 0
    for d in range(2, len(e)):
        if not e[d]:
            continue
        for d2 in range(d*2, len(e), d):
            e[d2] = 0
    return e

e = erat(int(input())) 
print(e)
print(sum(e))