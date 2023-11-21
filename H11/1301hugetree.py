[N,M] = list(map(int,input().split()))
length = list(map(int,input().split()))
num = 0
start = 0
NN = N
while NN >= 1:
    sum = 0
    for i in range(1+start,N+1):
        sum += length[i-1]
        if sum > M:
            num+= 1
            NN -= i-start-1
            start = i-1
            break
    else:
        NN = 0
        num += 1
print(num)
        




