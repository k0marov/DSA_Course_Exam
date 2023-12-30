def z_func(s):
    n = len(s)
    z = [0]*n
    z[0] = n
    l, r = 0, 0 
    for i in range(1, n):
        if i <= r and z[i-l] < r-i+1: # string is inside previously matched substring and its fully cached
            z[i] = z[i-l]
            continue
        # brute force 
        l = i 
        if i > r: # if i is not even inside previous substring, start from scratch
            r = l-1
        while r+1 < n and s[r+1] == s[r+1-l]:
            r += 1 
        z[i] = r-l+1
    return z
def find_substr(text, pat):
    n = len(text)
    m = len(pat)
    matches = [] 
    z = z_func(pat+'#'+text) 
    for i in range(len(text)):
        if z[i+m+1] == m:
            matches.append(i)
    return matches

s = input() 
pat = input() 
print(*find_substr(s, pat))