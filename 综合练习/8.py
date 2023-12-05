[T,N] = list(map(int,input().split()))
time = list(map(int,input().split()))
value = list(map(int,input().split()))
dp =[[0 for _ in range(T+1)] for _ in range(N+1)]
for i in range(T):
    for j in range(N):
        if i+1 <= time[j]:
            dp[j+1][i+1] = dp[j][i+1]
        else:
            c = (i+1)//time[j]
            valu = dp[j][i+1]
            for k in range(1,c+1):
                if dp[j][i+1-k*time[j]] + k*value[j] > valu:
                    valu = dp[j][i+1-k*time[j]] + k*value[j]
            dp[j+1][i+1] = valu
print(dp[N][T])



