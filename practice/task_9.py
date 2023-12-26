def sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
    return swaps

a = list(map(int, input().split()))
print(sort(a))
print(*a)