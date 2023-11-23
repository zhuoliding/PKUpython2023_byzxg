[V,n] = list(map(int,input().split()))
vol = list(map(int,input().split()))

def max_vol(V,n,list):
    dp = [[0]*(V + 1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,V+1):
            if list[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-list[i-1]]+list[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][V]
print(V-max_vol(V,n,vol))
        
