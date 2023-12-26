# source: https://vporoshok.me/post/2018/10/merge-sort/
def galloping(AB, n, C): 
    C[:] = AB[:n]
    # r — указатель на конец результата # j — место последней вставки
    # m — длина остатка B
    r, j, m = 0, n, len(AB) - n
    for i in range(n):
        # k — степень двойки
        # l — указатель на 2^k-1 элемент k, l = 0, 0
        while l < m and AB[j+l] < C[i]:
            k += 1
            l = 2**k - 1
            if l >= m: l=m-1
            while l >= 0 and AB[j+l] > C[i]: 
                l -= 1
        l += 1
        AB[r:r+l], AB[r+l] = AB[j:j+l], C[i] 
        r, j, m = r + l + 1, j + l, m - l