[T,N] = list(map(int,input().split()))
time = list(map(int,input().split()))
value = list(map(int,input().split()))
dp = [[0]*(N+1) for _ in range(T+1)]
for i in range(1,T+1):
    for j in range(1,N+1):
        if time[j-1] <= i:
            dp[i][j] = max(dp[i][j-1],dp[i-time[j-1]][j-1]+value[j-1])
        else:
            dp[i][j] = dp[i][j-1]

print(dp[T][N])