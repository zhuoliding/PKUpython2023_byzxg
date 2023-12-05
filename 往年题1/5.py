n, a = map(int,input().split())
sum = 0
for i in range(1,n+1):
    sum += a*i*(10**(n-i))
print(sum)