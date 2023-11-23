[N,S] = list(map(int,input().split()))
cost = list(map(int,input().split()))
num = list(map(int,input().split()))
spend = [-1 for _ in range(N)]
def value(i,spend):
    if spend[i-1] != -1:
        return spend[i-1]
    elif i == 1:
        spend[0] = cost[0]
        return cost[0]
    elif i > 1:
        if cost[i-1] <= value(i-1,spend) + S:
            spend[i-1] = cost[i-1]
            return cost[i-1]
        else:
            spend[i-1] = value(i-1,spend) + S
            return spend[i-1] 
sum = 0
for i in range(N):
    sum += num[i]*value(i+1,spend)

print(sum)
