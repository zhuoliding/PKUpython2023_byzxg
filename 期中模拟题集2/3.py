[a, b, k, l, n] = list(map(int,input().split()))
lis = []
lis.append(k)
lis.append(l)
for i in range(2,n+1):
    lis.append(lis[-1]*a + lis[-2]*b)
print(lis[n])

