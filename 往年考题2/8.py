n,x = map(int,input().split())
num = 0
for i in range(1,n+1):
    num += str(i).count(str(x))
print(num)
