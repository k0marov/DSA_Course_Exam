def sorted_place(arr, new):
    arr_sorted = [0] + sorted(arr) + [float('inf')]
    for i in range(1, len(arr_sorted)-1):
        if arr_sorted[i-1] <= new <= arr_sorted[i+1]:
            return i
    

a = list(map(int, input().split()))
print(sorted_place(a, int(input())))