def routes_to_start(N):
    N += 1
    dp = [0]*N
    dp[-1] = 1 

    for step in range(N-2, -1, -1):
        dp[step] = dp[step+1]
        if step+2 < N:
            dp[step] += dp[step+2]
        if step+3 < N:
            dp[step] += dp[step+3]
    return dp[0]

N = int(input())
print(routes_to_start(N))