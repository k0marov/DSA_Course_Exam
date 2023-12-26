def a(n):
    n += 1 
    dp = [0]*n 
    dp[0] = dp[1] = 1 
    for i in range(n): 
        k = i // 2
        if i % 2: 
            dp[i] = dp[k] - dp[k-1]
        else: 
            dp[i] = dp[k] + dp[k-1]

    return dp[n-1]


n = int(input())
print(a(n))