N = int(input())
lin = list(map(int,input().split()))
T = int(input())
#print(N,lin,T)
for i in range(0,N):
    for j in range(i+1,N):
        if lin[i]+lin[j] == T:
            print(i,j)
