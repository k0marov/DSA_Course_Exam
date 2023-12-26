def insertion_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        k = i
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            swaps += 1
            k -= 1
    return swaps

a = list(map(int, input().split()))
print(insertion_sort(a))
print(*a)