[N,M] = list(map(int,input().split()))
situa = [[int(x) for x in input().split()] for _ in range(M)]
situa.sort(key = lambda x: x[0])
sum = 0
i = 0
while N > 0:
    if situa[i][1] >= N:
        sum += N*situa[i][0]
        N = 0
    else:
        sum += situa[i][0]*situa[i][1]
        i += 1
        N -= situa[i-1][1]
print(sum)


