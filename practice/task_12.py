def merge(a, b):
    merged = [] 
    a = a[::-1]
    b = b[::-1] 
    while b:
        while a and a[-1] < b[-1]:
            merged.append(a.pop())
        merged.append(b.pop())
    merged.extend(a[::-1])
    return merged

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(merge(a, b))